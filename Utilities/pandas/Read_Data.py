# References:
# https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
# https://medium.com/data-science/its-time-to-say-goodbye-to-pd-read-csv-and-pd-to-csv-27fbc74e84c5
pd.read_csv()
file_name = 'CONNECTOME_MATRICES.csv'
con_mat = pd.read_csv(file_path + file_name, index_col='Id')
con_mat_2 = pd.read_csv(file_path + file_name, index_col='Id', true_values = ['yes'], false_values = ['no'])
# 'yes' is considered as True, 'no is considered as False'
con_mat.head()

pd.read_excel()
file_path = '/Users/xyz/data/'
file_name = 'METADATA.xlsx'
df_meta = pd.read_excel(file_path + file_name, sheet_name='combined')
df_meta.head()

pd.read_json()
pd.read_clipboard()

# Get a glimpse of 20 values randomly selected in a column named disease
df.disease.sample(n=20)

# Get a glimpse of 20 values randomly selected of the disease column that are not 'Norovirus'
df[df.disease != 'Norovirus'].disease.sample(n=20)
