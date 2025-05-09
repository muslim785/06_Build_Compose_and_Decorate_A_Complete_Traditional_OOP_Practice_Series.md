# Class Decorators in Python - Add Method Dynamically

This example demonstrates how to use a **class decorator** to dynamically add a method to a class in Python. The decorator `add_greeting` adds a new method `greet()` to the target class.

## ✅ Features

- Uses a class decorator `add_greeting`
- Dynamically adds a `greet()` method to the decorated class
- Keeps the original class functionality intact

## 💻 Full Code

```python
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Example usage
p = Person("Ayan")
print(p.greet())




---

### 📘 Summary

- `add_greeting` adds a method to the `Person` class without changing its original definition.
- This is useful for adding common features to multiple classes (e.g. logging, auditing, metadata).

Would you like to try adding multiple methods using a single class decorator?
