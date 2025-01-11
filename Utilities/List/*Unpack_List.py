# Unpack lists
# A list can contain a mix of different types of variables
data = [ 'XYZ', 90, 71.1, (2023, 12, 21) ] 
_, shares, price, _ = data
shares
price

# Extended unpacking
data = [ 'XYZ', 90, 71.1, (2023, 12, 21) ]
_, shares, price, (year, *_) = data
shares
price
year

a, b, *_ = ['a', 'cde', 6, 9, 10]
print(_)
# [6, 9, 10]

*__, a, b = ['a', 'cde', 'bib', 6, 9, 10]
print(__)
# a cde bib 6

*__, a, b, *_ = ['a', 'cde', 'bib', 6, 9, 10]
# We can't have two starred expressions (*__ and *_) in a single unpacking assignment.

line = 'https://ftp.ncbi.nlm.nih.gov/geo/series/GSE85nnn/GSE85241/suppl/GSE85241%5Fcellsystems%5Fdataset%5F4donors%5Fupdated%2Ecsv%2Egz'
ncbi, base_name = line.split('suppl/')
base_name

# Unpack list elements into column names
df = pd.DataFrame(columns=[*adata_cell_pop.var_names, *obs_to_keep])
# The * operator is used to unpack elements from the lists (or any iterable) adata_cell_pop.var_names and obs_to_keep. 
# This operator is often used to unpack iterables in Python.
# For example, if adata_cell_pop.var_names is ['gene1', 'gene2', 'gene3'] and obs_to_keep is ['age', 'gender'], then [*adata_cell_pop.var_names, *obs_to_keep] becomes ['gene1', 'gene2', 'gene3', 'age', 'gender'].

# Swap 2 variables
a = [7, 8, 9, 10, 11]
b = [8, 8, 8, 8, 8]
a, b = b, a
print(a)
print(b)
