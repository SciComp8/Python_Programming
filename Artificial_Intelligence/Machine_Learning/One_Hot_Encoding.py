import pandas as pd
train_data = pd.read_csv("../data/raw/train.csv")
test_data = pd.read_csv("../data/raw/test.csv")

y = train_data["Outcome"]
features = ["Gender", "Ethnicity"]
X = pd.get_dummies(train_data[features]) 
X_test = pd.get_dummies(test_data[features]) #
