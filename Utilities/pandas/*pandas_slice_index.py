# Topic: slice and index DataFrames
 
"""Prepare a sample dataset"""
import pandas as pd
import numpy as np
num_rows = 10000
num_columns = 20
data = np.random.rand(num_rows, num_columns)
column_names = [f"Column_{i+1}" for i in range(num_columns)]
df = pd.DataFrame(data, columns=column_names)
print(df.head())

"""Show the explicit column and row indices"""
df.columns
# Index(['Column_1', 'Column_2', 'Column_3', 'Column_4', 'Column_5', 'Column_6',
#        'Column_7', 'Column_8', 'Column_9', 'Column_10', 'Column_11',
#        'Column_12', 'Column_13', 'Column_14', 'Column_15', 'Column_16',
#        'Column_17', 'Column_18', 'Column_19', 'Column_20'],
#       dtype='object')
df.index
# RangeIndex(start=0, stop=10000, step=1)

"""Set up the index"""
# Set a column as the row index
df.set_index("column_name_1") # Index values in this column can be repetitive 
# Reset the row index as default
df.reset_index()
# Reset the row index as default and drop the previous index such that the previous index will not appear as a column
df.reset_index(drop=True)

"""
Locate rows using the index name locator "loc" versus the index number locator "iloc"
"""
# When the selected row numbers are small, use iloc, otherwise, use loc
# Select the first 100 rows
import time
start_time = time.time()
df.loc[range(0, 100)]
end_time = time.time()
print(end_time - start_time) # 0.019807100296020508

start_time = time.time()
df.iloc[range(0, 100)]
end_time = time.time()
print(end_time - start_time) # 0.013633012771606445

# Select the first 500 rows
start_time = time.time()
df.loc[range(0, 500)]
end_time = time.time()
print(end_time - start_time) # 0.020083904266357422 seconds

start_time = time.time()
df.iloc[range(0, 500)]
end_time = time.time()
print(end_time - start_time) # 0.019440889358520508 seconds

# Select the first 5000 rows
start_time = time.time()
df.loc[range(0, 5000)]
end_time = time.time()
print(end_time - start_time) # 0.015697956085205078 seconds

start_time = time.time()
df.iloc[range(0, 5000)]
end_time = time.time()
print(end_time - start_time) # 0.01716899871826172

"""
Randomly select rows
"""
# Reference: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sample.html
# DataFrame.sample(n=None, frac=None, replace=False, weights=None, random_state=None, axis=None, ignore_index=False)
df.sample(int(0.8 * df.shape[0]), axis=0, replace = True)

"""
Select rows based on value(s) of one/multiple columns
"""
df["column_name_1"] > 50 # subset rows and return a logical column
df[df["column_name_1"] > 50] # subset rows and return a subsetted data frame
df[df["column_name_1"]  == "labrador"] # subset rows and return a subsetted data frame
df[df["column_name_1"]  < "2017-09-09"] # subset rows and return a subsetted data frame
is_lab = df["column_name_1"]  == "labrador"
is_lab2 = df["column_name_1"]  == "labrador2"
df[is_lab & is_lab2] # subset rows based on multiple conditions
df[(df["column_name_1"]  == "labrador") & (df["column_name_1"]  == "labrador2")] # One-line expression
is_lab_or_lab2 = df["column_name_1"].isin(["labrador", "labrador"])
df[is_lab_or_lab2] # subset rows based on multiple values of a categorical variable

"""
Select rows based on value(s) of one/multiple columns using the index name locator - loc
"""
# Subset the rows based on the particular values of a column
# Approach 1: a cumbersome way to select eligible rows
df[df["column_name_1"].isin(["value_1", "value_2"])] 

# Approach 2: we first build the column index; and then filter on index values
# Set the variable to be filtered as the index
df.set_index("column_name") 
# We then use loc to filter on index values, here we select rows that meet 2 values; 
# Notice that .loc[] makes our code less burdensome to maintain and easy for our collaborators to read 
df.loc[["value_1", "value_2"]] 
df.loc["value_1"]

# Set multi-level/hierarchical indices made out of multiple columns when one category is nested inside another category
df.set_index(["column_name_1", "column_name_2"]) # The index level of column_name_2 is nested inside of the index level of column_name_1
# Subset the outer index level with a list
df.loc[["value_1", "value_2"]]
# Subset the inner index level with a list of tuples
df.loc[[("val_1_for_col_1", "val_1_for_col_2"), ("val_2_for_col_1", "val_2_for_col_2")]]

# Make the sorting by index values
df.sort_index() # By default, this function sorts all index levels from outer to inner in ascending order
# Control the sorting level and order
df.sort_index(level=["col_name_1", "col_name_2"], ascending=[True,False])
df.sort_index(level="col_name_1")

# Sort the row index before slicing; notice that we can only slice an index if the index is sorted
df.set_index(["col_name_1", "col_name_2"]).sort_index()
df.loc["val_1":"val_3"] # Subset the outer index level that meet val_1, val_2, val_3; notice that the initial and final values are both included, compared to slicing a list
# Special slicing feature for dates
df.loc["2020-01-27":"2022-03-09"]
df.loc["2020":"2022"]
# Conventional way to subset rows that meet date values
df[(df["date"] >= "2010-09-02") & (df["date"] <= "2012-09-02")]

df.loc[("val_1_for_col_1", "val_1_for_col_2"):("val_3_for_col_1", "val_3_for_col_2")] # Subset the outer index level that meet val_1_for_col_1, val_2_for_col_1, val_3_for_col_1, and then subset the inner index level that meet val_1_for_col_2, val_2_for_col_2, val_3_for_col_2

"""
Select columns
"""
target_features = ['col_name_1', 'col_name_2', 'col_name_3']; X_train = train_data[target_features]
cat_features_selected = [col for col in X_train.columns if X_train[col].dtype == 'object']
num_features_selected = [col for col in X_train.columns if X_train[col].dtype in ['int64', 'float64']]
y_train = X_train.outcome

"""
Select columns using the index name locator "loc" versus the index number locator "iloc
"""
# The speeds across loc, iloc, and [[]] are similar; may choose [[]] for convenient typing

df.loc[:, "col_name_1":"col_name_3"] # Select columns beginning from col_name_1 to col_name_3, and keep all rows

sig_feature = sig_connectome + sig_meta
df = df.loc[:, sig_feature]

import time
start_time = time.time()
df.loc[:, "Column_1":"Column_3"]
end_time = time.time()
print(end_time - start_time) # 0.010194063186645508 seconds

start_time = time.time()
df.iloc[:, :3] # Select the first 3 columns
end_time = time.time()
print(end_time - start_time) # 0.00931406021118164 seconds

start_time = time.time()
df[["Column_1", "Column_2", "Column_3"]]
end_time = time.time()
print(end_time - start_time) # 0.009947061538696289 seconds

df.iloc[:,[0,2,5,9]] # Select the first, third, sixth, and tenth columns
df.iloc[:, 1:-1] # Select all the columns except the first and last
df.iloc[:, -1] # Select the last column

"""
Randomly select columns
"""
# Reference: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sample.html
# DataFrame.sample(n=None, frac=None, replace=False, weights=None, random_state=None, axis=None, ignore_index=False)
df.sample(int(0.8 * df.shape[1]), axis=1, replace=False)


"""
! Slice rows and columns at the same time
"""
df.loc[("val_1_for_col_1", "val_1_for_col_2", "val_1_for_col_3"):("val_3_for_col_1", "val_3_for_col_2", "val_3_for_col_3"), "col_name_1":"col_name_3"] 

df.loc[df.var_name == 'value']['col_name']
# Select columns based on the value of another column
test_data.loc[test_data.UMR == 'Yes']['Outcome']

# Slicing and subsetting using iloc method, similar to slicing lists
# Slice lists
list_1[1:6] # Select the 2nd to 5th items in a list
list_1[:6] # Select from the beginning to the 5th item in a list
list_1[:] # Return the whole list

# Subset the DataFrame by row and column numbers
df.iloc[2] # Select the 2nd row
df.iloc[1:6, 1:6] # Select the 2nd to 5th rows and the 2nd to 5th columns

# Calculate the summary statistics across rows [per column as a group]
df_pivot_table.mean(axis="index")
# Filter for the group that has the largest mean value
mean_by_group=df_pivot_table.mean(axis="index")
mean_by_group[mean_by_group == max(mean_by_group)]

# Calculate the summary statistics across columns [per row as a group]; pivot table has columns with the same data type
df_pivot_table.mean(axis="columns")

# Access components of a date (year, month, day)
df["date_column"].dt.year
df["date_column"].dt.month
df["date_column"].dt.day
