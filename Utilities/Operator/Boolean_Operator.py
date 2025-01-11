# Boolean variables can either be True or False
# Boolean examples in Kaggle: https://github.com/SciComp8/Python_Programming/blob/main/Kaggle/Learn_Python/Booleans_Conditionals.py
# Operator precedence: https://docs.python.org/3/reference/expressions.html#operator-precedence


out_of_donut = True
if out_of_donut:
    print("Please run to the supermarket NOW!")

# Truthy values: non 0; non-empty string; non-empty list; non-empty dictionary; non-empty tuple
# Falsey valuees: 0; ""; []; {}; (); None

donut_list = []
# Check the truthiness of donut_list
print(bool(donut_list))
# False

# The highest precedence belongs to (), followed by not, and, and or.
# ==
# is True | is False
# !=
# < 
# <=
# >
# >=

donut_qty == 10

# Be careful with equality comparisons of floats
x = 0.1 + 1.1
x == 2.1
# False
print(x)
# 1.2000000000000002
