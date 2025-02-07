# Reference:
# https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html

# The one-hot encoding approach is suitable when the categorical variable does not show clear ordering.
# However, when the categorical variable takes on > 15 different values (i.e., cardinality), this approach does not work well.
# Cardinality: number of unique entries of a categorical variable.
# We can remove categorical variables with high cardinality, or we can ordinally encode these variables.
# Ordinal encoding: if the validation data contains values that weren't present in the training set, the encoder will raise an error because those new values don't have an assigned integer.

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Define a scoring mechanism to evaluate the impact of each encoding strategy on model performance
def score_encode_strategy(X_t=X_train, X_v=X_valid, y_t=y_train, y_v=y_valid):
    rf = RandomForestRegressor(n_estimators=50, random_state=9)
    rf.fit(X_t, y_t)
    preds = rf.predict(X_v)
    return mean_absolute_error(y_v, preds)

data_train = pd.read_csv("../data/raw/train.csv")
data_valid = pd.read_csv("../data/raw/valid.csv")

y_train = data_train["Methylation_Level"]
y_valid = data_valid["Methylation_Level"]
features = ["Grade_Category", "Age_Category", "BMI_Category"]

# Automatically obtain categorical variables
# Method 1:
data_train = data_train.select_dtypes(include=['object'])
# Method 2:
cat = (data_train.dtypes == 'object')
cat_var_name = list(cat[cat].index)
# boolean Series is stored in the variable cat.
# cat[cat] uses boolean indexing to select only those entries in the Series cat where the value is True. 
# The .index attribute returns the index labels of this filtered Series cat[cat], which are the column names that have data type 'object'.

print("This dataset has the following categorical variables:")
print(cat_name)

# Take a look at the categories in each categorical variable
print("The unique values in 'Grade_Category' column in training data:", data_train['Grade_Category'].unique())
print("\nThe unique values in 'Grade_Category' column in validation data:", data_valid['Grade_Category'].unique())

cat_var_name = [col for col in X_train.columns if X_train[col].dtype == "object"]

# Obtain the number of unique categories in each categorical variable
cat_var_nunique = list(map(lambda col: data_train[col].nunique(), cat_var_name))
cat_var_nunique_d = dict(zip(cat_var_name, cat_var_nunique)) # Create a zip iterator: zip_iterator = zip(list1, list2)
print(cat_var_nunique_d)
# Show the number of unique categories by categorical variable, in ascending order
sorted(cat_var_nunique_d.items(), key=lambda x: x[1])
# One-hot encode categorical variables with cardinality <= 15
cat_oh_yes = [col for col in cat_var_name if data_train[col].nunique() <= 15]
# Remove categorical variables with cardinality > 15
cat_oh_no = list(set(cat_var_name)-set(cat_oh_yes))

print('Categorical columns that will be one-hot encoded:', low_cardinality_cols)
print('\nCategorical columns that will be dropped from the dataset:', high_cardinality_cols)

### OH method 1: 
X_train = pd.get_dummies(data_train[features]) 
X_test = pd.get_dummies(data_test[features]) #

### ! OH method 2: 
OH_encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
# handle_unknown='ignore': prevent errors when the validation set contains classes absent from the training data.
# When an unknown category is encountered during transform, the resulting one-hot encoded columns for this feature will be all zeros. 
# sparse=False: guarantees that the encoded columns are output as a dense NumPy array rather than as a sparse matrix
X_train_OH = pd.DataFrame(OH_encoder.fit_transform(data_train[features])) # data_train[cat_oh_yes]
X_valid_OH = pd.DataFrame(OH_encoder.transform(data_valid[features]))
X_train_OH.index = data_train.index
X_valid_OH.index = data_valid.index

# Select numerical variables
X_train_num = data_train.drop(features, axis=1)
# data_train.dtypes
# X_train_num = data_train.select_dtypes(exclude=['object'])
X_valid_num = data_valid.drop(features, axis=1)

# Combine numerical variables and one-hot encoded variables
X_train = pd.concat([X_train_num, X_train_OH], axis=1)
X_valid = pd.concat([X_valid_num, X_valid_OH], axis=1)
X_train.columns = X_train.columns.astype(str) # Convert each column name in the index to a string data type
X_valid.columns = X_valid.columns.astype(str)

print("The mean absolute error from One-Hot Encoding:") 
print(score_encode_strategy(X_train, X_valid, y_train, y_valid))
