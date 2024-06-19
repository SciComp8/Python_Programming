# Ref: https://www.kaggle.com/code/colinmorris/booleans-and-conditionals
var = True
print(var) # True
print(type(var)) # <class 'bool'>

# Get boolean values from boolean operators
def is_suitable_for_atac_seq(fragment_length):
    """
    Is the given fragment length suitable for ATAC-Seq analysis?
    ATAC-Seq typically uses fragments between 50 and 150 bp.
    """
    return 50 <= fragment_length <= 150

print("Is a 30 bp fragment suitable for ATAC-Seq?", is_suitable_for_atac_seq(30)) # False
print("Is a 100 bp fragment suitable for ATAC-Seq?", is_suitable_for_atac_seq(100)) # True
print("Is a 200 bp fragment suitable for ATAC-Seq?", is_suitable_for_atac_seq(200)) # True

# Comparisons
3.0 == 3 # True
'3' == 3 # False

# Comparison operators combined with arithmetic operators
