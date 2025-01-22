pd.read_csv()
file_name = 'CONNECTOME_MATRICES.csv'
con_mat = pd.read_csv(file_path + file_name)
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
