# The one-hot encoding approach is suitable when the categorical variable does not show clear ordering.
# But, when the categorical variable takes on > 15 different values, this approach does not work well.

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

data_train = pd.read_csv("../data/raw/train.csv")
data_valid = pd.read_csv("../data/raw/valid.csv")

y_train = data_train["Methylation_Level"]
y_valid = data_valid["Methylation_Level"]
features = ["Grade_Category", "Age_Category", "BMI_Category"]

# Method 1: 
X_train = pd.get_dummies(data_train[features]) 
X_test = pd.get_dummies(data_test[features]) #

# Method 2: 
OH_encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
# handle_unknown='ignore': prevent errors when the validation set contains classes absent from the training data
# sparse=False: guarantees that the encoded columns are output as a dense NumPy array rather than as a sparse matrix
