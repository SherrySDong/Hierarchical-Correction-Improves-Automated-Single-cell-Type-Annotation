import glob
import os
import sys
GENES=open('selected_genes.txt','r')
gene_list=[]
for ggg in GENES:
    ggg=ggg.strip()
    gene_list.append(ggg)
GENES.close()


import pickle
import pandas as pd

def load_from_pkl (path):
    with open(path, 'rb') as f:
        cols, rows, sub = pickle.load(f)
    df = pd.DataFrame(sub.todense(), columns=cols)
    df.index = rows
    return df



os.system('rm -rf ../processeddata_sep/')
os.system('mkdir ../processeddata_sep/')
## separate each into 100 size files
all_files=glob.glob('../processed/*.pkl')

for the_file in all_files:
    ttt=the_file.split('/')

    df = load_from_pkl(the_file)
    df_new=df[gene_list]
    i=0
    while (i<len(df_new)):
        df_tmp=df_new.iloc[i:i+100]
        df_tmp.to_pickle('../processeddata_sep/'+ttt[-1]+'.'+str(i))
        i=i+100
