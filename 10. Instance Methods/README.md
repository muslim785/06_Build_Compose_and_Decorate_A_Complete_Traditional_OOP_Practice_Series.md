# Dog Class - Instance Methods

This Python project demonstrates the use of **instance methods** by defining a `Dog` class. The class has instance variables `name` and `breed`, and an instance method `bark()` that prints a message including the dog's name.

## ✅ Features

- Defines instance variables: `name` and `breed`
- Implements an instance method `bark()` that prints the dog's name in a barking message
- Shows how to use instance methods to operate on object-specific data

## 💻 Full Code

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking! Woof Woof!")

# Example usage:
dog1 = Dog("Buddy", "Golden Retriever")
dog1.bark()  # Output: Buddy is barking! Woof Woof!
