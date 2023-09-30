# We have the option to create custom Python functions by employing the 'def' keyword, incorporating function headers, docstrings, and defining function bodies. 
# Nonetheless, there exists a faster method for crafting functions spontaneously, referred to as lambda functions, as they make use of the 'lambda' keyword.

# lambda argument(s) : expression 
# Case 1:
lambda : print('Hello Anonymous Function!')
greet = lambda : print('Hello Anonymous Function!')
greet()

# Case 2:
greet_stock = lambda stock_name: print('Welcome to the world of', stock_name, 'stocks!')
greet_stock('GOOGL')

# Case 3:
raise_to_power = lambda m, n: m ** n
raise_to_power(8, 8)

# Case 4:
def neg_log_likelyhood(X, Y, theta):
    loss_function = np.sum(np.exp(theta * X) - (Y * theta * X) + np.log(factorial_Y))
    return loss_function
def backtracking_line_search(L, theta, direction, step=0.5, rho=0.8):
    while L(theta + step * direction) > L(x):
        step *= rho
    return step
t = backtracking_line_search(
        L=lambda theta: neg_log_likelyhood(X=X_data, Y=Y_data, theta=theta), #!
        theta=theta_estimate,
        direction=-gradient)


# Integrate lambda with map
# The map function accepts two parameters: a function and a sequence, e.g., a list, and then proceeds to apply the specified function to each element within the given sequence.
num_list = [6, 8, 15, 0, 90, 50]
cubic_all = map(lambda num: num ** 3, num_list)
print(cubic_all)
print(list(cubic_all))

# Bioinformatics scenarior: calculate the average expression level of a specific gene across all spatial locations. 
gene_data = [
    {'gene_name': 'GeneA', 'location1': 10, 'location2': 15, 'location3': 8},
    {'gene_name': 'GeneB', 'location1': 5, 'location2': 12, 'location3': 7},
    {'gene_name': 'GeneC', 'location1': 8, 'location2': 9, 'location3': 10},
]

# Define a lambda function to calculate the average expression of a gene
calculate_average_expression = lambda gene_data_point: (
    gene_data_point['location1'] + gene_data_point['location2'] + gene_data_point['location3']
) / 3

# Calculate the average expression of 'GeneA' using the lambda function
gene_name_to_calculate = 'GeneA'
average_expression = list(map(
    calculate_average_expression, 
    list(filter(lambda data_point: data_point['gene_name'] == gene_name_to_calculate, gene_data))
))
