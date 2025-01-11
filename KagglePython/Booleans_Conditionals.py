# Ref: https://www.kaggle.com/code/colinmorris/booleans-and-conditionals
var = True
print(var) # True
print(type(var)) # <class 'bool'>

# Get boolean values from boolean operators
def is_ok_for_atac_seq(fragment_length):
    """
    Is the given fragment length suitable for ATAC-Seq analysis?
    ATAC-Seq typically uses fragments between 50 and 150 bp.
    """
    return 50 <= fragment_length <= 150

print("Is a 30 bp fragment suitable for ATAC-Seq?", is_ok_for_atac_seq(30)) # False
print("Is a 100 bp fragment suitable for ATAC-Seq?", is_ok_for_atac_seq(100)) # True
print("Is a 200 bp fragment suitable for ATAC-Seq?", is_ok_for_atac_seq(200)) # True

# Comparisons
9.0 == 9 # True
'9' == 9 # False

# Comparison operators combined with arithmetic operators 
def is_even(n):
    return (n % 2) == 0

print("Is 60 even?", is_even(60))
print("Is 9 even?", is_even(9))

# Combine boolean values
def is_ok_for_atac_seq2(fragment_length):
    """
    Is the given fragment length suitable for ATAC-Seq analysis?
    ATAC-Seq typically uses fragments between 50 and 150 bp.
    Additionally, the fragment length must be an even number.
    """
    return 50 <= fragment_length <= 150 and fragment_length % 2 == 0

print("Is a 30 bp fragment suitable for ATAC-Seq?", is_ok_for_atac_seq2(30)) # False
print("Is a 100 bp fragment suitable for ATAC-Seq?", is_ok_for_atac_seq2(100)) # True
print("Is a 200 bp fragment suitable for ATAC-Seq?", is_ok_for_atac_seq2(200)) # True
