# Reference:
# https://github.com/SciComp8/Python_Programming/blob/main/Utilities/List/*List_Comprehension.py

import pandas as pd
X_train = pd.read_csv('../data/raw/training.csv')
cat_var = [col for col in X_train.columns if X_train[col].dtype == "object"]

# Obtain the number of unique categories in each categorical variable
cat_var_nunique = list(map(lambda col: X_train[col].nunique(), cat_var))
