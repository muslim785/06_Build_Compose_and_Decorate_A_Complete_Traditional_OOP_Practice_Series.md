# Python Callable Objects using `__call__()` Method

This example shows how to make a Python object **callable like a function** by implementing the special `__call__()` method. We also use the built-in `callable()` function to verify this behavior.

## ✅ Features

- Implements the `__call__()` method in a class
- Demonstrates how objects can be used like functions
- Uses `callable()` to check if an object is callable

## 💻 Full Code

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

# Example usage
m = Multiplier(5)

# Check if the object is callable
print("Is m callable?", callable(m))

# Use the object like a function
result = m(10)
print("Result of m(10):", result)




---

### 📘 Summary

With `__call__()`, you can turn objects into function-like behavior—this is especially useful in advanced programming like decorators, machine learning pipelines, or middleware design.

Would you like to extend this example to support addition or other operations as well?
