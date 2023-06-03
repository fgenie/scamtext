import pandas as pd
from fire import Fire 
from pathlib import Path

WHOLE = 'v1.csv'
ROOT = Path('data_split/')
if not ROOT.exists():
    ROOT.mkdir(parents=True) 

def main(fraction=0.1, numsplits=3):
    df = pd.read_csv(WHOLE)
    # drop timestamp
    df = df.drop(columns='timestamp')
    # leave only non-nan
    smask = ~(df.spam.isna())
    nmask = ~(df.normal.isna())
    df = df[smask & nmask]

    # make splits
    for i in range(numsplits):
        fpref = f'v2_{i}'
        testidx = df.sample(frac=fraction).index
        dftest = df.loc[testidx]
        dftrain = df.drop(testidx)
        dftest.to_csv(ROOT/f"{fpref}_test.csv", index=False)
        dftrain.to_csv(ROOT/f"{fpref}_train.csv", index=False)
        print(testidx)
        print(len(dftrain),len(dftest))
        




if __name__ == '__main__':
    Fire(main)