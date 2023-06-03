import pandas as pd
from fire import Fire 
from utils import count_token

RAW = 'spam_data_v0.csv'

def flatten(df):
    return df
    # # flatten and rebuild
    # listlist = df.spam.apply(lambda txt:txt.split('\n[Web발신]')).tolist()
    # flat = []
    # for l in listlist:
    #     flat += l
    # L = len(flat)
    # L_ = len(df.normal)
    # nor = df.normal.tolist() + ['']*(L-L_)
    # assert len(flat) == len(nor)
    # dat = {
    #     'spam': flat,
    #     'normal': nor, 
    # }
    # flat_df = pd.DataFrame(dat)
    # return flat_df
    
def main(outcsv = 'v1.csv'):
    # read
    df = pd.read_csv(RAW)
    # multiple msgs split, flatten
    multi = df.spam.apply(lambda x: len(x.split('\n[Web발신]'))) > 1
    df_m = df[multi]
    df_m_ = flatten(df_m)
    df_s = df[~multi]    
    df = pd.concat([df_s, df_m_])

    # erase normal urls, typical headers that hide real patterns (e.g. [Web발신, 국외발신, 국제발신])
    headers = ['[Web발신]', '[국외발신]', '[국제발신]']
    for header in headers:
        for col in ['spam', 'normal']:
            df[col] = df[col].apply(lambda txt: txt.replace(header, ''))
            df[col] = df[col].str.replace(r"https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)", "")
    
    # misc. for normal msgs
    df[df.normal=='.'] = ''
    
    # count tokens and record
    stats = df.spam.apply(count_token).describe(percentiles=[0.1*i for i in range(10)])
    # df.normal.apply(count_token)
    print(stats)

    na = df.spam.isna() & df.normal.isna()
    df[~na].to_csv(outcsv, index=False)
    print(f"wrote to {outcsv}")
    return


if __name__ == '__main__':
    Fire(main)