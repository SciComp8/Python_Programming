# The random search approach is efficient as it randomly samples from the set of possible hyperparameters values,
# rather than sampling all combinations of hyperparameters in Grid Search

# Import packages
import xgboost as xgb
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.validation import check_is_fitted
from scipy.sparse import issparse
from sklearn.model_selection import RandomizedSearchCV
from scipy import stats 

# Define the XGBoost classifier with GPU and RandomizedSearchCV
class XGBoostClassifierDMatrix(xgb.XGBClassifier, BaseEstimator, ClassifierMixin):
    """
    Wrapper for XGBoost classifier to accept DMatrix in fit.
    """
    def __init__(self, use_dmatrix=True, **kwargs):
        super().__init__(**kwargs)
        self.use_dmatrix = use_dmatrix
        self.xgb_dm = None  # Track DMatrix if used

    def fit(self, X, y=None, sample_weight=None, eval_set=None, **kwargs):
        if self.use_dmatrix:
            if isinstance(X, xgb.DMatrix):
                self.xgb_dm = X
            else:
                self.xgb_dm = xgb.DMatrix(X, label=y)
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

 
def optimized_random_search_xgb_gpu(X_train, y_train):
    param_grid = {
        'learning_rate': stats.uniform(0.01, 0.1), 
        # Create a continuous uniform distribution that generates random numbers uniformly over [0.01, 0.01+0.1)
        'max_depth': stats.randint(3, 10), 
        # Create a discrete uniform distribution that samples integers from [3, 9]
        'colsample_bytree': stats.uniform(0.5, 0.5),
        'subsample': stats.uniform(0.5, 0.5),
        'reg_lambda': stats.uniform(1, 4),
        'reg_alpha': stats.uniform(0, 1),
        'n_estimators': stats.randint(100, 501),
    }

    model = XGBoostClassifierDMatrix(
        device='cuda',
        enable_categorical=True,
        use_dmatrix=False  # Or True if you want DMatrix
    )

    random_search = RandomizedSearchCV(
        model,
        param_grid,
        n_iter = 30, # Number of parameter settings that are sampled. n_iter trades off runtime vs quality of the solution.
        cv=5,
        scoring='accuracy',
        verbose=1
    )
    random_search.fit(X_train, y_train)

    print(f"Best parameters: {random_search.best_params_}")
    return random_search


# Prepare data
y_train = y_train.drop(columns = ['subject_id'])
y_train = y_train.loc[:, 'Outcome']


# Run the XGBoost classifier
random_search_xgb = optimized_random_search_xgb_gpu(X_train, y_train)

print("Best set of hyperparameters: ", random_search_xgb.best_params_)
print("Best score: ", random_search_xgb.best_score_)

xgb_best = random_search_xgb.best_estimator_
