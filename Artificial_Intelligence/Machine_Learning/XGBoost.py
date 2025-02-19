from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error

xgb_mdl = XGBRegressor(n_estimators=1000, learning_rate=0.05) 

# Fit the model
xgb_mdl.fit(X_train, y_train) 

# Get predictions
preds = xgb_mdl.predict(X_valid) 

# Calculate MAE
mae = mean_absolute_error(preds, y_valid) 

# Uncomment to print MAE
print("The Mean Absolute Error:" , mae)
