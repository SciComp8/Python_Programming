import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt


file_path = '../raw/sale_data/train.csv'
sale_data = pd.read_csv(file_path)

sale_data.columns
y = sale_data.Price

feature_names = [cname for cname in train_data.columns if sale_data[cname].dtype in ['int64', 'float64']]
X = sale_data[feature_names].copy()

# Review data
print(X.describe())
print(X.head())

rfg_pipeline = Pipeline(steps=[('preprocessor', SimpleImputer()),
                               ('model', RandomForestRegressor(n_estimators=n_est,
                                                               random_state=9))
                              ])


def get_mae(n_est):
    """Return the average MAE over 10 CV folds of a random forest model.
    
    Keyword argument:
    n_estimators -- the number of trees in the forest
    """

    scores = -1 * cross_val_score(rfg_pipeline, X, y, cv=10, scoring='neg_mean_absolute_error')
    return scores.mean()

mae_dict = {n_est:get_mae(n_est) for n_est in range(50, 401, 50)} 

# Visualize n_estimator mapping to the minimum mean absolute error
plt.plot(list(mae_dict.keys()), list(mae_dict.values()))
plt.show()
