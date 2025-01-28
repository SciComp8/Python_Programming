# Set up coding environment
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

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

# 3: Split data into training and validation data
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=9)

# 4: specify and fit model
sale_model = DecisionTreeRegressor(random_state=9)
sale_model.fit(X, y)

# 5: make predictions
val_predictions = sale_model.predict(val_X)
print(val_y.head())
print(val_predictions[0:5])

# 5: evaluate model
print(mean_absolute_error(val_y, val_predictions))


