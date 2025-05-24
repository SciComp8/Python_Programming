# Reference: https://realpython.com/python-kwargs-and-args/
# Use *args and **kwargs to pass multiple positional arguments or keyword arguments to a function
def make_dict(**kwargs):
    return kwargs

make_dict(alpha = 1, beta = 2, gamma = 6)
# {'alpha': 1, 'beta': 2, 'gamma': 6}


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

# **fit_params
# kwargs is just a variable name. We could call it **hyperparams, **config, or even **stuff_i_have_to_define.
# The double-asterisk unpacking operator ** is what lets us pass a dictionary of arguments as if they were individually specified.
