# Reference: https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html
# tree's depth: how many splits a tree makes; greater depth, more overfitting
# max_leaf_nodes: maximum number of leaf nodes (terminal nodes) that the tree can have; more leaf nodes, more overfitting

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.copy.html

# 0: Set up coding environment
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

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
# Creates a new object X with a copy of the data and indices from the original,
# so that changes to the copied DataFrame do not affect the original, and vice versa.

# Review data
print(X.describe())
print(X.head())

# 3: Split data into training and validation data
# A larger validation set reduces noise in model quality assessment, making it more reliable. 
# However, this requires sacrificing training data, which can lead to poorer model performance due to a smaller training set.
train_X, val_X, train_y, val_y = train_test_split(X, y, train_size=0.7, test_size=0.3, random_state=9)

# 4: Specify the model and fit the model with training data
sale_model = DecisionTreeRegressor(random_state=9)
sale_model.fit(train_X, train_y)

# 5: Make predictions
val_predictions = sale_model.predict(val_X)
print(val_y.head().tolist())
print(val_predictions[0:5])

# 6: Evaluate the model
print(mean_absolute_error(val_y, val_predictions))

# 7: Compare different max_leave_nodes
max_leaf_nodes_test = [2**1, 2**2, 2**3, 2**4, 2**5]
for max_leaf_nodes in max_leaf_nodes_test:
    mae_test = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, mae_test))

best_max_leaf_nodes = 2**3

# 8: Fit the model with the best argument and all data
best_model = DecisionTreeRegressor(max_leaf_nodes=best_max_leaf_nodes, random_state=9)
best_model.fit(X, y)


