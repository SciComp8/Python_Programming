import pandas as pd
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

file_path = ['../raw/sale_data/economics_train.csv', '../raw/sale_data/economics_test.csv']
X = pd.read_csv(file_path[0], index_col='Id')
X_test = pd.read_csv(file_path[1], index_col='Id')
X.drop(axis=0, subset=['GDP'], inplace=True)
y = X.GDP

X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.7, test_size=0.3, random_state=9)

xgb_mdl = XGBRegressor(n_estimators=1000, learning_rate=0.05) 

# Fit the model
xgb_mdl.fit(X_train, y_train) 

# Get predictions
preds = xgb_mdl.predict(X_valid) 

# Calculate MAE
mae = mean_absolute_error(preds, y_valid) 

# Uncomment to print MAE
print("The Mean Absolute Error:" , mae)
