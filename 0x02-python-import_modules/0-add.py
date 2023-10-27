def add(a, b):
    """
    Adds two numbers and returns the result.

    Parameters:
    - a (int): The first number to be added.
    - b (int): The second number to be added.

    Returns:
    int: The sum of the two numbers.

    Examples:
    >>> add(1, 2)
    3
    >>> add(5, -3)
    2
    """

    return a + b

# Assigning values to variables a and b
a = 1  # Assigning the value 1 to variable a
b = 2  # Assigning the value 2 to variable b

# Importing the add function from add_0.py
from add_0 import add

# Printing the result of the addition
print(f"{a} + {b} = {add(a, b)}")
