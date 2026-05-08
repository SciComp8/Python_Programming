# Strings are non-scalar objects that can be subdivided

amino_acid = 'glutamic acid'

# Find characters in amino_acid variable
length_string = len(amino_acid)

# Convert to string
to_string = str(length_string)

# Predefined variable
statement = "Number of characters in the name of this amino acid:"

# Concatenate strings and print result
print(statement+' '+to_string)

# Successively concatenate strings
3 * amino_acid
# '3' * amino_acid; error

# Index a string
amino_acid[0]

# Select the first 3 characters
amino_acid[:3]

# Select from 3rd to the 6th character
amino_acid[3:6]

# Select from 3rd character to the end
amino_acid[2:]

# Capitalize the first chracter in a string
print('cycle'.capitalize())
# Cycle
