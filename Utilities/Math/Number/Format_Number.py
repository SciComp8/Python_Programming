# Case 1:
num = 100**10
print(num)
# 100000000000000000000
print(f"{num:,}") 
# 100,000,000,000,000,000,000

type(f"{num:,}")
# <class 'str'>
type(print(f"{num:,}"))
# <class 'NoneType'>
# Notice that printing a value but not returning a value will result in <NoneType>.

# Case 2:
# f'{value:{width}.{precision}}'
# value -> any expression that evaluates to a number
# width -> the number of characters used in total to display, but if value needs more space than the width specifies, then the additional space is used.
# precision -> the number of characters used after the decimal point
num = 0.00000001
print(num)
# 1e-08
print(f"{num:10.8f}") 
# 0.00000001
print(f"{num:.8f}") 
# 0.00000001

