
Reference: https://xgboost.readthedocs.io/en/stable/python/python_api.html#module-xgboost.sklearn

| Parameter | Starting Value | Common Range | How to Tune in Overfitting/Underfitting Situations
|----------|----------|----------|----------|
|Learning rate: `eta` | 0.1 | Reduce it to 10% of its value every 10 rounds | Decrease/increase | 
|Maximum depth of trees: `max_depth ` | 3 | Increase it until the model performance stops improving | Decrease/increase | 
|Fraction of observations used for each tree: `subsample` | 0.8 | Reduce it to 0.5 to prevent overfitting | Decrease/increase | 
