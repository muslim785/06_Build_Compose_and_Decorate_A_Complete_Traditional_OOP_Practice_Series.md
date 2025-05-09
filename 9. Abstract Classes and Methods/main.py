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
print(f"Area of rectangle: {rect.area()}")  # Output: 90
