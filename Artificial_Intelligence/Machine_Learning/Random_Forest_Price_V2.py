# Reference: 
# https://www.youtube.com/watch?v=2_iKR_fDKNM | NISS AI, Statistics & Data Science in Practice: Lucas Mentch - Random Forests
# Decision trees, while simple and effective, can overfit the training data, making them less reliable for new data. 
# Random forest addresses this by averaging the predictions of many uncorrelated decision trees, reducing the overall error and improving the model's generalizability. 
# This ensures more stable and accurate predictions, even in complex datasets.
# mtry defines the number of variables randomly sampled as candidates at each split
# From the standpoint of model complexity, this parameter in random forests functions similarly to the shrinkage penalty used in explicit regularization methods such as the lasso.

# https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html
# n_estimators: no. of trees in the forest
# criterion{“squared_error”, “absolute_error”, “friedman_mse”, “poisson”}. The function to measure the quality of a split. 
# “squared_error” for the mean squared error, which is equal to variance reduction as feature selection criterion and minimizes the L2 loss using the mean of each terminal node.
# “absolute_error” for the mean absolute error, which minimizes the L1 loss using the median of each terminal node.
# min_samples_split: The minimum number of samples required to split an internal node.
# max_depth: The maximum depth of the tree. If None, then nodes are expanded until all leaves are pure or until all leaves contain less than min_samples_split samples.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# 0: Set up environment
file_path = '../raw/sale_data/train.csv'
sale_data = pd.read_csv(file_path)

# Drop rows with missing values
sale_data = sale_data.dropna(axis=0)

# 1: Specify prediction target
sale_data.columns
y = sale_data.Price

# 2: Create feature sets
feature_names = ['Area', 'Year', 'GDP', 'Population']
X = sale_data[feature_names].copy()

# Review data
print(X.describe())
print(X.head())

# 3: Split data into training and validation data
train_X, val_X, train_y, val_y = train_test_split(X, y, train_size=0.7, test_size=0.3, random_state=9)

# 4: Define several models
rf_1 = RandomForestRegressor(n_estimators=50, random_state=9)
rf_2 = RandomForestRegressor(n_estimators=100, random_state=9)
rf_3 = RandomForestRegressor(n_estimators=100, criterion='absolute_error', random_state=9)
rf_4 = RandomForestRegressor(n_estimators=150, min_samples_split=20, random_state=9)
rf_5 = RandomForestRegressor(n_estimators=150, max_depth=8, random_state=9)

# 5: Specify the model scoring mechanism
def score_rf(rf, X_t=X_train, X_v=X_valid, y_t=y_train, y_v=y_valid):
    rf.fit(X_t, y_t)
    preds = rf.predict(X_v)
    return mean_absolute_error(y_v, preds)

# 6: Evaluate models
rfs = [rf_1, rf_2, rf_3, rf_4, rf_5]
for i in range(0, len(rfs)):
    mae = score_rf(rfs[i])
    print("The mean absolute error of the random forest model %d is: %d" % (i+1, mae))

# 7: Identify the model with best performance
best_rf = rf_5

# 7: Submit predictions using the test data
file_path = '../raw/sale_data/test.csv'
test_data = pd.read_csv(file_path)
test_X = test_data[features].copy()
test_preds = best_rf.predict(test_X)

submit_preds = pd.DataFrame({'Id': test_data.Id, 'Price': test_preds})
submit_preds.to_csv('submit_preds.csv', index=False)
