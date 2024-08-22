# Module 3: Python Coding Practices and Packing Concepts

## Python Style Guide and Coding Practices

### Introduction to PEP8
- When you write your code you need to ensure that people/team can read and understand it easily
- This requires some coding standards and conventions
- Python Enhancement Proposal (PEP8) style guide:
    - A document released by python.org
    - Provides conventions and guidelines to make your python code readable and consistenly formatted

### Coding Conventions and Guidelines

#### Key guidelines to improve the readability:

- Using spaces for indentations, instead of tab:
    - The reason: Code editors interprets differently tab character:
        - Some editors interprets it as three(3) spaces
        - Others interprets it as four(4) spaces
    - Four(4) spaces recommended for indentation
- Using blank lines to seperate functions and classes:
    - One blank line
    - Helps establish the beginning and end of different parts of the code
- Using spaces around operators and commas:
    - One space around operators
    - One space after commas

#### Conventions to maintain consistency and manageability
- Create seperate functions for functionalities. This
    - increases the execution speed of the code
    - supports the reuse of the code block in a much more convenient way
- Naming conventions
    - Naming functions and files using lowercase and underscores:
        - Reason: That naming convention is used by Python and it's buil-in functions
        - Leave acronyms in function name as they are(often upercase)
    - Naming packages using lowercase: underscores are discouraged
    - Naming classes using CamelCase
        - aka CapWord case:
        - Helps distinguish between classes and functions
    - Naming constants with upsercase and underscores:
        - Capitalize alll words
        - Seperate all words with underscore

### Static Code Analysis

- Used to manage compliance with these style guidelines without executing the code
- Helps find issues such as:
    - Programming errors
    - Coding standards violations
    - Undefined values
    - Syntax violations
    - Security vulnerabilities
- The PyLint library can be used to check the compliance of your Python code with PEP8 guidelines

- Static code Analysis Resources:
    - [PEP 8 Style Guide for Python Code](https://peps.python.org/pep-0008/)
    - [What Is Static Code Analysis?](https://in.mathworks.com/discovery/static-code-analysis.html)
    - [Static Program Analysis](https://en.wikipedia.org/wiki/Static_program_analysis)
    - [How Static Code Analysis Works](https://www.perforce.com/blog/qac/how-static-code-analysis-works)

### Hands-on Lab: Static Code Analysis

![alt text](./resources/static_code_analysis_lab.png)

pip3 install pylint==2.11.1
create a python file named sample1.py with the following content

```python
# Define a function named 'add' that takes two arguments, 'number1' and 'number2'.
def add(number1, number2):
    # The function returns the sum of 'number1' and 'number2'.
    return number1 + number2

# Initialize the variable 'num1' with the value 4.
num1 = 4

# Initialize the variable 'num2' with the value 5.
num2 = 5

# Call the 'add' function with 'num1' and 'num2' as arguments and store the result in 'total'.
total = add(num1, num2)

# Print the result of adding 'num1' and 'num2' using the 'format' method to insert the values into the string.
print("The sum of {} and {} is {}".format(num1, num2, total))
```

Run th cmd pylint sample1.py

pylint sample1.py 
************* Module sample1
sample1.py:15:0: C0301: Line too long (110/100) (line-too-long)
sample1.py:16:0: C0304: Final newline missing (missing-final-newline)
sample1.py:1:0: C0114: Missing module docstring (missing-module-docstring)
sample1.py:2:0: C0116: Missing function or method docstring (missing-function-docstring)
sample1.py:7:0: C0103: Constant name "num1" doesn't conform to UPPER_CASE naming style (invalid-name)
sample1.py:10:0: C0103: Constant name "num2" doesn't conform to UPPER_CASE naming style (invalid-name)
sample1.py:13:0: C0103: Constant name "total" doesn't conform to UPPER_CASE naming style (invalid-name)
sample1.py:16:6: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)

------------------------------------
Your code has been rated at -3.33/10

On each line of the log, an indicaton is given on the issue, with the line and col where it occurs

Line too long: 110/100: means that the max  number of characters recommended by line is 100
Final newline missing: means that any python code should have a final new line, a new line that ends the code
Missing module docstring
Missing function or method docstring
Constant name "num1" doesn't conform to UPPER_CASE ...
Constant name "num2" doesn't conform to UPPER_CASE ...
Constant name "total" doesn't conform to UPPER_CASE ...

Formatting a regular string which could be a f-string: print(f"The sum of {num1} and {num2} is {total}") is remommended instead of .format  This is because f-strings, introduced in Python 3.6, are generally more readable and efficient.

Finaly a score is assined to the code ; 10 is the max score; the score can be negative as well

create a new file sample.py with the following content

```python
# Define a function named 'add' that takes two arguments, 'number1' and 'number2'.
# The purpose of this function is to add the two numbers and return the result.
def add(number1, number2):
    # Return the sum of 'number1' and 'number2'.
    # This line computes the addition of the two input numbers and outputs the result.
    return number1 + number2

# Initialize the constant variable 'NUM1' with the value 4.
# Constants are usually written in uppercase letters to indicate that they should not be changed.
NUM1 = 4

# Initialize the variable 'num2' with the value 5.
# This variable will be used as the second input to the 'add' function.
num2 = 5

# Call the 'add' function with 'NUM1' and 'num2' as arguments.
# The result of this addition operation is stored in the variable 'total'.
total = add(NUM1, num2)

# Print a formatted string that displays the sum of 'NUM1' and 'num2'.
# The 'format' method is used to insert the values of 'NUM1', 'num2', and 'total' into the string.
print("The sum of {} and {} is {}".format(NUM1, num2, total))
```

Run pylint sample2.py

The score should improve

Now
cp sample2.py sample3.py

Improve the code in sample3.py to reach 10 as score. You should have something that look like the following

```python
"""This is the docstring of the module"""
# Define a function named 'add' that takes two arguments, 'number1' and 'number2'.
# The purpose of this function is to add the two numbers and return the result.
def add(number1, number2):
    """Return the sum of 'number1' and 'number2'."""
    # This line computes the addition of the two input numbers and outputs the result.
    return number1 + number2

# Initialize the constant variable 'NUM1' with the value 4.
# Constants are usually written in uppercase letters to indicate that they should not be changed.
NUM1 = 4

# Initialize the variable 'num2' with the value 5.
# This variable will be used as the second input to the 'add' function.
NUM2 = 5

# Call the 'add' function with 'NUM1' and 'num2' as arguments.
# The result of this addition operation is stored in the variable 'total'.
TOTAL = add(NUM1, NUM2)

# Print a formatted string that displays the sum of 'NUM1' and 'num2'.
# The 'format' method is used to insert the values of 'NUM1', 'num2', and 'total' into the string.
print("The sum of {NUM1} and {NUM2} is {TOTAL}")
```

pylint sample3.py

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

## Unit testing

- A method to validate if units of code are operating as designed
- A unit is a smaller, testable part of an application
- An example of a unit, which has two functions: ![square and doubler ](./resources/square_doubler_unit_test.png)

![alt text](./resources/unit_test_lab.png)

![alt text](./resources/unit_test_lab_end.png)

touch mymodule.py

```py
def square(number):
    """
    This function returns the square of a given number
    """
    return number ** 2

def double(number):
    """
    This function returns twice the value of a given number
    """
    return number * 2
```


touch test_mymodule.py

```py
# Import the 'unittest' module to create unit tests for your code.
import unittest

# Import the 'square' and 'double' functions from the 'mymodule' module.
from mymodule import square, double

# Define a test case class for testing the 'square' function.
# A test case is a single unit of testing. It checks a specific aspect of the code's behavior.
class TestSquare(unittest.TestCase): 

    # Define the first test method for the 'square' function.
    # Test methods should start with the word 'test' so that the test runner recognizes them as test cases.
    def test1(self): 
        # Check that calling 'square(2)' returns 4.
        # This tests if the function correctly computes the square of 2.
        self.assertEqual(square(2), 4) # test when 2 is given as input the output is 4.

        # Check that calling 'square(3.0)' returns 9.0.
        # This tests if the function correctly computes the square of 3.0, verifying that it handles float inputs.
        self.assertEqual(square(3.0), 9.0)  # test when 3.0 is given as input the output is 9.0.

        # Check that calling 'square(-3)' does not return -9.
        # This tests that the function's output is not -9, verifying that the square of -3 should be 9.
        self.assertNotEqual(square(-3), -9)  # test when -3 is given as input the output is not -9.

# Define a test case class for testing the 'double' function.
class TestDouble(unittest.TestCase): 

    # Define the first test method for the 'double' function.
    def test1(self): 
        # Check that calling 'double(2)' returns 4.
        # This tests if the function correctly computes double of 2.
        self.assertEqual(double(2), 4) # test when 2 is given as input the output is 4.

        # Check that calling 'double(-3.1)' returns -6.2.
        # This tests if the function correctly computes double of -3.1, verifying that it handles negative float inputs.
        self.assertEqual(double(-3.1), -6.2) # test when -3.1 is given as input the output is -6.2.

        # Check that calling 'double(0)' returns 0.
        # This tests if the function correctly computes double of 0, verifying that the function works for edge cases.
        self.assertEqual(double(0), 0) # test when 0 is given as input the output is 0.
        
# Run all the test cases defined in the module when the script is executed.
# This will automatically discover and run all the test cases defined in the module.
unittest.main()
```

Run command python3 test_mymodule.py and this will run the tests.


```py
def add(a,b):
    """
    This function returns the sum of the given numbers
    """
    return a + b
```

Final file content
```py
# Import the 'unittest' module to create unit tests for your code.
import unittest

# Import the 'square' and 'double' functions from the 'mymodule' module.
from mymodule import square, double,add

# Define a test case class for testing the 'square' function.
# A test case is a single unit of testing. It checks a specific aspect of the code's behavior.
class TestSquare(unittest.TestCase): 

    # Define the first test method for the 'square' function.
    # Test methods should start with the word 'test' so that the test runner recognizes them as test cases.
    def test1(self): 
        # Check that calling 'square(2)' returns 4.
        # This tests if the function correctly computes the square of 2.
        self.assertEqual(square(2), 4) # test when 2 is given as input the output is 4.

        # Check that calling 'square(3.0)' returns 9.0.
        # This tests if the function correctly computes the square of 3.0, verifying that it handles float inputs.
        self.assertEqual(square(3.0), 9.0)  # test when 3.0 is given as input the output is 9.0.

        # Check that calling 'square(-3)' does not return -9.
        # This tests that the function's output is not -9, verifying that the square of -3 should be 9.
        self.assertNotEqual(square(-3), -9)  # test when -3 is given as input the output is not -9.

# Define a test case class for testing the 'double' function.
class TestDouble(unittest.TestCase): 

    # Define the first test method for the 'double' function.
    def test1(self): 
        # Check that calling 'double(2)' returns 4.
        # This tests if the function correctly computes double of 2.
        self.assertEqual(double(2), 4) # test when 2 is given as input the output is 4.

        # Check that calling 'double(-3.1)' returns -6.2.
        # This tests if the function correctly computes double of -3.1, verifying that it handles negative float inputs.
        self.assertEqual(double(-3.1), -6.2) # test when -3.1 is given as input the output is -6.2.

        # Check that calling 'double(0)' returns 0.
        # This tests if the function correctly computes double of 0, verifying that the function works for edge cases.
        self.assertEqual(double(0), 0) # test when 0 is given as input the output is 0.

class Add(unittest.TestCase): 

    # Define the first test method for the 'double' function.
    def test1(self): 
        # Check that calling 'add(2,4)' returns 6.
        # This tests if the function correctly computes add of 2 and 4.
        self.assertEqual(add(2,4), 6) # test when 2 and 4 are given as input the output is 6.

        # Check that calling 'add(0,0)' returns 0.
        # This tests if the function correctly computes add of 0 and 0.
        self.assertEqual(add(0,0), 0) # test when 0 and 0 are given as input the output is 0.

        # Check that calling 'add(2.3,3.6)' returns 5.9.
        # This tests if the function correctly computes add of 2.3 and 3.6.
        self.assertEqual(add(2.3,3.6), 5.9) # test when 2.3 and 3.6 are given as input the output is 5.9.

        # Check that calling 'add('hello','world')' returns 'helloworld'.
        # This tests if the function correctly computes add of 'hello' and 'world'.
        self.assertEqual(add('hello','world'), 'helloworld') # test when 'hello' and 'world' are given as input the output is 'helloworld'.

        # Check that calling 'add(2.3000,4.300)' returns 6.
        # This tests if the function correctly computes add of 2.3000 and 4.300.
        self.assertEqual(add(2.3000,4.300), 6.6) # test when 2.3000 and 4.300 are given as input the output is 6.
        
        # Check that calling 'add(-2,-2)' does not return 0.
        # This tests if the function correctly computes add of -2 and -2.
        self.assertNotEqual(add(-2,-2), 0) # test when -2 and -2 are given as input the output is not 0.
# Run all the test cases defined in the module when the script is executed.
# This will automatically discover and run all the test cases defined in the module.
unittest.main()
```

## Packaging

### Module vs Package vs Library

- Module:
    - A python file (.py) containing definitions, statements, functions and classes
    - Can import module from other scripts or notebooks
    - Is imported by other scripts or notebooks for use
- Package: 
    - A collection of modules containing an __init__.py file
    - The __init__.py adds code to reference the modules in the package 

- Library:
    - A collection of packages or a single package
    - Examples: Numpy, Pytorch, Pandas
- Package and Library are often used interchangeabily

#### Packaging-Hands-on lab

![alt text](./resources/packaging_lab.png)

create a folder named mymath
cd mymath
touch basic.py

```py
def square(number):
    """
    This function returns the square of a given number
    """
    return number ** 2

def double(number):
    """
    This function returns twice the value of a given number
    """
    return number * 2

def add(a, b):
    """
    This function returns the sum of given numbers
    """
    return a + b
```

touch stats.py

```py
def mean(numbers):
    """
    This function returns the mean of the given list of numbers.
    The mean is calculated as the sum of all numbers divided by the count of numbers.
    """
    # Calculate the mean by summing all the numbers and dividing by the length of the list.
    # 'sum(numbers)' computes the total of all numbers in the list.
    # 'len(numbers)' gives the count of numbers in the list.
    # The mean (or average) is the total sum divided by the number of elements.
    return sum(numbers) / len(numbers)  # Return the mean value.

def median(numbers):
    """
    This function returns the median of the given list of numbers.
    The median is the middle value when the numbers are sorted.
    If there is an even number of observations, it returns the average of the two middle numbers.
    """
    # Sort the list of numbers in ascending order.
    # Sorting is necessary to find the median, as the median depends on the order of values.
    numbers.sort()

    # Check if the number of elements in the list is even.
    # len(numbers) % 2 == 0 evaluates to True if the list has an even number of elements.
    if len(numbers) % 2 == 0:
        # If the list has an even number of elements, find the two middle numbers.
        # 'len(numbers) // 2' computes the index of the second middle element in a zero-indexed list.
        # 'len(numbers) // 2 - 1' computes the index of the first middle element.
        median1 = numbers[len(numbers) // 2]  # The higher index of the two middle values.
        median2 = numbers[len(numbers) // 2 - 1]  # The lower index of the two middle values.
        
        # Calculate the median by taking the average of the two middle numbers.
        # This is done by adding the two middle values and dividing by 2.
        mymedian = (median1 + median2) / 2  # Average of the two middle values.
    else:
        # If the list has an odd number of elements, return the middle number.
        # 'len(numbers) // 2' computes the index of the middle element.
        mymedian = numbers[len(numbers) // 2]  # The middle value for lists with an odd number of elements.

    # Return the calculated median value.
    return mymedian
```

touch __init__.py

```py
from . import basic
from . import stats
```

cd ..

```sh
python3
```

```py
python3      
Python 3.10.12 (main, Jul 29 2024, 16:56:48) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import mymath
>>> mymath.basic.add(3,4)
7
>>> mymath.stats.mean([3,4,5])
4.0
>>> exit()
```

![alt text](./resources/module_summary.png)

[Cheatsheet: Python Coding Practices and Packaging Concepts](https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTVNraWxsc05ldHdvcmstUFkwMjI0RU4tQ291cnNlcmEvbGFicy9yZWFkaW5nL20xL0NoZWF0c2hlZXQubWQiLCJ0b29sX3R5cGUiOiJpbnN0cnVjdGlvbmFsLWxhYiIsImFkbWluIjpmYWxzZSwiaWF0IjoxNzIxODE4NzEyfQ.FUIZ2Obc65IW4DdQOZsJiWkrl5_DjuQLtSN_cPMIamE)