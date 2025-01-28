# Set up coding environment
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

file_path = '../raw/sale_data/train.csv'

sale_data = pd.read_csv(file_path)

# 1: Specify prediction target
sale_data.columns
y = sale_data.Price

# 2: Create feature sets
feature_names = ['Area', 'Year', 'GDP', 'Population']
X = sale_data[feature_names]

# Review data
print(X.describe())
print(X.head())

# 3: specify and fit model
sale_model = DecisionTreeRegressor(random_state=9)
sale_model.fit(X, y)

# 4: make predictions
predictions = sale_model.predict(X)
print(predictions)
print(y.head())
print(predictions[0:5])
