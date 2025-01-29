# Reference: https://www.youtube.com/watch?v=2_iKR_fDKNM | NISS AI, Statistics & Data Science in Practice: Lucas Mentch - Random Forests
# mtry defines the number of variables randomly sampled as candidates at each split
# From the standpoint of model complexity, this parameter in random forests functions similarly to the shrinkage penalty used in explicit regularization methods such as the lasso.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
