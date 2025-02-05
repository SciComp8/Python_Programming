# Reference:
# https://github.com/SciComp8/Python_Programming/blob/main/Utilities/List/*List_Comprehension.py

import pandas as pd

# Method 1
cat = (X_train.dtypes == 'object')
cat_name = list(cat[cat].index)

# Method 2
cat_name = [col for col in X_train.columns if X_train[col].dtype == "object"]
