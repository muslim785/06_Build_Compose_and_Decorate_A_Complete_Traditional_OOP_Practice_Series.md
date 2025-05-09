# Logger Class - Constructors and Destructors

This project demonstrates the use of **constructors** and **destructors** in Python by creating a class named `Logger`. It prints messages during object creation and deletion.

## ✅ Features

- Prints a message when a `Logger` object is created.
- Prints another message when the object is destroyed.
- Demonstrates lifecycle of Python objects.

## 🧰 Requirements

- Python 3.x

## 🚀 Installation

1. Download or clone this repository.
2. Ensure Python 3 is installed on your machine.

## 💻 Full Code

```python
class Logger:
    def __init__(self):
        print("Logger initialized: Object created.")

    def __del__(self):
        print("Logger destroyed: Object deleted.")

# Example usage:
logger1 = Logger()

# Optional: Force deletion
del logger1
