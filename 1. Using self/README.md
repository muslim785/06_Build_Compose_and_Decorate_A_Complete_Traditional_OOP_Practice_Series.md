# Student Grade Management System

This is a simple Python program that defines a `Student` class. The class stores student details like name and marks, calculates the student's grade, and displays the information. It includes data validation and error handling to ensure the provided inputs are correct.

## Features
- Stores student name and marks.
- Calculates and assigns grades based on marks.
- Validates input data (name should be a non-empty string, marks should be between 0 and 100).
- Displays student details and their corresponding grade.

## Requirements
- Python 3.x

## Installation
1. Clone this repository or download the files to your local machine.
2. Ensure that Python 3 is installed on your machine.

## How to Use
1. Create a `Student` object by passing the student's name and marks.
2. Call the `display()` method to view the student's details, including the grade.

### Example Usage:

```python
student1 = Student("MUSLIM HABIB", 99)
student1.display()
