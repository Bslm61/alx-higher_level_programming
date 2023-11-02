<<<<<<< HEAD
def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name must be a string")
    full_name = f"My name is {first_name} {last_name}"
    print(full_name)

# Example usage:
say_my_name("John", "Doe")  # Prints: My name is John Doe
say_my_name("Alice")       # Prints: My name is Alice
say_my_name(123, "Smith")  # Raises a TypeError exception

=======
#!/usr/bin/python3
"""
Print the name of a user
"""


def say_my_name(first_name, last_name=""):
    """a program to print name

    first_name: the firstname string
    last_name: the second string

    Raises:
        TypeError: if first_name is not instance of str
        TypeError: if last_name is not intance of str
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
>>>>>>> 5556f47e958b52121281de8e7bf3f6c40c84a57f
