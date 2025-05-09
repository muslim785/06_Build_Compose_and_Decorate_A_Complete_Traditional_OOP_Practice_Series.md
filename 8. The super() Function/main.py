class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person initialized with name: {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call the constructor of the Person class
        self.subject = subject
        print(f"Teacher initialized with subject: {self.subject}")

# Example usage:
teacher1 = Teacher("Mr. Hamza", "Mathematics")
