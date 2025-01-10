# Walrus Operator (:=): the walrus operator allows us to assign values to variables as part of an expression. 
# This is useful for cases where we want to both assign a value and use it in a loop or conditional statement, without needing a separate line for assignment.
# enumerate: https://github.com/SciComp8/Python_Programming/blob/main/Utilities/Tuple/Enumerate_Position.py

import numpy as np

for i, number in enumerate(squared_numbers := np.arange(10, 60, 10)**2):
    print(f"Index {i}: Squared {number}")
# Index 0: Squared 100
# Index 1: Squared 400
# Index 2: Squared 900
# Index 3: Squared 1600
# Index 4: Squared 2500
