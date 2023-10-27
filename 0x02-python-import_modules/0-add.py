# Importing the required function from the simple file
from simple_file import simple_function

def import_simple_function():
    """
    Function to import a simple function from a simple file.

    Returns:
    - str:
        Returns a string indicating that the function has been imported successfully.
    """

    # Importing the simple_function from the simple_file
    # Assuming that the simple_file.py is in the same directory as this script
    try:
        from simple_file import simple_function
        return "Simple function imported successfully."
    except ImportError:
        return "Error: Failed to import the simple function."

# Example usage of the import_simple_function
result = import_simple_function()
print(result)
