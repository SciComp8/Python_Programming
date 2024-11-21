# Major types of errors in Python programming
## Syntax Errors, also known as parsing errors
The syntax errors indicate the syntax or structure of the code is incorrect. They are detected by the compiler or the interpreter.
### Concatenate 2 different types of objects
  ```python
  print('6 % 6 = ' + 6 % 6)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: can only concatenate str (not "int") to str
  ```

### Compare a number with a string
  ```python
age = input('Please type your age: ')
print('Are you older than 10?', age > 10)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print('Are you older than 10?', age > 10)
TypeError: '>' not supported between instances of 'str' and 'int'
  ```

### Wrongly written keywords
  ```python
  Cell In[17], line 3
  return y
  ^
  SyntaxError: 'return' outside function
  ```
### Name is not defined (e.g., wrong variable/function names)
  ```python
  a = 8
  print(AA)
  Traceback (most recent call last):
    File "<pyshell#37>", line 1, in <module>
    print(AA)
  NameError: name 'AA' is not defined. Did you mean: 'aa'?

  NameError                                 Traceback (most recent call last)
  Cell In[18], line 1
  ----> 1 devide_two(98.920)
  NameError: name 'devide_two' is not defined
  ```
### Wrong input
  ```python
  age = int(input('Please type your age: '))
  Sixteen
  Traceback (most recent call last):
    File "<pyshell#44>", line 1, in <module>
    age = int(input('Please type your age: '))
  ValueError: invalid literal for int() with base 10: 'Sixteen'

  age = input('Please type your age: ')

  try:
      age = int(age)
      print('How old will you be in 2 year?', age + 1)
  except ValueError:
      print('The given age is not valid')
  ```
### Setting extra parameters
  ```python
  TypeError                                 Traceback (most recent call last)
  Cell In[14], line 4
  2 y = 5
  3 # Which of the two variables above has the smallest absolute value?
  ----> 4 smallest_abs = min(abs(x, y))
  TypeError: abs() takes exactly one argument (2 given)
  ```
### Two starred expressions in assignment
  ```python
  *__, a, b, *_ = ['a', 'cde', 'bib', 6, 9, 10]
  File "<stdin>", line 1
  SyntaxError: two starred expressions in assignment
  ```
### Wrong use of an operator

### Forgetting parentheses in a function call

### Call the locally scoped function
  ```python
  def house():
    print("Gallary from house()")
    def first_house():
        print("Gallary from first_house()")
    def second_house():
        print("Gallary from second_house()")
    first_house()
    second_house()

  first_house()
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  NameError: name 'first_house' is not defined
  ```
### Not putting strings in single quotes or double quotes

## Runtime Errors
### No compatible binary
  ```python
  DEBUG [main] Printing verbose output
  Traceback (most recent call last):
    File "/Users/your_name/.pyenv/versions/3.8.18/bin/kb", line 8, in <module>
      sys.exit(main())
    File "/Users/your_name/.pyenv/versions/3.8.18/lib/python3.8/site-packages/ngs_tools/logging.py", line 62, in inner
      return func(*args, **kwargs)
    File "/Users/your_name/.pyenv/versions/3.8.18/lib/python3.8/site-packages/kb_python/main.py", line 1583, in main
      raise UnsupportedOSError(
    kb_python.config.UnsupportedOSError: Failed to find compatible kallisto binary. Provide a compatible binary with the --kallisto option or    run kb compile."
  ```
### No compatible tensor shape
  ```python
  data_1 = torch.tensor([[1, 5, 6], [2, 6, 9]])
  data_2 = torch.tensor([[0, 1], [3, 3]])
  data_1 + data_2
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  RuntimeError: The size of tensor a (3) must match the size of tensor b (2) at non-singleton dimension 1
 ```

## Logical Errors


# More reading
- https://docs.python.org/3/tutorial/errors.html


