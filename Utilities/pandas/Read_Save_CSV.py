# Reference
# https://towardsdatascience.com/its-time-to-say-goodbye-to-pd-read-csv-and-pd-to-csv-27fbc74e84c5/
# For datasets with fewer than 1 million rows, Pandas and Dask exhibited similar performance in reading CSV files.
# As the dataset size increased beyond 1 million rows, Dask's performance declined, taking significantly more time than Pandas to read the CSV files.
# DataTable consistently outperformed both, reading CSV files 4 to 5 times faster than Pandas, making it the most efficient among the three for this task.

# Dask was slower than Pandas in writing dataframes to CSV files across all dataset sizes.
# DataTable again demonstrated superior performance, writing to CSV files faster than both Pandas and Dask.
