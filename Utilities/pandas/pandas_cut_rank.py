# References: 
# https://pandas.pydata.org/docs/reference/api/pandas.cut.html
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rank.html

import pandas as pd
# Stratify the target variable (y_train) by dividing it into 10 equal-sized bins based on its ranked values. 
y_train_stratified = pd.cut(y_train.rank(method='first'), bins=10, labels=False)

# Ranking resolves ties by order of appearance.
# Binning (pd.cut) converts ranks into discrete strata for balanced sampling.
