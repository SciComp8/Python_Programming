df.head()

df.col_name.sample(n=6)

# Get a glimpse of the entries in the diagnosis_time column for different spellings of min (e.g., min, mins, minutes)
df.diagnosis_time[df.diagnosis_time.str.contains('min')].sample(n=20)

df.info() # this info method shows information on each of the columns, such as the data type and number of missing values
df = pd.read_csv('data/data_raw.csv')
df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 874 entries, 0 to 873
# Data columns (total 3 columns):
#  #   Column       Non-Null Count  Dtype 
# ---  ------       --------------  ----- 
#  0   name         874   non-null  object
#  1   author       874   non-null  object
#  2   time         874   non-null  object

# dtypes: object(3)
# memory usage: 1.3+ MB

df.describe() # descriptive statistics
# count: how many rows have non-missing values
# mean: average
# std, standard deviation: how values are numerically spread out
# 25%/50%/75%: the smallest number that is bigger than 25%/50%/75% of the values

df.shape # shape is an attribute, not a method; so there is no parenthesis 

df.values # values attribute extracts the data values in 2-D numpy array

df.columns # columns attribute extracts the column names

df.columns = new_column # assign new column names

df.index # index attribute extracts the row names/numbers

df.sort_values("column_name", ascending=False) # change the order of the rows by sorting on the particular column

df.sort_values(["column_name_1", "column_name_2"]) # sort on the first column then on the second column

df.sort_values(["column_name_1", "column_name_2"],  ascending=[True, False]) # sort on the first column by ascending order then on the second column by decreasing order

df["column_name_1"] # select one column

df[["column_name_1", "column_name_2"]] # select multiple columns

cols_to_select = ["column_name_1", "column_name_2"] # select multiple columns
df[cols_to_select]

df["column_name_1"] > 50 # subset rows and return a logical column

df[df["column_name_1"] > 50] # subset rows and return a subsetted data frame

df[df["column_name_1"]  == "labrador"] # subset rows and return a subsetted data frame

df[df["column_name_1"]  < "2017-09-09"] # subset rows and return a subsetted data frame

is_lab = df["column_name_1"]  == "labrador"
is_lab2 = df["column_name_1"]  == "labrador2"
df[is_lab & is_lab2] # subset rows based on multiple conditions

df[(df["column_name_1"]  == "labrador") & (df["column_name_1"]  == "labrador2")] 

is_lab_or_lab2 = df["column_name_1"].isin(["labrador", "labrador"])
df[is_lab_or_lab2] # subset rows based on multiple values of a categorical variable

df.drop(columns=['column_name'], axis=1, inplace=True) # drop a column
