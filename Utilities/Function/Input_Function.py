#define and set variables from user input (casted to a float)
total_reads = float(input("Enter the total number of reads: "))
mutant_reads = float(input("Enter the number of mutant reads: "))

#calculate the mutational frequency
mutational_frequency = (mutant_reads / total_reads) * 100  #calculate the frequency in percentage

#round the mutational frequency to 2 decimal places
mutational_frequency = round(mutational_frequency, 2)

#print the final mutational frequency
print("The mutational frequency is ", mutational_frequency, "%", sep='')


def math_2_num(x, y):
    if y == 0:
        raise ValueError("Division by zero is not allowed.")
    addition = x + y
    yield f"The addition of the two numbers is: {addition}"
    subtract = x - y
    yield f"The subtraction of the two numbers is: {subtract}"
    multiply = x * y
    yield f"The multiplication of the two numbers is: {multiply}"
    division = x / y
    yield f"The division of the two numbers is: {division}"
    # Calculate the derivative of the functions with respect to x
    derivative_addition = 1
    yield f"The derivative of addition with respect to x is: {derivative_addition}"
    derivative_subtract = 1
    yield f"The derivative of subtraction with respect to x is: {derivative_subtract}"
    derivative_multiply = y
    yield f"The derivative of multiplication with respect to x is: {derivative_multiply}"
    derivative_division = 1 / y
    yield f"The derivative of division with respect to x is: {derivative_division}"

# Ask the users to input the first number of their choice
num1 = int(input("Please enter the first number: "))
# Ask the users to input the second number of their choice
num2 = int(input("Please enter the second number: "))

print("The two numbers are", num1, "and", num2)

for result in math_2_num((num1, num2):
    print(result)


def math_2_num_2(x, y):
    addition = x + y
    yield f"The addition of the two numbers is: {addition}"
    subtract = x - y
    yield f"The subtraction of the two numbers is: {subtract}"
    multiply = x * y
    yield f"The multiplication of the two numbers is: {multiply}"
    derivative_multiply = y
    yield f"The derivative of multiplication with respect to x is: {derivative_multiply}"
    if y != 0:
        division = x / y
        yield f"The division of the two numbers is: {division}"
        derivative_addition = 1
        yield f"The derivative of addition with respect to x is: {derivative_addition}"
        derivative_subtract = 1
        yield f"The derivative of subtraction with respect to x is: {derivative_subtract}"
        derivative_division = 1 / y
        yield f"The derivative of division with respect to x is: {derivative_division}"
    else:
        yield "Division and its related derivative are undefined when the second number is zero."

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

print("The two numbers are", num1, "and", num2)

for result in math_2_num_2(num1, num2):
    print(result)

