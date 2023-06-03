from pathlib import Path
import shutil

import pandas as pd
from typing import Callable, Sequence, Mapping, Any


from omegaconf import OmegaConf
from fire import Fire
'''
1. wrapped
2. wrapped/funcs/
3. copy the functions*.py into 2.

'''

def evaldirs(conf):
    evaluate_dirs = (Path(conf.root)/conf.expname).glob(f"{conf.globpattern}{conf.data}*")  
    return [p for p in evaluate_dirs]

def tandem_execution(functions:Sequence[Callable], txt:str)->float:
    results = pd.Series([func(txt) for func in functions]).mean()
    return results

def main(
        evalconfig:str='config_yamls/cold_ablations/ctx15/4_1.yaml',
        inputmsgs_csv:str='3_inputmsgs.csv',
        thld:float=0.35,
        )->Mapping[str,Any]:
    rootdir = Path('wrapped')
    # rm wrapped if existed
    if rootdir.exists():
        shutil.rmtree('wrapped')
        print('rm -rf wrapped')

    # make root
    rootdir.mkdir()

    # make [rootdir]/funcs/
    fdir = rootdir/'funcs'
    fdir.mkdir()
    
    # read evalconf and find paths for individual checkers (python functions)
    conf = OmegaConf.load(evalconfig)
    dirs = evaldirs(conf)
    indiv_checkers = []
    for dir in dirs:
        for p in dir.glob('function_*_*.py'):
            indiv_checkers.append(p)
    # copy those functions into wrapped/funcs/
    for i,p in enumerate(indiv_checkers):
        newpath = fdir/f"f_{i}.py"
        shutil.copy(str(p), str(newpath))
        print(f'cp {str(p)} {str(newpath)}')
    
    # copy inputcsv and running script.
    print(f'cp 4_1_packaged_run_tandem.py wrapped/')
    print(f'cp 3_inputmsgs.csv wrapped/')
    shutil.copy('4_1_packaged_run_tandem.py', 'wrapped/')
    shutil.copy('3_inputmsgs.csv', 'wrapped/')
    
    
    return
    
    

    

if __name__ == "__main__":
    Fire(main)
