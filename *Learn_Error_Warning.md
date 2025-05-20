# Major types of errors in Python programming
## Syntax errors, also known as parsing errors
These errors occur when Python cannot parse our code due to incorrect syntax. They are detected by the compiler or the interpreter.

### Concatenate 2 different types of objects
  ```python
  print('6 % 6 = ' + 6 % 6)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: can only concatenate str (not "int") to str
  ```

### Compare a number with a string
  ```python
  age = input('Please type your age: ')
  print('Are you older than 10?', age > 10)
  Traceback (most recent call last):
    File "<pyshell#42>", line 1, in <module>
      print('Are you older than 10?', age > 10)
  TypeError: '>' not supported between instances of 'str' and 'int'
  ```

### Misspelled keywords
  ```python
  Cell In[17], line 3
  return y
  ^
  SyntaxError: 'return' outside function
  ```

### Misspelled attribute name
  ```python
  df = sns.load_dataset("tips")
  df['day'].value_count()
  AttributeError: 'Series' object has no attribute 'value_count'.
  ```

### Name is not defined (e.g., wrong variable/function names)
  ```python
  a = 8
  print(AA)
  Traceback (most recent call last):
    File "<pyshell#37>", line 1, in <module>
    print(AA)
  NameError: name 'AA' is not defined. Did you mean: 'aa'?

  NameError                                 Traceback (most recent call last)
  Cell In[18], line 1
  ----> 1 devide_two(98.920)
  NameError: name 'devide_two' is not defined
  ```
### Wrong input
  ```python
  age = int(input('Please type your age: '))
  Sixteen
  Traceback (most recent call last):
    File "<pyshell#44>", line 1, in <module>
    age = int(input('Please type your age: '))
  ValueError: invalid literal for int() with base 10: 'Sixteen'

  age = input('Please type your age: ')
  try:
      age = int(age)
      print('How old will you be in 2 year?', age + 1)
  except ValueError:
      print('The given age is not valid')
  ```
### Setting extra parameters
  ```python
  TypeError                                 Traceback (most recent call last)
  Cell In[14], line 4
  2 y = 5
  3 # Which of the two variables above has the smallest absolute value?
  ----> 4 smallest_abs = min(abs(x, y))
  TypeError: abs() takes exactly one argument (2 given)
  ```
### Two starred expressions in assignment
  ```python
  *__, a, b, *_ = ['a', 'cde', 'bib', 6, 9, 10]
  File "<stdin>", line 1
  SyntaxError: two starred expressions in assignment
  ```
### Wrong use of an operator

### Forgetting parentheses in a function call

### Call the locally scoped function
  ```python
  def house():
    print("Gallary from house()")
    def first_house():
        print("Gallary from first_house()")
    def second_house():
        print("Gallary from second_house()")
    first_house()
    second_house()

  first_house()
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  NameError: name 'first_house' is not defined
  ```
### Not putting strings in single quotes or double quotes

## Runtime Errors
These errors occur when an operation is performed on incompatible data types (e.g., comparing an integer with a string).

### No compatible binary
  ```python
  DEBUG [main] Printing verbose output
  Traceback (most recent call last):
    File "/Users/your_name/.pyenv/versions/3.8.18/bin/kb", line 8, in <module>
      sys.exit(main())
    File "/Users/your_name/.pyenv/versions/3.8.18/lib/python3.8/site-packages/ngs_tools/logging.py", line 62, in inner
      return func(*args, **kwargs)
    File "/Users/your_name/.pyenv/versions/3.8.18/lib/python3.8/site-packages/kb_python/main.py", line 1583, in main
      raise UnsupportedOSError(
    kb_python.config.UnsupportedOSError: Failed to find compatible kallisto binary. Provide a compatible binary with the --kallisto option or    run kb compile."
  ```
### No compatible tensor shape
  ```python
  data_1 = torch.tensor([[1, 5, 6], [2, 6, 9]])
  data_2 = torch.tensor([[0, 1], [3, 3]])
  data_1 + data_2
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  RuntimeError: The size of tensor a (3) must match the size of tensor b (2) at non-singleton dimension 1
 ```

### XGBoost is performed on incompatible data types
  ```python
  params = {
              'objective':'binary:logistic',
              'max_depth': 5,
              'alpha': 10,
              'learning_rate': 0.1,
              'n_estimators': 100,
              'enable_categorical': True
          }
  
  xgb_model = XGBClassifier(**params)
  xgb_model.fit(X_train, y_train.loc[:, 'Outcome_1'])
  typeerror: '<' not supported between instances of 'int' and 'str'
  ```
- This error means that one or more of your target variables are a mix of data types (e.g., both integers and strings). 
- When the decision tree tries to compare values using the "<" operator to determine splits, it fails if it encounters an integer and a string together.

### XGBoost `NotFittedError`
  ```Python
  class XGBoostClassifierDMatrix(xgb.XGBClassifier, BaseEstimator, ClassifierMixin):
      """
      Wrapper for XGBoost classifier to accept DMatrix in fit.
      """
      def __init__(self, use_dmatrix=True, **kwargs):
          super().__init__(**kwargs)
          self.use_dmatrix = use_dmatrix  # Control DMatrix usage
  
      def fit(self, X, y=None, sample_weight=None, eval_set=None, **kwargs):
          if self.use_dmatrix:
              self.is_fitted_ = True  # Set fitted here for DMatrix
              if isinstance(X, xgb.DMatrix):
                  self.xgb_dm = X
                  super().fit(X, y, sample_weight=sample_weight, eval_set=eval_set, **kwargs)
              else:
                  self.xgb_dm = xgb.DMatrix(X, label=y)
                  super().fit(self.xgb_dm, y, sample_weight=sample_weight, eval_set=eval_set, **kwargs)
          else:
              super().fit(X, y, sample_weight=sample_weight, eval_set=eval_set, **kwargs)
          return self
  
      def predict(self, X, output_margin=False, iteration_range=(0, 0),
                  predict_type='auto', missing=np.nan, validate_features=True):
          check_is_fitted(self, 'is_fitted_')
          if self.use_dmatrix:
              if isinstance(X, xgb.DMatrix):
                  return super().predict(X, output_margin=output_margin, iteration_range=iteration_range,
                                         predict_type=predict_type, missing=missing, validate_features=validate_features)
              else:
                  return super().predict(xgb.DMatrix(X), output_margin=output_margin, iteration_range=iteration_range,
                                         predict_type=predict_type, missing=missing, validate_features=validate_features)
          else:
               return super().predict(X, output_margin=output_margin, iteration_range=iteration_range,
                                         predict_type=predict_type, missing=missing, validate_features=validate_features)
  
      def fit_predict(self, X, y=None, sample_weight=None, eval_set=None, **fit_params):
          """Fit to training data, then predict on X."""
          if self.use_dmatrix:
              if isinstance(X, xgb.DMatrix):
                  self.xgb_dm = X
                  self.fit(X, y, sample_weight=sample_weight, eval_set=eval_set, **fit_params)
                  return self.predict(X)
              else:
                  self.xgb_dm = xgb.DMatrix(X, label=y)
                  self.fit(self.xgb_dm, y, sample_weight=sample_weight, eval_set=eval_set, **fit_params)
                  return self.predict(X)
          else:
              self.fit(X, y, sample_weight=sample_weight, eval_set=eval_set, **fit_params)
              return self.predict(X)
  
  
  def optimized_grid_search_xgb_gpu(X_train, y_train):
      """
      Optimizes XGBoost SingleOutputClassifier GridSearchCV for GPU (CUDA) without separate test data.
  
      Args:
          X_train: Training features.
          y_train: Training target.
  
      Returns:
          The best fitted GridSearchCV object.
      """
  
      param_grid = {
          'learning_rate': [0.1],
          'max_depth': [3],
          'colsample_bytree': [0.8],
          'subsample': [0.8],
          'reg_lambda': [1],
          'reg_alpha': [0],
          'n_estimators': [100],
      }
  
      # Convert to numpy arrays
      X_train_np = np.array(X_train)
      y_train_np = np.array(y_train)
  
  
      def create_model():
          xgb_clf = XGBoostClassifierDMatrix(  # Use the wrapper
              device='cuda',  # Set device here
              enable_categorical=True,
              use_dmatrix=False
          )
          return xgb_clf
  
      # Wrap model creation and GridSearchCV in a function
      def train_model():
          xgb_clf = create_model()
          grid_search_clf = GridSearchCV(xgb_clf, param_grid, cv=5, scoring='accuracy', verbose=1)
          grid_search_clf.fit(X_train_np, y_train_np) # Pass numpy arrays to gridsearch
          return grid_search_clf
  
      grid_search_xgb = train_model()
      best_model = grid_search_xgb.best_estimator_
  
      print(f"Best parameters: {grid_search_xgb.best_params_}")
  
      return grid_search_xgb" ![image](https://github.com/user-attachments/assets/36bb487d-73c7-4254-8061-576bbfaa1ac5)

  NotFittedError: This XGBoostClassifierDMatrix instance is not fitted yet. Call 'fit' with appropriate arguments before using this   estimator.

  ```
- The XGBClassifier base class has its own fitted state, but the wrapper `XGBoostClassifierDMatrix` introduces a separate `is_fitted_` flag, leading to mismatches.
- Since we set `use_dmatrix=False` in `optimized_grid_search_xgb_gpu()`, the `is_fitted_ flag` in `predict()` is never set, causing `check_is_fitted()` to fail in `predict()`.

## Logical Errors


# More reading
- https://docs.python.org/3/tutorial/errors.html

# Handle errors
## Method 1: `try-except-else` or `try-except`
### Case 1:
  ```python
  def cubic(number): 
      """Returns the cubic of a number."""
      try: 
          return number ** 3
      except:
          print("The number you've input must be an int or float.")
          
  cubic('hello')
  ```
### Case 1.1:
  ```python
  def cubic(number): 
      """Returns the cubic of a number."""
      try: 
          return number ** 3
      except TypeError: # Allow other errors except TypeError pass through
          print("The number you've input must be an int or float.")
          
  cubic('hello')
  ```
    
### Case 2:
  ```python
  nums = [1, 2, "A"]
  sum_nums = 0
  for item in nums:
      try:
          float_num = float(item)
      except (ValueError, TypeError) as e:
          print(f"This is a non-numeric item: {item}")
      else:
          sum_nums += float_num 
          print(f"{sum_nums=}")
  ```
### Case 3: bioinformatics scenarior: load the BAM file and print reads in a specific region
  ```python
  import pysam
  try:
      bam_file = pysam.AlignmentFile("alignment.bam", "rb")
  except FileNotFoundError:
      print("Error: The BAM file 'alignment.bam' was not found.")
  except (IOError, ValueError) as e:
      print(f"Error: An error occurred while reading the BAM file: {e}")
  else:
      for read in bam_file.fetch('chr8', 100, 120):
          print(read)
          
      bam_file.close()
  ```

## Method 2: `raise:`
  ```python
  def sqrt(number): 
      """Returns the square root of a number."""
      if number < 0:
          raise ValueError("The number you've input must be non-negative.")
      try: 
          return number ** 0.5
      except TypeError:
          print("The number you've input must be an int or float.")
          
  sqrt('hello')
  sqrt(-8)
  ```

# Warning
 ```python
/usr/local/lib/python3.11/dist-packages/xgboost/core.py:160: UserWarning: [15:39:53] WARNING: /workspace/src/learner.cc:742: 
Parameters: { "estimator__alpha", "estimator__colsample_bytree", "estimator__lambda", "estimator__learning_rate", "estimator__max_depth", "estimator__n_estimators", "estimator__subsample", "use_dmatrix" } are not used.
 ```
The warning message occurs as the parameters we are passing to XGBoostClassifierDMatrix through the param_grid in GridSearchCV are not being properly forwarded to the underlying XGBoost classifier. 

