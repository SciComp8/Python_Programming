# References
# https://www.kaggle.com/code/colinmorris/booleans-and-conditionals
# https://github.com/SciComp8/Python_Programming/blob/main/Kaggle/Learn_Python/Exercise_Booleans_Conditionals.py#L58
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


prepared_for_cyberattack = has_firewall or (attack_risk_level < 5 and has_intrusion_detection) or not (attack_risk_level > 0 and is_business_hours)
prepared_for_cyberattack = (
    has_firewall
    or ((attack_risk_level < 5) and has_intrusion_detection))
    or (not ((attack_risk_level > 0) and is_business_hours))
)

# Combine boolean operators and conditional statements
# elif and else blocks are optional
def classify_temperature(temp):
    if temp == 0:
        print(temp, "degrees is freezing point.")
    elif temp > 0:
        print(temp, "degrees is above freezing.")
    elif temp < 0:
        print(temp, "degrees is below freezing.")
    else:
        print(temp, "is unlike any temperature I've ever measured...")

classify_temperature(6)
classify_temperature(0)

# Convert things to boolean values
print(bool(90)) # True
print(bool(0)) # False
print(bool("congress")) # True
print(bool("")) # False
print(bool(())) # False
print(bool([])) # False
print(bool({})) # False
