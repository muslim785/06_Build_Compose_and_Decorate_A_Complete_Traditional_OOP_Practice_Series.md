# Python Property Decorators - @property, @setter, @deleter

This example demonstrates how to use **property decorators** in Python to encapsulate and control access to a class attribute using `@property`, `@setter`, and `@deleter`.

## ✅ Features

- Encapsulates the `_price` attribute in a class
- Allows safe access and modification using decorators
- Prints messages on get, set, and delete operations

## 💻 Full Code

```python
class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        print("Getting price...")
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative.")
        else:
            print("Setting price...")
            self._price = value

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Example usage
p = Product(100)
print(p.price)      # Getting
p.price = 150       # Setting
print(p.price)
del p.price         # Deleting




---

### 📘 Summary

This pattern is a clean and Pythonic way to manage attributes—offering control, validation, and flexibility while keeping a simple interface for the user.

Would you like to include validation logic for string or other types of properties too?
