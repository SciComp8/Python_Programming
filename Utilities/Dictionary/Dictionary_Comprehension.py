# Build the dictionary comprehensions
square = {num: num ** 2 for num in range(9)}
print(square)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

res = {n_est:score_func(n_est) for n_est in range(50, 401, 50)}
# Alternatively
res = {}
for i in range(1,9):
    results[50*i] = get_score(50*i)

import anndata as ad
sum_dict = {gene: 'sum' for gene in adata_replicate.var_names}
# The 'sum' specifies the aggregation method to compute the sum of gene expression values when aggregating data for each gene within the adata_replicate 
