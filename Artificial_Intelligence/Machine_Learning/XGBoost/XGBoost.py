# References:
# https://www.analyticsvidhya.com/blog/2016/03/complete-guide-parameter-tuning-xgboost-with-codes-python/

import pandas as pd
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import xgboost as xgb
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.validation import check_is_fitted
from scipy.sparse import issparse
from sklearn.model_selection import GridSearchCV

file_path = ['../raw/sale_data/economics_train.csv', '../raw/sale_data/economics_test.csv']
X = pd.read_csv(file_path[0], index_col='Id')
X_test = pd.read_csv(file_path[1], index_col='Id')
X.drop(axis=0, subset=['GDP'], inplace=True)
y = X.GDP

X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.7, test_size=0.3, random_state=9)

xgb_mdl = XGBRegressor(n_estimators=1000, learning_rate=0.05) 
xgb_mdl.fit(X_train, y_train) 
preds = xgb_mdl.predict(X_valid) 
mae = mean_absolute_error(preds, y_valid) 
print("The Mean Absolute Error:" , mae)

# Optimize XGBoost with GPU
class XGBoostClassifierDMatrix(xgb.XGBClassifier, BaseEstimator, ClassifierMixin):
    """
    Wrapper for XGBoost classifier to accept DMatrix in fit.
    """
    def __init__(self, use_dmatrix=True, **kwargs):
        super().__init__(**kwargs)
        self.use_dmatrix = use_dmatrix
        self.xgb_dm = None 

    def fit(self, X, y=None, sample_weight=None, eval_set=None, **kwargs):
        if self.use_dmatrix:
            if isinstance(X, xgb.DMatrix):
                self.xgb_dm = X
            else:
                self.xgb_dm = xgb.DMatrix(X, label=y) # labels/target values (y) for supervised learning
            super().fit(self.xgb_dm, y, sample_weight=sample_weight, eval_set=eval_set, **kwargs)
        else:
            super().fit(X, y, sample_weight=sample_weight, eval_set=eval_set, **kwargs)
        return self

    def predict(self, X, **kwargs):
        if self.use_dmatrix and not isinstance(X, xgb.DMatrix):
            X = xgb.DMatrix(X)
        return super().predict(X, **kwargs)

    def fit_predict(self, X, y=None, **fit_params):
        self.fit(X, y, **fit_params)
        return self.predict(X)

print(XGBoostClassifierDMatrix.__mro__)

# Why Use DMatrix instead of NumPy array, Pandas DataFrame, SciPy sparse matrix, or CSV file?
# Optimized for fast matrix operations (2-5x faster than raw arrays); required for GPU acceleration (device='cuda'); compresses data (critical for large datasets).

def optimized_grid_search_xgb_gpu(X_train, y_train):
    param_grid = {
        'learning_rate': [0.1, 0.05],
        'max_depth': [3, 5, 7],
        'colsample_bytree': [0.8, 0.7, 0.6, 0.5],
        'subsample': [0.8, 0.7, 0.6, 0.5],
        'reg_lambda': [1, 5],
        'reg_alpha': [0, 1],
        'n_estimators': [100, 500, 1000],
    }

    # Convert to numpy arrays (optional, XGBoost handles DataFrames)
    X_train_np = np.array(X_train)
    y_train_np = np.array(y_train)

    model = XGBoostClassifierDMatrix(
        device='cuda',
        enable_categorical=True,
        use_dmatrix=True # 
    )

    grid_search = GridSearchCV(
        model,
        param_grid,
        cv=5,
        scoring='accuracy',
        verbose=1
    )
    grid_search.fit(X_train_np, y_train_np)

    print(f"Best parameters: {grid_search.best_params_}")
    return grid_search

