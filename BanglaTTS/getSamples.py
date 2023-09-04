import pandas as pd
import csv

def getsample(filename):
    df = pd.read_csv(filename,quoting=csv.QUOTE_NONE)
    df = df[df['\t0'] != '"']['\t0'].apply(lambda x: x.split('\t')[1])
    df = df.apply(lambda x: x.replace('"', ''))
    df = df.apply(lambda x:x.strip(" "))
    df.name = 'words'
    print(len(df))
    for n in range(10):
        df.sample(20).to_csv(f'./banglatts/Samples/{n}.csv',index=False)

if __name__ == '__main__':
    getsample('./BanglaTTS/words.csv')
