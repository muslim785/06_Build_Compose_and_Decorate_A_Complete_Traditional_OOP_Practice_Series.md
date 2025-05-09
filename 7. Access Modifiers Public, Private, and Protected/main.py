class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public variable
        self._salary = salary     # Protected variable
        self.__ssn = ssn          # Private variable

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN (inside class): {self.__ssn}")

# Create an object
emp = Employee("Uzair", 50000, "123-45-6789")

# Accessing variables
print("Accessing public variable:", emp.name)         # ✅ Works
print("Accessing protected variable:", emp._salary)   # ⚠️ Works, but not recommended
try:
    print("Accessing private variable:", emp.__ssn)    # ❌ Fails
except AttributeError as e:
    print("Error accessing private variable:", e)

# Accessing private variable using name mangling
print("Accessing private variable with name mangling:", emp._Employee__ssn)

# Show all info using a class method
emp.show_info()
