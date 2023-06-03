import importlib
from pathlib import Path
import pandas as pd
from typing import Callable, Sequence, Mapping, Any, Union
import re
from fire import Fire
'''
input: 3_inputmsgs.csv (sequence of sms)
output:
    - if decision_only=True
        sequence of boolean decisions (spam true or not)
    - else
        json like object containing decisions 
        
        ```else output example
        response = dict(
            input_txts = input_txts, # input_txts to be diagnosed (inputs)
            voted_spam_fraction = voted_spam_ratio, # fraction of functions that consider each msg is spam.
            decisions = decisions, # is_spam
            num_functions = num_functions,  # number of functions used to decide whether it's a spam       
        )
        ```

'''

def evaldirs(conf):
    evaluate_dirs = (Path(conf.root)/conf.expname).glob(f"{conf.globpattern}{conf.data}*")  
    return [p for p in evaluate_dirs]

def tandem_execution(functions:Sequence[Callable], txt:str)->float:
    # print([func(txt) for func in functions])
    results = pd.Series([func(txt) for func in functions]).mean()
    return results

def preproc(txts:Sequence[str])->Sequence[str]:
    # preproc for engine (as experimented)

    # erase normal urls, typical headers that hide real patterns (e.g. [Web발신, 국외발신, 국제발신])
    headers = ['[Web발신]', '[국외발신]', '[국제발신]']
    headers_pattern = "|".join(map(re.escape, headers)) 
    url_pattern = r"https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"

    processed_txts = [ re.sub(headers_pattern, "", re.sub(url_pattern, "", txt)) for txt in txts]
    newtxt = re.sub(url_pattern, "", txts[0])
    newtxt = re.sub(headers_pattern, "", txts[0])
    
    return processed_txts

def main(
        inputmsgs_csv:str='3_inputmsgs.csv',
        decision_only=False, 
        thld:float=0.35, # affects performance. do not configure this.
        )->Union[Mapping[str,Any],Sequence[bool]]:
    # load checkers
    indiv_checkers = []
    # print('loading')
    for p in Path().glob('funcs/f_*.py'):
        # print('\t', str(p))
        module = importlib.import_module(str(p.parent/p.stem).replace('/', '.'))
        indiv_checkers.append(module.is_spam)
    # load input_txt msgs
    input_txts_ = pd.read_csv(inputmsgs_csv).msgs.tolist() #raw
    input_txts = preproc(input_txts_) # preproc
    voted_spam_ratio = [tandem_execution(indiv_checkers, txt) for txt in input_txts]
    decisions = [r>=thld for r in voted_spam_ratio]
    num_functions = len(indiv_checkers)
    
    if decision_only:
        response = decisions 
    else: 
        response = dict(
            input_txts = input_txts_, # processed input to the checkers
            voted_spam_fraction = voted_spam_ratio, # fraction of functions that consider each msg is spam.
            decisions = decisions, # is_spam
            num_functions = num_functions,  # number of functions used to decide whether it's a spam       
        )
    
    return response
    


if __name__ == "__main__":
    Fire(main)
