def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name must be a string")
    full_name = f"My name is {first_name} {last_name}"
    print(full_name)

# Example usage:
say_my_name("John", "Doe")  # Prints: My name is John Doe
say_my_name("Alice")       # Prints: My name is Alice
say_my_name(123, "Smith")  # Raises a TypeError exception

