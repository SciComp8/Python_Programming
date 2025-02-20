When we assign a Series to a DataFrame column like the following, pandas aligns the data based on the index. 

```Python}
df_2['Outcome'] = df_1['Outcome']
```

If the indexes in both df_1 and df_2 are identical (or at least overlap as you expect), the values from df_1['Outcome'] will be correctly aligned with the corresponding rows in df_2.

If the indexes don't match, pandas will attempt to align them. Rows in df_2 that don't have a corresponding index in df_1 will receive NaN for the Outcome column.
