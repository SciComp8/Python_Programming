# The one-hot encoding approach is suitable when the categorical variable does not show clear ordering.
# But, when the categorical variable takes on > 15 different values, this approach does not work well.

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

### Method 1: 
X_train = pd.get_dummies(data_train[features]) 
X_test = pd.get_dummies(data_test[features]) #

### Method 2: 
OH_encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
# handle_unknown='ignore': prevent errors when the validation set contains classes absent from the training data
# sparse=False: guarantees that the encoded columns are output as a dense NumPy array rather than as a sparse matrix
X_train_OH = pd.DataFrame(OH_encoder.fit_transform(X_train[features]))
X_valid_OH = pd.DataFrame(OH_encoder.transform(X_valid[features]))
X_train_OH.index = X_train.index
X_valid_OH.index = X_valid.index

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
