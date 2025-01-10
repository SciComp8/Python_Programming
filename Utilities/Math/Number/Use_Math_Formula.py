# Reference: https://www.cuemath.com/algebra/sum-of-cubes-of-n-natural-numbers/#

import time

def math_formula(n):
    """
    Calculate the sum of cubes of the first 'n' natural numbers using a math formula.

    :param n: An integer representing the number of natural numbers to consider.
    :return: The sum of cubes of the first 'n' natural numbers.
    """
    return (n * (n + 1) / 2) ** 2

def for_loop(n):
    """
    Calculate the sum of cubes of the first 'n' natural numbers using a for loop.

    :param n: An integer representing the number of natural numbers to consider.
    :return: The sum of cubes of the first 'n' natural numbers.
    """
    result = 0
    for i in range(1, n + 1):
        result += i ** 3
    return result

n = 1000000

start_time_math = time.time()
result_math = math_formula(n)
end_time_math = time.time()
print(f"Execution Time (Analytical Approach): {end_time_math - start_time_math} seconds") 
# Execution Time (Analytical Approach): 0.0009810924530029297 seconds

start_time_for = time.time()
result_for = for_loop(n)
end_time_for = time.time()
print(f"Execution Time (For Loop Approach): {end_time_for - start_time_for} seconds")
# Execution Time (For Loop Approach): 0.07994413375854492 seconds

diff_speed = ((end_time_for - start_time_for) - (end_time_math - start_time_math)) / (end_time_math - start_time_math) * 100
print(f"Analytical Approach is running {diff_speed} % faster than For Loop Approach")
# Analytical Approach is running 8048.481166464156 % faster than For Loop Approach
