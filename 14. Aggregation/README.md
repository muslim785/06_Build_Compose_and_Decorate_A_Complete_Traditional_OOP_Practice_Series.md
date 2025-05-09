# Department and Employee Classes - Aggregation in Python

This Python project demonstrates **aggregation**, where one class stores a reference to another class's object that exists independently. A `Department` object references an `Employee` object without owning its lifecycle.

## ✅ Features

- Defines `Employee` and `Department` classes
- An existing `Employee` object is passed to the `Department` constructor
- Demonstrates how objects can be shared across classes

## 💻 Full Code

```python
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_details(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}"

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation

    def show_employee(self):
        print(f"Department: {self.dept_name}")
        print("Employee Info:", self.employee.get_details())

# Example usage:
emp = Employee("Dua", 101)
dept = Department("HR", emp)
dept.show_employee()



---

### 📘 Explanation

- The `Employee` class defines employee details.
- The `Department` class holds a reference to an existing `Employee` object.
- The employee exists before and independently of the department, showing a classic aggregation relationship.

Would you like to allow one department to hold multiple employees using a list?
