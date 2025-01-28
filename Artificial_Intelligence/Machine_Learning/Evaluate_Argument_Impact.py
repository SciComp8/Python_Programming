import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

def get_mae(max_leaf_nodes_test, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes_test, random_state=9)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)


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

# 4: Specify the model and fit the model with training data
sale_model = DecisionTreeRegressor(random_state=9)
sale_model.fit(X, y)

# 5: Make predictions
val_predictions = sale_model.predict(val_X)
print(val_y.head().tolist())
print(val_predictions[0:5])

# 6: Evaluate the model
print(mean_absolute_error(val_y, val_predictions))

# 7: Compare different max_leave_nodes
max_leaf_nodes_test = [5, 25, 50, 100, 250, 500]
for max_leaf_nodes in max_leaf_nodes_test:
    mae_test = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, mae_test))

