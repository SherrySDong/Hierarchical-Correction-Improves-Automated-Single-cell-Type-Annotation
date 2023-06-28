#!/usr/bin/env python3
import os
import glob
import pickle
import pandas as pd
import scanpy as sc

# function is a good way to organize code
# so the script is better organized and easier to maintain
def extract_chunked (input_path, obs_path, chunk_path_prefix, chunk=20000):
    # read h5ad file from input_path
    # write obs information to obs_path
    # and write the real data in chunks to chunk_path_fmt

    # each chunk contains at most "chunk" rows.
        
    # the problem the current program gets killed
    # is that the data file is too big.
    
    # Usually in such case, the library already has
    # some pre-built mechanism to handle this.
    # In this case it's called "backed" mode,
    # which can be enabled by passing in backed='r'

    ds = sc.read_h5ad(input_path, backed='r')

    # save obs, obs is a pandas DataFrame
    # Usually you need to know the data type of something
    # you are operating with.
   
    # assert isinstance(ds.obs, pd.DataFrame)
    ds.obs.to_csv(obs_path, sep='\t')

    # When read with backed mode, X is of type
    #       anndata._core.sparse_dataset.SparseDataset

    # This type supports slicing operations like numpy matrix.
    # What's different is it doesn't read in all the data,
    # but rather read in the portion of data asked for in the
    # slicing operation.  

    N, C = ds.X.shape   

    processed_rows = 0

    columns = list(ds.var.index)

    total_chunks = (N + chunk -1) // chunk
    print("Shape:", ds.X.shape)
    print("Total chunks: %d" % total_chunks)

    for no, offset in enumerate(range(0, N, chunk)):
        sub = ds.X[offset:(offset+chunk), :]
        # sub is of type scipy.sparse._csr.csr_matrix

        # now we need to assemble sub into a dataframe
        # so we can save it to csv file
        
        # get row names from obs
        row_index = list(ds.obs.iloc[offset:(offset+chunk)].index)

        with open('%s%d.pkl' % (chunk_path_prefix, no), 'wb') as f:
            pickle.dump((columns, row_index, sub), f)

        df = pd.DataFrame(sub.todense(), columns=columns)
        df.index = row_index

      #  df.to_csv('%s%d.csv' % (chunk_path_prefix, no), sep='\t')

        print("Extracted chunk %d/%d of %d rows at offset %d..." % (no, total_chunks, df.shape[0], offset))
        processed_rows += df.shape[0]

    # sanity check, the number of processed rows match
    # assert N == processed_rows
    print("Finished processing %s." % input_path)

all_file=glob.glob('../data/*.h5ad')
FAILED=open('failed.txt','w')
for the_file in all_file:
    try:
        # file name is like .../tabula_sapiens_all.h5ad

        # we'll cleanup the name

        bname = os.path.basename(the_file).rsplit('.', 1)[0]
        obs_path = '../processed/%s_obs.csv' % bname
        # %% for single %
        chunk_path_prefix = '../processed/%s_' % bname
        print("Processing %s" % the_file)

        extract_chunked (the_file, obs_path, chunk_path_prefix)
    except:
        raise
        FAILED.write(the_file)
        FAILED.write('\n')
        pass
