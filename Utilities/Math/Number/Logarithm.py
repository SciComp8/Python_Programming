m = 9
n = np.log(m)
print(n, f" | m = e^n: {np.exp(n)}")

# Interpret: np.exp(n) is 9.000000000000002 is not quite 9. 
# This is due to floating point precision. 
# The standard for floating point numbers does not always give exactly the correct number when performing the division calculation.
# Because a finite number of bits are used to store numbers in.
