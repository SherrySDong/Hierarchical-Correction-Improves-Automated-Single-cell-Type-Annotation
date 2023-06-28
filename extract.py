import pandas as pd
import anndata as ad

adata_gex= ad.read_h5ad("local.h5ad")
## print out all informaiton in this file
print(adata_gex)
print(adata_gex.obs)
print(adata_gex.uns)

obs_gex = adata_gex.obs
obs_gex.to_csv("GEX_observation.txt", sep="\t")

feature_gex = adata_gex.var
print(feature_gex)
feature_gex.to_csv("GEX_feature.txt", sep="\t")

count_norm_sizefactor_gex = adata_gex.to_df()
print(count_norm_sizefactor_gex)
count_norm_sizefactor_gex.to_csv("GEX.txt", sep="\t")

