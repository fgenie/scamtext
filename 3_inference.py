'''
parallel execution scenario for profiling in this code is just wrong...
텍스트 16개 측정하는데 하나당 한 번씩 프로세스 생성하는게 말이 되냐... 프로세스 생성을 16배로 측정한 결과가 나오는 것.
'''

import multiprocessing
from multiprocessing import Pool
import importlib
from pathlib import Path
import pandas as pd
from typing import Callable, Sequence, Mapping, Any

from omegaconf import OmegaConf
from fire import Fire

import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time} seconds")
        return result
    return wrapper
'''
load regexp spam checkers
run it
    with multiprocessing 
    with single proceess
to answer a single text input


considered optimal: 
config_yamls/cold_ablations/ctx15_niter4_1 -> ctx15/4_1.yaml
config_yamls/cold_ablations/ctx10_niter5_1

considered sub-optimal:
config_yamls/cold_ablations/ctx10_niter1_3
config_yamls/cold_ablations/ctx10_niter1_1
config_yamls/cold_ablations/ctx3_niter1_0

'''

def evaldirs(conf):
    evaluate_dirs = (Path(conf.root)/conf.expname).glob(f"{conf.globpattern}{conf.data}*")  
    return [p for p in evaluate_dirs]


def run_script(func, txt):
    return func(txt)

def parallel_execution(functions:Sequence[Callable], txt:str)->float:
    cores = multiprocessing.cpu_count()  # get the number of cores
    with Pool(cores) as p:
        results = p.starmap(run_script, [(func, txt) for func in functions])
    results = pd.Series(results).mean()
    return results

def tandem_execution(functions:Sequence[Callable], txt:str)->float:
    results = pd.Series([func(txt) for func in functions]).mean()
    return results

# def batched_call()
#     # i consider if single calls saturates cpu resources, this function would not improve performance.
#     return 

def main():
    do()
    
@timeit
def do(
        evalconfig:str='config_yamls/cold_ablations/ctx15/4_1.yaml',
        multiproc:bool=False,
        inputmsgs_csv:str='3_inputmsgs.csv',
        thld:float=0.35,
        )->Mapping[str,Any]:
    # read evalconf and load individual checkers (python functions)
    conf = OmegaConf.load(evalconfig)
    dirs = evaldirs(conf)
    indiv_checkers = []
    for dir in dirs:
        for p in dir.glob('function_*_*.py'):
            module = importlib.import_module(str(p.parent/p.stem).replace('/', '.'))
            indiv_checkers.append(module.is_spam)
    # load input_txt msgs
    input_txts = pd.read_csv(inputmsgs_csv).msgs.tolist()
    exec_method = parallel_execution if multiproc else tandem_execution
    voted_spam_ratio = [exec_method(indiv_checkers, txt) for txt in input_txts]
    decisions = [r>=thld for r in voted_spam_ratio]
    num_functions = len(indiv_checkers)
    
    response = dict(
        input_txts = input_txts, # input_txts to be diagnosed (inputs)
        voted_spam_fraction = voted_spam_ratio, # fraction of functions that consider each msg is spam.
        decisions = decisions, # is_spam
        num_functions = num_functions,  # number of functions used to decide whether it's a spam       
    )
    return response
    
    

    

if __name__ == "__main__":
    Fire(main)
