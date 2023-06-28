import pickle
import numpy as np
import os
import sys
import random 
import pandas as pd
import glob

random.seed(sys.argv[1])
## map all cells to binarized cell type
all_obs=glob.glob('../processed/*obs.csv')
#all_obs=glob.glob('../processed/single_nucleus_cross_tissue_obs.csv')

i=0
map_gs={}
for the_file in all_obs:
    df = pd.read_csv(the_file,sep='\t',header=0)
    for the_type in df.cell_type.unique():
        if (the_type in map_gs):
            pass
        else:
            map_gs[the_type]=i
            print(the_type, i)
            i=i+1
### column different cell types. rows: cell. yes: 1, no, 0



all_types=map_gs.keys()
type_len=len(all_types)

the_map={}
all_files=glob.glob('../processed/*obs.csv')
for the_file in all_files:
        FILE=open(the_file,'r')

        line=FILE.readline()
        lll=line.split('\t')
        i=0
        for aaa in lll:
            if aaa == 'cell_type':
                record=i
            i=i+1
        for line in FILE:
            table=line.split("\t")
            val=map_gs[table[record]]
            vector=np.zeros(type_len)
            vector[val]=1
            the_map[table[0]]=vector
        FILE.close()



os.system("mkdir test_gs")
os.system("mkdir train_gs")
all_files=glob.glob('../processed/*obs.csv')
for the_file in all_files:
    aaa = the_file.split('/')
    aaa = aaa[-1].split('_obs.csv')
    name = aaa[0]
    rrr = random.random()
    if (rrr<1.8):
        #train.write(line)
            alldata = glob.glob('../processeddata_sep/' + name + '*')
            for each_data in alldata:
                ttt = each_data.split('/')
                with open(each_data, 'rb') as f:
                    x = pickle.load(f)
                a_list = list(x.index)
                the_gs = open('train_gs/' + ttt[-1], 'w')
                for thecell in a_list:
                    vector=the_map[thecell]
                    the_gs.write(thecell)
                    for val in vector:
                        the_gs.write('\t')
                        the_gs.write(str(val))
                    the_gs.write('\n')
    else:
        #test.write(line)

            alldata = glob.glob('../processeddata_sep/' + name + '*')
            for each_data in alldata:
                ttt = each_data.split('/')
                with open(each_data, 'rb') as f:
                    x = pickle.load(f)
                a_list = list(x.index)
                the_gs = open('test_gs/' + ttt[-1], 'w')
                for thecell in a_list:
                    vector=the_map[thecell]
                    the_gs.write(thecell)
                    for val in vector:
                        the_gs.write('\t')
                        the_gs.write(str(val))
                    the_gs.write('\n')
