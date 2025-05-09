# Shape and Rectangle Classes - Using Abstract Classes and Methods

This Python project demonstrates the use of **abstract classes** and **abstract methods** with the `abc` module. It defines an abstract class `Shape` with an abstract method `area()`, and a derived class `Rectangle` that implements this method.

## ✅ Features

- Uses the `abc` module to create abstract classes.
- Defines the abstract method `area()` in the `Shape` class.
- The `Rectangle` class inherits from `Shape` and implements the `area()` method.

## 💻 Full Code

```python
from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract method, must be implemented in subclasses

# Derived class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height  # Implements the abstract method

# Example usage:
rect = Rectangle(9, 10)
print(f"Area of rectangle: {rect.area()}")    # Output: 90
