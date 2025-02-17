# Create a range object to produce values from 10 to 15 
values = range(10, 26)

# Calculate the sum of values
sum(values)

# Print each element in a range object
for x in range(6):
    print(x)
# 0
# 1
# 2
# 3
# 4
# 5

for x in range(100, 1001, 100):
    print(x)
# 100
# 200
# 300
# 400
# 500
# 600
# 700
# 800
# 900
# 1000

for x in range(start=100, stop=1001, step=100):
...     print(x)
...
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: range() takes no keyword arguments
