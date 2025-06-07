

| Parameter | Starting Value | Common Range | How to Tune in Overfitting/Underfitting Situations
|----------|----------|----------|----------|
|Learning rate: `eta` | 0.1 | Reduce it to 10% of its value 10 steps: [10^(-1), 10^(-11)] | Decrease/increase | 
|Maximum depth of trees: `max_depth` | 3 | Increase it until the model performance stops improving: [3, ∞] | Decrease/increase | 
|Fraction of observations used for each tree: `subsample` | 0.8 | Reduce it to 0.5 to prevent overfitting: [0.5, 0.8] | Decrease/increase |


## More reading
https://xgboost.readthedocs.io/en/stable/python/python_api.html#module-xgboost.sklearn
