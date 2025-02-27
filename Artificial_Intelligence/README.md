
# Useful AI computing procedures

## Environment setup
- [What files are contained in training and test folders?](https://github.com/SciComp8/Python_Programming/blob/main/Utilities/Generator.py#L122)
- [Create symbolic links to access the file from another location without duplicating it](https://github.com/SciComp8/Python_Programming/blob/main/Utilities/File/Create_SymbolicLink.py)

## Dataframe manipulation
- [Read data](https://github.com/SciComp8/Python_Programming/blob/main/Utilities/pandas/Read_Data.py)
- [Deep copy features](https://github.com/SciComp8/Python_Programming/blob/main/Artificial_Intelligence/Machine_Learning/Decision_Tree_Price.py#L25)
- [Slice and index a dataframe](https://github.com/SciComp8/Python_Programming/blob/main/Utilities/pandas/*pandas_slice_index.py#L173)
  - [Select target columns](https://github.com/SciComp8/Python_Programming/blob/main/Utilities/pandas/*pandas_slice_index.py#L130)
  - [Randomly select columns](https://github.com/ScienceComputing/Python_Programming/blob/main/Utilities/pandas/*pandas_slice_index.py#L165)
- Split data into training and validation sets before any fitting of preprocessing steps to avoid [train-test contamination](https://github.com/SciComp8/Python_Programming/blob/main/Artificial_Intelligence/Machine_Learning/Train_Test_Contamination.md)
  - [Use `train_test_split`](https://github.com/SciComp8/Python_Programming/blob/main/Artificial_Intelligence/Machine_Learning/Decision_Tree_Price.py#L33)
  - [Randomly select rows](https://github.com/ScienceComputing/Python_Programming/blob/main/Utilities/pandas/*pandas_slice_index.py#L70)

## Data exploration
- [Explore data with summary statistics](https://github.com/SciComp8/Python_Programming/blob/main/Utilities/pandas/*pandas_summary_statistics.py)


## Feature engineering
- [Manage missing values](https://github.com/SciComp8/Python_Programming/blob/main/Artificial_Intelligence/Machine_Learning/Manage_Missingness.py#L114)
  - [Impute missing values](https://github.com/SciComp8/Python_Programming/blob/main/Artificial_Intelligence/Machine_Learning/Manage_Missingness.py#L61)
  - [Drop missing values](https://github.com/SciComp8/Python_Programming/blob/main/Artificial_Intelligence/Machine_Learning/Manage_Missingness.py)
- Encode categorical variables
  - [Which variables are categorical?](https://github.com/SciComp8/Python_Programming/blob/main/Artificial_Intelligence/Machine_Learning/List_Categorical_Variable.py)
  - [Ordinal encoding](https://github.com/SciComp8/Python_Programming/blob/main/Artificial_Intelligence/Machine_Learning/Ordinal_Encoding.py)
  - [One-hot encoding](https://github.com/SciComp8/Python_Programming/blob/main/Artificial_Intelligence/Machine_Learning/One_Hot_Encoding.py#L65)
  - *Should the year be encoded as the original integer or using one-hot encoding?* It depends. If the year has a meaningful numeric relationship with the target (e.g., older years might correlate with higher frequency of a disease), keep it as an integer. However, if specific years have unique relationships with the target, the year is better treated using one-hot encoding.
- [Normalize a feature](https://github.com/ScienceComputing/Python_Programming/blob/main/Utilities/pandas/*pandas_summary_statistics.py)

## Build a model: define -- fit -- predict -- evaluate
- [Train a decision tree regressor](https://github.com/SciComp8/Python_Programming/blob/main/Artificial_Intelligence/Machine_Learning/Decision_Tree_Price.py)
- [Train a decision tree classifier](https://github.com/SciComp8/Python_Programming/blob/main/Artificial_Intelligence/Machine_Learning/Decision_Tree_Mortality.ipynb)
- [Train a random forest regressor](https://github.com/SciComp8/Python_Programming/blob/main/Artificial_Intelligence/Machine_Learning/Random_Forest_Price.py)
- [Train a gradient boosting regressor](https://github.com/SciComp8/Python_Programming/blob/main/Artificial_Intelligence/Machine_Learning/XGBoost.py)

## Make a pipeline that bundles imputation, one-hot encoding, model training, and model evaluation
- [Pipeline](https://github.com/SciComp8/Python_Programming/blob/main/Artificial_Intelligence/Machine_Learning/Pipeline.py)
  
## Fine-tune a model for better performance
- [Evaluate the impact of different arguments on model performance](https://github.com/SciComp8/Python_Programming/blob/main/Artificial_Intelligence/Machine_Learning/Evaluate_Argument_Impact.py)
- [Use cross-validation (CV) to evaluate the impact of different arguments on model performance](https://github.com/SciComp8/Python_Programming/blob/main/Artificial_Intelligence/Machine_Learning/Cross_Validation.py); CV is suitable for small datasets, as computational burden isn't a big issue
- [Define several models with varied arguments and select the model with the best performance](https://github.com/SciComp8/Python_Programming/blob/main/Artificial_Intelligence/Machine_Learning/Random_Forest_Price_V2.py)
- Add more relevant features
- Use another state-of-the-art model algorithm
