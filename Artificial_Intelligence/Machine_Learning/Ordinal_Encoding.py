# Reference:
# https://github.com/SciComp8/Python_Programming/blob/main/Artificial_Intelligence/Machine_Learning/List_Categorical_Variable.py

# The ordinal encoding approach assumes there is an inherent order of categories in the variable.

import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

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

# ! Take a look at the categorical variable
# When we fit an ordinal encoder on the training data, it assigns each unique value a specific integer label. 
# If the validation data contains values that weren't present in the training set, the encoder will raise an error because those new values don't have an assigned integer.
# To address this problem, one way is to tailor an ordinal encoder to handle new categories; another is to remove the problematic categorical variables.
print("The unique values in 'Grade_Category' column in training data:", data_train['Grade_Category'].unique())
print("\nThe unique values in 'Grade_Category' column in validation data:", data_valid['Grade_Category'].unique())
# Obtain categorical variables in the training data
cat_var = [col for col in data_train.columns if data_train[col].dtype == "object"]
# Obtain categorical variables that can be ordinally encoded
cat_var_oe_yes = [col for col in cat_var if set(data_valid[col]).issubset(set(data_train[col]))]       
# Drop categorical variables that CANNOT be ordinally encoded
cat_var_oe_no = list(set(cat_var)-set(cat_var_oe_yes))
X_train = data_train.drop(cat_var_oe_no, axis=1)
X_valid = data_valid.drop(cat_var_oe_no, axis=1)
        
print('Categorical columns that will be ordinal encoded:', good_label_cols)
print('\nCategorical columns that will be dropped from the dataset:', bad_label_cols)

ordinal_encoder = OrdinalEncoder()
X_train[features] = ordinal_encoder.fit_transform(X_train[features]) 
X_valid[features] = ordinal_encoder.transform(X_valid[features]) #
# For these categorical variables, we randomly map each unique category value to a distinct integer. 
# This straightforward method is widely used because it avoids the hassle of crafting custom labels. 
# However, we may achieve better performance by assigning more meaningful, informed labels to ordinal variables.
# ordinal_encoder.transform(X_valid[features]): we apply the same ordinal encoding parameters (categorical integer value) that were derived from the training data, without recalculating them on the validation data. 
# This ensures that the variable encoding process remains consistent and that the validation set doesn't influence the encoding statistics.

print("The mean absolute error from Ordinal Encoding:") 
print(score_encode_strategy(X_train, X_valid, y_train, y_valid))

