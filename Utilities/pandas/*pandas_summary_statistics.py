# Compute built-in summary statistics
# Check data with these statistics is important in a data science project. 
# We may spot something in the dataset that needs further inspection.
print("Number of rows in the dataset:", df.shape[0])
print("Number of columns in the dataset:", df.shape[1])
df.head()
df.describe()
df.info()

# Estimate the mean
df["column_name_1"].mean()
df.var_1.mean() # Pull out a variable using dot-notation
df.var_1.mean().round() # :)
df[df["column_name_1"] == "group1"]["column_name_2"].mean() # Calculate the mean of a variable (column_name_2) by the specific group (group1)
df[df.var_1 == 'value']['var_2'].mean() # :)

df["column_name_1"].median()
df["column_name_1"].mode()
print('The most frequent category is:', df['column_name_1'].mode().values, '\n')
df["column_name_1"].min()
df["column_name_1"].max()
df["column_name_1"].var()
df["column_name_1"].std()
df["column_name_1"].sum()
df["column_name_1"].quantile()

# Example: find the oldest and youngest birth date
df["birthdate"].min()
df["birthdate"].max()

# Compute custom summary statistics
def pct90(column):
    return column.quantile(90)

def pct70(column):
    return column.quantile(70)

df["column_name_1"].agg(pct90)
df[["column_name_1", "column_name_2"]].agg(pct90)
df["column_name_1"].agg([pct90, pct70])

# Build a custom IQR function and mix it with np.median
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
    
df["column_name_1"].agg(iqr)

import numpy as np
print(df[["column_name_1", "column_name_2", "column_name_3"]].agg([iqr, np.median]))

# Compute cumulative statistics - return an entire column, not a single number
df["column_name_1"].cumsum()
df["column_name_1"].cummax()
df["column_name_1"].cummin()
df["column_name_1"].cumprod()

# Normalize the column(s) using z-score or min-max
z_fun = lambda x: (x - x.mean()) / x.std()
df["column_name_1"].transform(z_fun)
df[["column_name_1", "column_name_2", "column_name_3"]].transform(z_fun)
min_max_fun = lambda x: (x - x.min()) / (x.max() - x.min())
df["column_name_1"].transform(min_max_fun)
df[["column_name_1", "column_name_2", "column_name_3"]].transform(min_max_fun)

# Impute the missing values using median or mean
miss_median = lambda x: x.fillna(x.median())
df["column_name_1"].transform(miss_median)
miss_mean = lambda x: x.fillna(x.mean())
df["column_name_1"].transform(miss_mean)

# Drop rows with missing values
df_clean = df.dropna(axis=0, how='any')

# Drop columns with missing values
df_clean = df.dropna(axis=1)
# how='all': drops a column only if all values are missing

# Drop the records with the duplicate values on variables
df.drop_duplicates(subset=["column_name_1", "column_name_2"])

# Count the categorical variable
df["column_name_1"].value_counts() # Count the number of each categorical level
df["column_name_1"].value_counts(sort=True) # Sort the count
df["column_name_1"].value_counts(normalize=True) # Count the proportion of each categorical level

# Count the sample size of each group
df.groupby("group_column").count()

# Calculate one or multiple grouped summary statistics for one or multiple variables
df.groupby("group_column")["column_name_1"].mean()
df.groupby("group_column")["column_name_1"].agg([mean, max, sum])
df.groupby(["group_column_1", "group_column_2"])["column_name_1"].mean()
df.groupby(["group_column_1", "group_column_2"])[["column_name_1", "column_name_2"]].mean()

# Create the pivot table grouped by one/multiple variables
# A pivot table is a pandas DataFrame with the sorted index
df.pivot_table(values="column_name", index="group_column") # By default, pivot_table takes the mean value for each group
df.pivot_table(values="column_name", index=["group_column_1", "group_column_2") # By default, pivot_table takes the mean value for each group
# Make a pivot table of the avg_gdp_c column, with **country and city as rows**, and **year as columns**.
GDP_by_country_city_vs_year = gdp.pivot_table(values="avg_gdp_c", index=["country", "city"], columns="year")

# Create the pivot table for multiple summary statistics
import numpy as np
df.pivot_table(values="column_name", index="group_column", aggfunc=np.median)
df.pivot_table(values="column_name", index="group_column", aggfunc=[np.mean, np.median])

# Create the pivot tables grouped by multiple variables
df.pivot_table(values="column_name", index="group_column_1", columns="group_column_2") 
df.pivot_table(values="column_name", index="group_column_1", columns="group_column_2", fill_value=0) # Replace NaN with 0
# df.pivot_table(values="column_name", index="group_column_1", columns="group_column_2", fill_value=0, margins=True) # Return the mean of values per row/column


