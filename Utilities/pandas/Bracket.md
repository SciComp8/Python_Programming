When we use `X_cat_train_full[col]`, we get a Series corresponding to that column.

when we use `X_cat_train_full[[col]]`, we get a DataFrame with just that single column.

A DataFrame allows us to maintain the structure (e.g., number of columns) for consistency with other DataFrame operations, while a Series might behave differently in certain operations.
