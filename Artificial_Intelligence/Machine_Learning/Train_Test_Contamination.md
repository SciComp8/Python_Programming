

Imagine we fit a preprocessor—say, an imputer for missing values—**before** splitting our data using `train_test_split()`. 

Our model might score impressively during validation, yet underperform in real-world deployment.

**This happens because we've inadvertently allowed the model to incorporate the validation data during training**. 

Consequently, it may overfit to the characteristics of that specific dataset, failing to generalize to new data. 

The risk amplifies when employing complex feature engineering.

To prevent this, always ensure that any fitting—whether for preprocessing or model training—is restricted solely to the training set. 

Using scikit-learn pipelines can simplify this process, and it's especially vital to incorporate preprocessing within the pipeline when performing cross-validation.

References: 
- https://github.com/SciComp8/Python_Programming/blob/main/Artificial_Intelligence/Machine_Learning/Cross_Validation.py
