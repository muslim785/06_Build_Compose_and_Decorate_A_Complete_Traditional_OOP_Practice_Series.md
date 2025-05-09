# Employee Class - Access Modifiers in Python

This project demonstrates the use of **access modifiers** in Python using a class called `Employee`.

## 👨‍💼 Class Details

- `name`: Public attribute – accessible from anywhere.
- `_salary`: Protected attribute – accessible, but should be used only within class or subclass.
- `__ssn`: Private attribute – not directly accessible outside the class.

## ✅ Features

- Demonstrates public, protected, and private variable use.
- Shows what happens when trying to access each type of variable.
- Includes name mangling to access private data (not recommended in real-world use).

## 🧰 Requirements

- Python 3.x

## 💻 Full Code

```python
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN (inside class): {self.__ssn}")

emp = Employee("John Doe", 50000, "123-45-6789")

print("Accessing public variable:", emp.name)
print("Accessing protected variable:", emp._salary)

try:
    print("Accessing private variable:", emp.__ssn)
except AttributeError as e:
    print("Error accessing private variable:", e)

print("Accessing private variable with name mangling:", emp._Employee__ssn)

emp.show_info()
