# Generator () returns a generator object
(2 * num for num in range(5)) 

# List comprehension [] returns a list
[2 * num for num in range(5)]

# Both can be iterated over
num_gen = (2 * num for num in range(5))
for num in num_gen:
    print(num)  

num_gen = [2 * num for num in range(5)]
for num in num_gen:
    print(num)  

# Convert a generator to a list
num_gen = (2 * num for num in range(5))
print(list(num_gen)) 

# Calculate the length of each string element
person_list = ['John', 'Katie', 'Angel', 'Julia', 'Peter']
lengths = (len(person) for person in person_list)
for value in lengths:
    print(value)


# When we prefer generator over list comprehension?
# We prefer the generator when working with *extremely large sequences, 
# as we don't want to store the entire list *in memory, which is what list comprehension would do. 
# We want to generate elements of the sequence on the fly.
(2 * num for num in range(2 ** 10000000000)] # Prefer
print(next(num_gen))
print(next(num_gen))
print(next(num_gen))

[2 * num for num in range(2 ** 10000000000)] 

# Use generators load a very large (streaming) data file line by line
# Case 1: process the first 500 rows of a file line by line, to create a dictionary of the counts of how many times each country appears in a column in the dataset.
counts_dict = {}

# Define read_large_file()
def read_large_file(file_object):
    """A generator function to read a large file line by line on the fly."""
    
    while True: # Loop indefinitely until the end of the file
        data = file_object.readline() # Read a line from the file: data
        if not data: # Break if this is the end of the file
            break
        yield data # Yield the line of data

# Open a connection to a target file using a context manager 'with' statement, ensuring that resources are efficiently allocated when opening a connection to a file.
with open('large_data.csv') as file:
    
    file.readline() # Initialize an empty dictionary: counts_dict
    counts_dict = {} # Initialize an empty dictionary: counts_dict

    # Process only the first 500 rows
    for j in range(0,500):

        #! Split the current line into a list: line
        line = file.readline().split(',')

        #! Return the value for the first column; in this case, it is the country name
        first_col_val = line[0] 

        # If the column value is in the dict, increment its value
        if first_col_val in counts_dict.keys():
            counts_dict[first_col_val] += 1

        # Else, add to the dict and set value to 1
        else:
            counts_dict[first_col_val] = 1

print(counts_dict)

# Case 1.1: process each row of a file line by line on the file, to create a dictionary of the counts of how many times each country appears in a column in the dataset.
counts_dict = {}

# Open a connection to the file
with open('large_data.csv') as file:
    
    for line in read_large_file(file): # Iterate over the generator from read_large_file()

        row = line.split(',')
        first_col = row[0]

        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        else:
            counts_dict[first_col] = 1
        
print(counts_dict)

# Case 2: bioinformatics scenarior: parse a very large genomic data file
def parse_fasta(file_path):
    with open(file_path, 'r') as fasta_file:
        sequence = ""
        for line in fasta_file:
            if line.startswith(">"): 
                if sequence:
                    yield sequence # Yield the previously read sequence
                    sequence = ""
            else:
                sequence += line.strip() # Concatenate lines of the sequence with leading and trailing whitespace removed
        if sequence:
            yield sequence # Yield the last sequence in the file

# Usage example
fasta_file_path = "large_genomic_data.fasta"
sequences = parse_fasta(fasta_file_path)

# Process sequences one by one using next()
try:
    while True:
        sequence = next(sequences)
        print("Processing sequence:", sequence[:20], "...")
except StopIteration:
    print("Finished processing all sequences.")


# Generators in printing the file paths
# os.walk() yields a 3-tuple including dirpath, dirnames, filenames.
# _: capture the dirnames, but ignore them.
import os
for root, dirs, files in os.walk("./data/raw/"): 
   for dir in dirs:
      print(os.path.join(root, dir))
   for file in files:
      print(os.path.join(root, file))

for root, _, files in os.walk("./data/raw/"): 
   for file in files:
      print(os.path.join(root, file))

# Conditionals in the generator
aa = ['histidine', 'isoleucine', 'leucine', 'lysine', 'methionine', 'phenylalanine', 'threonine', 'tryptophan', 'valine']
aa_target = (x for x in aa if "t" in x)
print(list(aa_target))


# Build the generator function that produces the generator objects when called. 
# This function yields a sequence of values instead of returning a single value, using the keyword `yield`.
"""
Case 1
"""
def yield_gene_expression():
    genes = ["Gene1", "Gene2", "Gene3", "Gene4", "Gene5"]
    values = [10.5, 15.2, 8.7, 12.0, 9.8]  
    for gene, value in zip(genes, values):
        yield f"Gene: {gene}, Expression: {value} TPM"

gene_expression_generator = yield_gene_expression()

print(next(gene_expression_generator))
print(next(gene_expression_generator))
print(next(gene_expression_generator))
print(next(gene_expression_generator))
print(next(gene_expression_generator))
# Gene: Gene5, Expression: 9.8 TPM

"""
Case 2
"""
def num_sequence(n):
    """Generate values from 0 to n."""
    i = 0
    while i < n:
        yield i
        i += 1

result = num_sequence(7)
print(type(result)) # <class 'generator'>
for item in result:
    print(item)

"""
Case 3
"""
person_list = ['John', 'Katie', 'Angel', 'Julia', 'Peter']
# Define generator function get_lengths that allows users to input any list
def get_lengths(input_list):
    """Generator function that yields the length of the strings in input_list."""
    for person in input_list:
        yield len(person)

for value in get_lengths(person_list):
    print(value)


