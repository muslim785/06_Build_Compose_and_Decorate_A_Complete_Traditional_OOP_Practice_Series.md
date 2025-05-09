# 🧑‍🏫 Person and Teacher Classes - Using `super()` in Inheritance

This Python project demonstrates the use of the `super()` function in object-oriented programming. A class `Teacher` inherits from `Person`, and uses `super()` to call the base class constructor.

## ✅ Features

- Shows how to use inheritance in Python
- Demonstrates calling a superclass constructor with `super()`
- Adds custom attributes in both base and derived classes

## 👨‍👩‍👦 Class Structure

- **Person**
  - Constructor: Initializes `name`
- **Teacher (inherits from Person)**
  - Constructor: Calls `Person`'s constructor via `super()`, then initializes `subject`

## 💻 Full Code

```python
class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person initialized with name: {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        print(f"Teacher initialized with subject: {self.subject}")

# Example usage:
teacher1 = Teacher("Mr. Hamza", "Mathematics")
