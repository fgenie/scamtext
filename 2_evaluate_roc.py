# config 명세
# 여러 결과물을 활용할 경우 --> 여러 디렉토리를 인풋으로 받아서 활용
# pruning threshold
# voting threshold 는 True/False에서 0.5 이겠지만, 이건 분명 조정될 수 있다. 이것도 config로

# parallel execution of the loaded functions¡
from functools import partial
from tqdm import tqdm
from fire import Fire
import pandas as pd 
from omegaconf import OmegaConf
from pathlib import Path 
import re
import wandb
from collections import defaultdict

'''
forest decision process:
- eval() -> nctx_weighting (main()) -> thresholding_votes() (returns scalar)


- thresholding_votes 에서 aggregate = false로 주고 그 포인트에 대해서 false positive, false negative (오류 케이스들) 을 로깅하자.

false positive 가 더 심각하니까 FN은 로깅은 하지만 자세히 들여다보진 않아도 된다.

- roc_curve 함수에다 callback이나 coroutine으로 집어넣어서 false positive를 로깅할 수 있는 방법이 있겠지. 그러나 지금은 그것을 할 때가 아니다. 코드도 많이 고쳐야하고
'''

def evaldirs(conf):
    evaluate_dirs = (Path(conf.root)/conf.expname).glob(f"{conf.globpattern}{conf.data}*")  
    return [p for p in evaluate_dirs]

def load_train_test_data(conf, load_extended_test=False):
    ftrain, ftest = [f"{conf.dataroot}/{conf.data}_{spl}.csv" for spl in ['train', 'test']]
    if load_extended_test:
        ftest = 'data_split/extended_test.csv'
    df_train, df_test = map(pd.read_csv, [ftrain, ftest])
    print(df_test.shape)
    def drop_na(df):
        smask = ~(df.spam.isna() )
        nmask = ~(df.normal.isna())
        df = df[smask & nmask]
        return df
    df_train_, df_test_ = map(drop_na, [df_train, df_test])
    print(f"loading from \n\t{ftrain=},\n\t{ftest=}")
    print('before drop')
    print(df_train.shape)
    print(df_test.shape)
    print('after drop')
    print(df_train_.shape)
    print(df_test_.shape)
    return df_train_, df_test_



def thresholding_votes(vote, thld:float=0.5, aggregate=True):
    pos_rate = (vote >= thld)
    if aggregate:
        pos_rate = pos_rate.mean()
    return pos_rate

def eval(datdf:pd.DataFrame=None, treesdir:str='parentdir'):
    pattern = 'function_*_*_*.py'
    rootdir = Path(treesdir)
    fpaths = rootdir.glob(pattern)
    tp_res, fp_res = dict(), dict() # true positive / false positive (spam / normal)
    for i, file in enumerate(fpaths):
        code = "".join(open(file).readlines())
        exec(code, globals()) # load `is_spam(txt:str)->bool` from function_*_*_*.py
        # if 'f_old' in dir():
        #     assert f_old != is_spam
        tp_res[file.stem] = datdf.spam.apply(is_spam)
        fp_res[file.stem] = datdf.normal.apply(is_spam)
        # f_old = is_spam
    tp_df, fp_df = map(pd.DataFrame, [tp_res, fp_res])
    return tp_df, fp_df

        
def main(config='2_evaluate_config.yaml',
        load_extended_test=False,
        ):
    # assert load_extended_test, f'from may15, we need to load_extended_test'
    conf = OmegaConf.load(config)
    name = f"{Path(config).parent}_niter{Path(config).stem}"
    run = wandb.init(project='scamtext', config=conf, name=name)

    evaluate_dirs = evaldirs(conf)
    df_train, df_test = load_train_test_data(conf, load_extended_test=load_extended_test)
    
    for i, eval_dir in tqdm(enumerate(evaluate_dirs), total = len(evaluate_dirs)):
        train_tp_df, train_fp_df = eval(datdf=df_train, treesdir=eval_dir)     
        test_tp_df, test_fp_df = eval(datdf=df_test, treesdir=eval_dir)
        # save it
        train_tp_df.to_csv(eval_dir/'train_TP_indiv.csv', index=False)
        train_fp_df.to_csv(eval_dir/'train_FP_indiv.csv', index=False)
        test_tp_df.to_csv(eval_dir/'test_TP_indiv.csv', index=False)
        test_fp_df.to_csv(eval_dir/'test_FP_indiv.csv', index=False)
        
        # reading nctx options (k-shots used for generating function)
        pattern = r'n_ctx(\d+)_'
        matches = re.findall(pattern, eval_dir.name)
        nctx = int(matches[0]) if matches else 1
        if not conf.nctx_weighting:
            nctx = 1 # do not weight the followings 
        if i == 0:
            vote_tp_train = pd.concat([train_tp_df.T]*nctx)
            vote_fp_train = pd.concat([train_fp_df.T]*nctx)
            vote_tp_test = pd.concat([test_tp_df.T]*nctx)
            vote_fp_test = pd.concat([test_fp_df.T]*nctx)
        else:
            vote_tp_train = pd.concat([vote_tp_train]+ [train_tp_df.T]*nctx)
            vote_fp_train = pd.concat([vote_fp_train]+ [train_fp_df.T]*nctx)
            vote_tp_test = pd.concat([vote_tp_test]+ [test_tp_df.T]*nctx)
            vote_fp_test = pd.concat([vote_fp_test]+ [test_fp_df.T]*nctx)

    # aggregating (bagging) and thresholding
    tp_train, fp_train = vote_tp_train.mean(), vote_fp_train.mean()
    tp_test, fp_test = vote_tp_test.mean(), vote_fp_test.mean() # tp_* = 투표결과가 0~1사이로 정규화된 결과. thresholding_votes() 를 거쳐야 bool prediction이 됨.
    
    # make evalresultdir
    evalresdir = Path(conf.evaldir)
    if not evalresdir.exists():
        evalresdir.mkdir(parents=True)
    
    # according to the thresholds combinations, record results
    thresholds = [0.01*i for i in range(0,101,1)] #0.05 단위로 thresholding
    
    traindat = []
    testdat = []

    traintxt, testtxt = defaultdict(list), defaultdict(list)
    for thld_spam in thresholds:
        thresholding = partial(thresholding_votes, thld=thld_spam, aggregate=False) # aggregate=false여야 prediciton 결과를 바탕으로 틀린 예시를 골라낼 수 있다.
        tp_train_, tp_test_ = map(thresholding, [tp_train, tp_test]) # tp_* fp_* = 추론 결과이다 (df_* 와 같은 row수 )
        fp_train_, fp_test_ = map(thresholding, [fp_train, fp_test])

        # failed examples logging here (false positive/negative)
        fntxt_train:string = df_train[~tp_train_].spam.tolist() # false negative
        fntxt_test:string = df_test[~tp_test_].spam.tolist()  
        fptxt_train = df_train[fp_train_].normal.tolist() # false positive 
        fptxt_test = df_test[fp_test_].normal.tolist() 

        # make a table row
        traindat.append([thld_spam, tp_train_.mean(), fp_train_.mean(), fntxt_train, fptxt_train])
        testdat.append([thld_spam, tp_test_.mean(), fp_test_.mean(), fntxt_test, fptxt_test])


         

        # old
        res = {
            'TP' : [tp_train_.mean(), tp_test_.mean()],
            'FP' : [fp_train_.mean(), fp_test_.mean()],
        }
        indices = ['train', 'test']
        resdf = pd.DataFrame(res, index=indices)
        print(f"{thld_spam=}")
        print('\t', resdf)

        saveconf = evalresdir/'saved_eval_conf.yaml'
        saveres = evalresdir/f'performance_{conf.data}_thld{thld_spam:.2f}.tsv'
        conf.readdirs = evaluate_dirs 
        with open(saveconf, 'w') as ymlf:
            ymlf.write(OmegaConf.to_yaml(conf))
        resdf.to_csv(saveres, sep='\t')
        # print(f'wrote to {saveconf}')
        print(f'wrote to {saveres}')
    traintxt.update({'thlds': thresholds})
    testtxt.update({'thlds': thresholds})

    # wandb plot and logging
    

    trainwbt = wandb.Table(data=traindat, columns=['thld','TP', 'FP', 'fntxt', 'fptxt'])
    testwbt = wandb.Table(data=testdat, columns=['thld','TP', 'FP', 'fntxt', 'fptxt'])
    train_scatter = wandb.plot.scatter(trainwbt, 'TP', 'FP', 'train_perf')
    test_scatter = wandb.plot.scatter(testwbt, 'TP', 'FP', 'test_perf')
    wandb.log(
        {
            'train_roc': train_scatter,
            'test_roc': test_scatter,
        }
    )
    run.finish()
    return



if __name__ == '__main__':
    Fire(main)