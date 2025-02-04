# List comprehensions allow us to create lists from other lists or from columns of DataFrames, among many other objects, except the integer object.
# It is a single line of code, and more efficient than a for loop. See case 1.2
# Construct a list comprehension
# newlist = [expression for iterator variable in iterable] # iterator variable = item
# Case 1:
nums = [2, 8, 10, 1, 21, 60]
nums_plus_1 = [num + 1 for num in nums]
print(nums_plus_1) 
# [3, 9, 11, 2, 22, 61]

# Case 1.2:
import time
nums = range(0, 1000000)
start_time = time.time()
nums_plus_1 = [num + 1 for num in nums]
print(time.time() - start_time) # 0.26391100883483887 seconds

nums_plus_1 = []
start_time = time.time()
for num in nums:
    nums_plus_1.append(num)  
print(time.time() - start_time) # 7.955948829650879 seconds

# Case 1.3: 
titlecase_cakes = [cakes.title() for cake in cakes]
print(titlecase_cakes)

# Case 2:
nums_minus_1 = [num - 1 for num in range(11)]
print(nums_minus_1)
# [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Case 3: nested for loops
pairs = [(num1, num2) for num1 in range(5, 8) for num2 in range(9, 12)]
print(pairs)
# [(5, 9), (5, 10), (5, 11), (6, 9), (6, 10), (6, 11), (7, 9), (7, 10), (7, 11)]

# Case 4: nested list comprehensions
# [[output expression] for iterator variable in iterable]
# Output expression is itself a list comprehension
# Create a 10 x 10 matrix using a list of lists: matrix
matrix = [[col for col in range(10)] for row in range(10)]

# Print the matrix
for row in matrix:
    print(row)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Case 5: conditionals on the iterable in comprehensions
# newlist = [expression for iterator variable in iterable + conditional on iterator variable]
# Only do the operations on iterator variables that fit the condition

# Drop column with any missing value
col_miss = [col for col in df.columns if df[col].isnull().any()]
df_clean = df.drop(col_miss, axis=1)
# Iterator variable: col; iterable: df.columns; conditional on iterator variable: if df[col].isnull().any()

aa = ['histidine', 'isoleucine', 'leucine', 'lysine', 'methionine', 'phenylalanine', 'threonine', 'tryptophan', 'valine']
aa_target = [x for x in aa if "t" in x]
print(aa_target)
# ['histidine', 'methionine', 'threonine', 'tryptophan']


# Case 5.1: estimate the proportion of positives/negatives/zeros in a list
def calc_prop(data): 
    total = len(data)
    num_pos = sum([1 for i in data if i > 0]) # Notice
    num_neg = sum([1 for i in data if i < 0])
    num_zero = total - (num_pos + num_neg)
    
    ratio_pos = num_pos / total
    ratio_neg = num_neg / total
    ratio_zero = num_zero / total
    
    print(f'{ratio_pos:.2f}')
    print(f'{ratio_neg:.2f}')
    print(f'{ratio_zero:.2f}')

sample = [-9, 2, 3, 0, 0, 2, 3, 6]
calc_prop(data=sample)
# 0.62
# 0.12
# 0.25

# Case 6: conditionals on the output expression in comprehensions ~ if-else
# newlist = [expression + conditional on expression for iterator variable in iterable]
# substitute phenylalanine with methionine
aa = ['histidine', 'isoleucine', 'leucine', 'lysine', 'methionine', 'phenylalanine', 'threonine', 'tryptophan', 'valine']
aa_target_2 = [x if x != 'phenylalanine' else 'methionine' for x in aa]
print(aa_target_2)
# ['histidine', 'isoleucine', 'leucine', 'lysine', 'methionine', 'methionine', 'threonine', 'tryptophan', 'valine']

adata.obs['condition'] = ['stimulated' if sm_i == 'Oprozomib (ONX 0912)' else 'control' for sm_i in adata.obs['sm_name']]

# Case 7: nested conditionals on the output expression in comrehension ~ if-elif-else
# expression1 if condition1 else expression2 if condition2 else expresion3
# expression1 if condition1 else (expression2 if condition2 else expresion3)
# amino_acid = ['His', 'Val', 'Cys']
# ['Cysteine' if aa == 'Cys' else 'Histidine' if aa == 'His' else 'Valine' if aa == 'Val' else 'Other' for aa in amino_acid]
# ['Histidine', 'Valine', 'Cysteine']

# Case 8:
from collections import Counter
penguins = [{'Species': 'Gentoo',
  'Flipper Length (mm)': 230.0,
  'Body Mass (g)': 5500.0,
  'Sex': 'MALE'},
 {'Species': 'Chinstrap',
  'Flipper Length (mm)': 201.0,
  'Body Mass (g)': 4300.0,
  'Sex': 'MALE'},
 {'Species': 'Adlie',
  'Flipper Length (mm)': 180.0,
  'Body Mass (g)': 3800.0,
  'Sex': 'MALE'}]

penguins_sex_counts = Counter([penguin['Sex'] for penguin in penguins])
print(penguins_sex_counts)
# Counter({'MALE': 3})
print(penguins_sex_counts.most_common())
# [('MALE', 3)]
