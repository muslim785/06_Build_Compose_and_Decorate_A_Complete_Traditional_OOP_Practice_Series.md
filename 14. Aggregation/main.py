class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_details(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}"

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: uses an existing Employee object

    def show_employee(self):
        print(f"Department: {self.dept_name}")
        print("Employee Info:", self.employee.get_details())

# Example usage:
emp = Employee("Dua", 101)
dept = Department("HR", emp)
dept.show_employee()
