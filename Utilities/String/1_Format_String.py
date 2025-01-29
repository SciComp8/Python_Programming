# Reference: https://docs.python.org/3/library/stdtypes.html#str.format
# Format the title in a graph; show the message or error; pass the statement into a function

# Positional formatting: 'text{}'.format(value)
# The format method replaces the placeholders using the values.
print('{} helps prevent side effects due to drug reactions and toxic chemicals'.format('Cysteine'))
# Cysteine helps prevent side effects due to drug reactions and toxic chemicals

str1 = '{} helps prevent side effects due to drug reactions and toxic chemicals'
amino_acid = 'Cysteine'
str1.format(amino_acid)
# 'Cysteine helps prevent side effects due to drug reactions and toxic chemicals'

# Reorder the placeholder
str2 = '{1} helps {0} side effects due to drug reactions and toxic chemicals'
amino_acid = 'Cysteine'
function = 'prevent'
str2.format(function, amino_acid)
# 'Cysteine helps prevent side effects due to drug reactions and toxic chemicals'

# Specify the name for the placeholder
str3 = '{amino_acid} helps {function} side effects due to drug reactions and toxic chemicals'
str3.format(amino_acid=amino_acid, function=function)
# 'Cysteine helps prevent side effects due to drug reactions and toxic chemicals'

str4 = {'method': 'Supervised learning', 'goal': 'find patterns'}
print('{data[method]} tries to {data[goal]} in the dataset.'.format(data=str4))
# Supervised learning tries to find patterns in the dataset.

# Format specifier
# {index:specifier}
print('Only {0:.2f}% of the {1} produced worldwide is {2}!'.format(0.12890, 'protein data', 'analyzed'))
# Only 0.13% of the protein data produced worldwide is analyzed!
# :.2f -> use the float with 2 decimal places
# f'{value:{width}.{precision}}'
# value -> any expression that evaluates to a number
# width -> the number of characters used in total to display, but if value needs more space than the width specifies, then the additional space is used.
# precision -> the number of characters used after the decimal point

print("Validation MAE for Random Forest Model: {:,.0f}".format(rf_val_mae))
# : -> indicate formatting follows
# , -> add thousands separator (e.g., 10,000 instead of 10000)
# .0f -> use the float with 0 decimal places == round to zero decimal places (display as an integer)

# Call the function
def multiply_two_num(m, n):
  return m * n

print(f'If you mulitply 5 by 6, the result will be {multiply_two_num(5, 6)}.')
# If you mulitply 5 by 6, the result will be 30.
