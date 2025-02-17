# Topic: visualize our data
# Histogram - reveal the distribution of a numerical variable
# https://matplotlib.org/stable/gallery/statistics/hist.html#sphx-glr-gallery-statistics-hist-py
import matplotlib.pyplot as plt
df.head() # Take a look at the first rows of the data frame
df["numerical_var"].hist(bins=20) # Larger bins get higher numbers of bars
plt.show()

# Plot histograms for multiple variables
df[["numerical_var_1", "numerical_var_2"]].hist()
plt.show()

# Bar plot - reveal the relationship between a categorical variable and a numerical variable
df.head() # Take a look at the first rows of the data frame
avg_var_by_group = df.groupby("group")["var"].mean()
avg_var_by_group.plot(kind="bar", title="Mean Variable by Group")
plt.show()

# Line plot - reveal changes in a numerical variable over time 
df.head() # Take a look at the first rows of the data frame
df.plot(x="date", y="var", kind="line", rot=45) # Rotate the x-axis labels for easier reading
plt.show()
# Interpret the plot: the number of XXX spikes around the same time each year

# Scatter plot - reveal the relationship between 2 numerical variables
df.head() # Take a look at the first rows of the data frame
df.plot(x="var_1", y="var_2", kind="scatter", title="Var 1 vs. Var 2")
plt.show()

# Layer multiple plots
df.head() # Take a look at the first rows of the data frame
df[df["group"]=="val_1"]["var"].hist(alpha=0.7, bins=20) # Increase the color transparency
df[df["group"]=="val_2"]["var"].hist(alpha=0.7, bins=20)
plt.legend(["val_1", "val_2"])
plt.show()
