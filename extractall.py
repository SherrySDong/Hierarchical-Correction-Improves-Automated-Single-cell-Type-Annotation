import glob
import pandas as pd
import anndata as ad
all_file=glob.glob('../data/*h5ad')
FAILED=open('failed.txt','w')
for the_file in all_file:
    try:
        adata_gex=ad.read_h5ad(the_file)
        data=the_file.replace("h5ad", "_")
        data=the_file.replace("data", "processeddata_observation")
        
        obs_gex=adata_gex.obs
        obs_gex.to_csv(data+"GEX_observation.txt", sep="\t")

    except:
        FAILED.write(the_file)
        FAILED.write('\n')
        pass
