import pandas as pd

gene_count = pd.DataFrame({'Gene_1': [25, 90], 'Gene_2': [22, 99]})
gene_count_deep_copy = gene_count.copy() # Deep copy by default

gene_count_deep_copy['Gene_1'][0] = 7  
print(gene_count_deep_copy)
print(gene_count) # Original remains unchanged

gene_count_shallow_copy = gene_count # Shallow copy
gene_count_shallow_copy['Gene_1'][0] = 7  
print(gene_count_shallow_copy)
print(gene_count) # Original remains CHANGED
