# Reference:
# https://github.com/SciComp8/Python_Programming/blob/main/Utilities/List/*List_Comprehension.py
# https://github.com/SciComp8/Python_Programming/blob/main/Utilities/Function/Lambda_Function.py
# https://github.com/SciComp8/Python_Programming/blob/main/Utilities/Tuple/zip.py

import pandas as pd
X_train = pd.read_csv('../data/raw/training.csv')
cat_var_name = [col for col in X_train.columns if X_train[col].dtype == "object"]

# Obtain the number of unique categories in each categorical variable
cat_var_nunique = list(map(lambda col: X_train[col].nunique(), cat_var_name))
cat_var_nunique_d = dict(zip(cat_var_name, cat_var_nunique)) # Create a zip iterator: zip_iterator = zip(list1, list2)
print(cat_var_nunique_d)

# Show the number of unique categories by categorical variable, in ascending order
sorted(cat_var_nunique_d.items(), key=lambda x: x[1])

