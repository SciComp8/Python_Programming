# Topic: arguments
# Default arguments must follow non-default argument; calculate_power(pow_val=2, number) is incorrect
# *args must precede **kwargs
def calculate_power(number, pow_val=2):
    """Raise number to the power of pow_val."""
    new_value = number ** pow_val
    return new_value

calculate_power(2, 3) # 8
calculate_power(2, 2) # 4
calculate_power(2) # 4

# *Flexible* arguments: not sure the exact number of positional arguments a user wants to pass to the function
def add_all(*args):
    """Sum all values in *args together."""
    # Initialize sum
    sum_all = 0
    # Accumulate the sum
    for num in args:
        sum_all += num
    return sum_all

print(add_all(9))
print(add_all(9, 10, 11, 29))
# add_all() takes all the input parametersand packs them into a single immutable iterable object named args, which is a tuple. 
# Notice that we can choose any name we like, not limited to args.

def add_all(*elements):
    """Sum all values in *elements together."""
    print(type(elements))
    sum_all = 0
    for num in elements:
        sum_all += num
    return sum_all

print(add_all(9, 10, 11, 29))
# <class 'tuple'>
# 59

# Flexible arguments: pass an arbitrary number of keyword/named arguments
def print_all(**kwargs):
    """Print out key-value pairs in **kwargs."""
    # Print out the key-value pairs
    for key, value in kwargs.items():
        print(key + ':  ' + value)

print_all(name='cysteine', location='nails, skin, hair', function='make collagen')
# name:  cysteine
# location:  nails, skin, hair
# function:  make collagen

def print_all(**elements):
    """Print out key-value pairs in **elements."""
    print(type(elements))
    for key, value in elements.items():
        print(key + ':  ' + value)

print_all(name='cysteine', location='nails, skin, hair', function='make collagen')
# <class 'dict'>
# name:  cysteine
# location:  nails, skin, hair
# function:  make collagen

# print_all() takes all the input key-value parameters and packs them into a single mutable iterable object named elements, which is a dictionary. 
