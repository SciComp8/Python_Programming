# The ordinal encoding approach assumes there is an inherent order of categories in the variable.

import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

data_train = pd.read_csv("../data/raw/train.csv")
data_valid = pd.read_csv("../data/raw/valid.csv")

y = data_train["Outcome"]
features = ["Grade_Category", "Age_Category", "BMI_Category"]

ordinal_encoder = OrdinalEncoder()

X_train = ordinal_encoder.fit_transform(data_train[features]) 
X_valid = ordinal_encoder.transform(data_valid[features]) #

# We apply the same ordinal encoding parameters (categorical integer value) that were derived from the training data, without recalculating them on the validation data. 
# This ensures that the variable encoding process remains consistent and that the validation set doesn't influence the encoding statistics.
