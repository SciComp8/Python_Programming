import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

file_path = ['../raw/sale_data/economics_train.csv', '../raw/sale_data/economics_test.csv']
X = pd.read_csv(file_path[0], index_col='Id')
X_test = pd.read_csv(file_path[1], index_col='Id')
X.drop(axis=0, subset=['GDP'], inplace=True)
y = X.GDP

X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.7, test_size=0.3, random_state=9)

num_var = [num_name for num_name in X_train.columns if X_train[num_name].dtype in ['int64', 'float64']]
cat_var = [cat_name for cat_name in X_train.columns if X_train[cat_name].nunique() <= 15 and X_train[cat_name].dtype == "object"]
feature = cat_var + num_var

X_train_select = X_train[feature].copy()
X_valid_select = X_valid[feature].copy()
X_test_select = X_test[feature].copy()
X_train_select.head()

num_transformer = SimpleImputer(strategy='constant', fill_value=0)
cat_transformer = Pipeline(steps=[
    ('impute', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse=False))
])
# handle_unknown='ignore': prevent errors when the validation set contains classes absent from the training data.
# When an unknown category is encountered during transform, the resulting one-hot encoded columns for this feature will be all zeros. 
# sparse=False: guarantees that the encoded columns are output as a dense NumPy array rather than as a sparse matrix

preprocessor = ColumnTransformer(
    transformers=[
        ('num', num_transformer, num_var),
        ('cat', cat_transformer, cat_var)
    ])

rfg = RandomForestRegressor(n_estimators=150, random_state=9)

model_pip = Pipeline(steps=[('preprocessor', preprocessor), ('model', rfg)])

model_pip.fit(X_train, y_train)

preds = model_pip.predict(X_valid)

print('The mean absolute error is:', mean_absolute_error(y_valid, preds))
