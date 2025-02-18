# Reference:
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dtypes.html
# https://github.com/SciComp8/Python_Programming/blob/main/Artificial_Intelligence/Machine_Learning/Random_Forest_Price_V2.py
# https://github.com/SciComp8/Python_Programming/blob/main/Utilities/List/*List_Comprehension.py
# https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer.fit_transform

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Only keep numerical columns
df.dtypes
df_clean = df.select_dtypes(exclude=['object'])
df_clean = df.select_dtypes(include=['int64', 'float64'])

num_col = [col for col in df.columns if df[col].dtype in ['int64', 'float64']]
df_clean = df[num_col].copy()

### Manage missingness in columns ###
# Define a scoring mechanism to evaluate the impact of each missingness management strategy on model performance
def score_miss_strategy(X_t=X_train, X_v=X_valid, y_t=y_train, y_v=y_valid):
    rf = RandomForestRegressor(n_estimators=50, random_state=9)
    rf.fit(X_t, y_t)
    preds = rf.predict(X_v)
    return mean_absolute_error(y_v, preds)
    
# S1. Drop columns with missing values
# Method 1:
df_clean = df.dropna(axis=1, how='any')
# how='all': drops a column only if all values are missing
# When there are relatively few missing entries in the column (< 20%), dropping this column may yield bad results
# When there are relatively few missing entries in the column (< 20%), dropping columns yields slightly better results than imputation. 
# This could be partly due to noise, or because the chosen imputation method (e.g., filling in the mean) isn’t well-suited to the data. 

# Method 2: 
col_miss = [col for col in df.columns if df[col].isnull().any()]
df_clean = df.drop(col_miss, axis=1)

df_clean = df.dropna(axis=1, how='any').copy()
# If we modify df_clean without altering df, then using .copy() is a safe practice. 
# If we only read or perform operations that don’t change df_clean, we will not need .copy().

# ! Synchronize removal between 2 dataframes
cols_with_missing_X = [col for col in X.columns if X[col].isnull().any()]
print(cols_with_missing_X)
cols_with_missing_test = [col for col in X_test.columns if X_test[col].isnull().any()]
print(cols_with_missing_test) 
# Identify all columns with any missing values in training and test data sets
# Combine two lists and keep only the unique values,  by first concatenating them and then converting the result to a set (which automatically removes duplicates).
cols_with_missing_all = list(set(cols_with_missing_X + cols_with_missing_test))
print(cols_with_missing_all)
X.drop(cols_with_missing_all, axis=1, inplace=True)
X_test.drop(cols_with_missing_all, axis=1, inplace=True)

# S2. Drop a column with missing values when the missingness proportion in this column is very high
miss_dist = df.isnull().sum()/len(df)
print(miss_dist)
df_clean = df.drop(columns=['column_name_with_high_miss'])
df_clean = df.drop(['column_name_with_high_miss'], axis=1) # Equivalent

# S3. Impute the missing values using median or mean
# Although mean imputation is a simple approach, it usually performs remarkably well (with some variation across datasets). 
# Even though there are more sophisticated techniques—such as regression imputation, these methods rarely offer any significant advantage once the data is processed by advanced machine learning models.
# Method 1:
miss_median = lambda x: x.fillna(x.median())
df["column_name_1"].transform(miss_median)

miss_mean = lambda x: x.fillna(x.mean())
df["column_name_1"].transform(miss_mean)

# Method 2:
from sklearn.impute import SimpleImputer
imputer_median = SimpleImputer(missing_values=np.nan, strategy='median')
df_clean = pd.DataFrame(imputer_median.fit_transform(df))
df_clean.columns = df.columns

imputer_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
df_clean = pd.DataFrame(imputer_mean.fit_transform(df))
df_clean.columns = df.columns

# ! Perform imputation on training and validation sets
imputer_mean = SimpleImputer(strategy='mean')
X_train_imputed = pd.DataFrame(imputer_mean.fit_transform(X_train)) # fit_transform; ! exclude the validation data from the fitting of preprocessing steps including imputation
X_valid_imputed = pd.DataFrame(imputer_mean.transform(X_valid)) # transform
# We apply the same imputation parameters (mean) that were derived from the training data, without recalculating them on the validation data. 
# This ensures that the imputation process remains consistent and that the validation set doesn't influence the imputation statistics.

# S4. Add a new column that shows the location of the imputed entries
# Make copies to avoid changing original training and validation data
X_train_new = X_train.copy()
X_valid_new = X_valid.copy()

# For columns with missing values, create a corresponding new column indicating which record will be imputed
for col in col_miss:
    X_train_new[col + '_miss'] = X_train_new[col].isnull()
    X_valid_new[col + '_miss'] = X_valid_new[col].isnull()

# Perform imputation
imputer_mean = SimpleImputer(strategy='mean')
X_train_new_imputed = pd.DataFrame(imputer_mean.fit_transform(X_train_new)) # fit_transform
X_valid_new_imputed = pd.DataFrame(imputer_mean.transform(X_valid_new)) # transform

# As the imputation process removes column names, we place them back to data
X_train_new_imputed.columns = X_train_new.columns
X_valid_new_imputed.columns = X_valid_new.columns

### Manage missingness in rows ###
# S1. Drop rows with any missing values
df_clean = df.dropna(axis=0)

# S2. Drop rows only if the target variable value is missing
df_clean = df.dropna(axis=0, subset=['target_variable_name'])

### Manage missingness pipeline ###
# Read data
df_train = pd.read_csv('../data/feature_train.csv', index_col='Student_ID')
df_valid = pd.read_csv('../data/feature_valid.csv', index_col='Student_ID')
df_test = pd.read_csv('../data/feature_test.csv', index_col='Student_ID')
y_train = pd.read_csv('../data/target_train.csv', index_col='Student_ID')
y_valid = pd.read_csv('../data/target_valid.csv', index_col='Student_ID')
y_test = pd.read_csv('../data/target_test.csv', index_col='Student_ID')

# Initial inspection on data
df_train.columns
df_train.shape()
df_train.head()
df_train.describe()
miss_dist = df_train.isnull().sum()/len(df)
print(miss_dist)

# Drop rows if the target variable value is missing
df_train = df.dropna(axis=0, subset=['target_variable_name'])

# Define a scoring mechanism to evaluate the impact of each missingness management strategy on model performance
def score_miss_strategy(X_t=X_train, X_v=X_valid, y_t=y_train, y_v=y_valid):
    rf = RandomForestRegressor(n_estimators=50, random_state=9)
    rf.fit(X_t, y_t)
    preds = rf.predict(X_v)
    return mean_absolute_error(y_v, preds)

# Strategy 1: systematically drop columns with any missing values
col_miss = [col for col in df_train.columns if df_train[col].isnull().any()]
df_train_reduced = df_train.drop(col_miss, axis=1)
df_valid_reduced = df_valid.drop(col_miss, axis=1)

print("The mean absolute error after droping columns with any missing values:")
print(score_miss_strategy(X_t=df_train_reduced, X_v=df_valid_reduced, y_t=y_train, y_v=y_valid))

# Strategy 2: imputation 
imputer_mean = SimpleImputer(strategy='mean')
df_train_imputed = pd.DataFrame(imputer_mean.fit_transform(df_train)) 
df_valid_imputed = pd.DataFrame(imputer_mean.transform(df_valid)) 
df_train_imputed.columns = df_train.columns
df_valid_imputed.columns = df_valid.columns

print("The mean absolute error after droping columns with any missing values:")
print(score_miss_strategy(X_t=df_train_imputed, X_v=df_valid_imputed, y_t=y_train, y_v=y_valid))

# Preprocess test data
df_test_imputed = pd.DataFrame(imputer_mean.transform(df_test)) 
df_test_imputed.columns = df_test.columns

# Build model and make predictions
rf = RandomForestRegressor(n_estimators=50, random_state=9)
rf.fit(df_train_imputed, y_train)
preds_test = rf.predict(df_test_imputed)

submit_preds = pd.DataFrame({'Id': df_test_imputed.Id, 'Price': preds_test})
submit_preds.to_csv('submit_preds.csv', index=False)
