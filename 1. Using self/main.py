class Student:
    def __init__(self, name, marks):
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string.")
        
        if not isinstance(marks, (int, float)) or not (0 <= marks <= 100):
            raise ValueError("Marks must be a number between 0 and 100.")

        self.name = name
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A1"
        elif self.marks >= 75:
            return "A"
        elif self.marks >= 60:
            return "B"
        elif self.marks >= 40:
            return "C"
        else:
            return "F"

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.get_grade()}")

# Example usage with error handling:
try:
    student1 = Student("MusLIM HABIB", 99)
    student1.display()
    print("-----")

    student2 = Student("UZAIR AHMAD", 35)  # Invalid marks
    student2.display()

except ValueError as e:
    print(f"Error: {e}")
