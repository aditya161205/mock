```python
# example_module.py

# -------- Functions --------
def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b

def multiply_numbers(a, b):
    """Return the product of two numbers."""
    return a * b

def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0

def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

# -------- Classes --------
class Calculator:
    """A simple calculator that uses utility functions."""

    def __init__(self, value=0):
        self.value = value

    def add(self, number):
        self.value = add_numbers(self.value, number)
        return self.value

    def multiply(self, number):
        self.value = multiply_numbers(self.value, number)
        return self.value


class Person:
    """Represents a person with a name and age."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return greet(self.name) + f" I am {self.age} years old."

    def is_adult(self):
        return self.age >= 18
```
