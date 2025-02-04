# Reference:
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dtypes.html
# https://github.com/SciComp8/Python_Programming/blob/main/Artificial_Intelligence/Machine_Learning/Random_Forest_Price_V2.py
# https://github.com/SciComp8/Python_Programming/blob/main/Utilities/List/*List_Comprehension.py

# Only keep numerical columns
df.dtypes
df_clean = df.select_dtypes(exclude=['object'])

# Define a scoring mechanism to evaluate the impact of each missingness management strategy on model performance
def score_rf(rf, X_t=X_train, X_v=X_valid, y_t=y_train, y_v=y_valid):
    rf = RandomForestRegressor(n_estimators=50, random_state=9)
    rf.fit(X_t, y_t)
    preds = rf.predict(X_v)
    return mean_absolute_error(y_v, preds)

# Manage missingness in columns
# 1. Drop columns with missing values
# Method 1:
df_clean = df.dropna(axis=1, how='any')
# how='all': drops a column only if all values are missing

# Method 2: 
col_miss = [col for col in df.columns if df[col].isnull().any()]
df_clean = df.drop(col_miss, axis=1)

df_clean = df.dropna(axis=1, how='any').copy()
# If I modify df_clean without altering df, then using .copy() is a safe practice. 
# If I only read or perform operations that don’t change df_clean, I will not need .copy().

# 2. Drop a column with missing values when the missingness proportion in this column is very high
miss_dist = df.isnull().sum()/len(df)
print(miss_dist)
df_clean = df.drop(columns=['column_name_with_high_miss'])
# df_clean = df.drop(['column_name_with_high_miss'], axis=1)

# 3. Impute the missing values using median or mean
# Method 1:
miss_median = lambda x: x.fillna(x.median())
df["column_name_1"].transform(miss_median)

miss_mean = lambda x: x.fillna(x.mean())
df["column_name_1"].transform(miss_mean)

# Method 2:
from sklearn.impute import SimpleImputer
imputer_median = SimpleImputer(missing_values=np.nan, strategy='median')
imputer_median.fit(df)
df_clean = np.array(imputer_median.transform(df), dtype=np.float32)

imputer_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer_mean.fit(df)
df_clean = np.array(imputer_mean.transform(df), dtype=np.float32)

# 4. Add a new column that shows the location of the imputed entries

# Manage missingness in rows
# 1. Drop rows with missing values
df_clean = df.dropna(axis=0)

