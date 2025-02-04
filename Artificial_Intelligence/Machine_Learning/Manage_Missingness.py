# Manage missingness in columns

# 1. Drop columns with missing values
df_clean = df.dropna(axis=1, how='any')
# how='all': drops a column only if all values are missing

# 2. Drop a column with missing values when the missingness proportion in this column is very high.

# 3. Impute the missing values using median or mean
miss_median = lambda x: x.fillna(x.median())
df["column_name_1"].transform(miss_median)
miss_mean = lambda x: x.fillna(x.mean())
df["column_name_1"].transform(miss_mean)

# Manage missingness in rows
# 1. Drop rows with missing values
df_clean = df.dropna(axis=0)

