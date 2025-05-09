# Counter Class - Object Creation Tracker

This Python program defines a `Counter` class that keeps track of how many objects have been created. It uses a class variable and a class method with `cls` to manage and display the object count.

## Features
- Tracks the number of `Counter` objects created.
- Displays the current count using a class method.
- Demonstrates the use of class variables and class methods in Python.

## Requirements
- Python 3.x

## Installation
1. Clone this repository or download the files to your local machine.
2. Ensure Python 3 is installed on your machine.

## How to Use
1. Create instances of the `Counter` class.
2. Call the class method `display_count()` to display the number of objects created.

### Example Usage:

```python
counter1 = Counter()
counter2 = Counter()
counter3 = Counter()
counter4 = Counter()
counter5 = Counter()

# Display the count of objects created
Counter.display_count()  # Should print: Number of objects created: 5
