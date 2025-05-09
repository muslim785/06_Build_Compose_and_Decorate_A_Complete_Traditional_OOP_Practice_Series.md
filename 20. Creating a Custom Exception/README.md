# Custom Exception in Python - `InvalidAgeError`

This project demonstrates how to create and use a **custom exception** in Python. A custom exception class `InvalidAgeError` is defined and used in a function to enforce age restrictions.

## ✅ Features

- Defines a custom exception class `InvalidAgeError`
- Uses `raise` to trigger the exception for invalid input
- Handles the exception using `try...except`

## 💻 Full Code

```python
# Define a custom exception
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or older."):
        super().__init__(message)

# Function to check age
def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. You must be 18 or older.")
    else:
        print(f"Access granted. Your age is {age}.")

# Example usage
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print("Custom Exception Caught:", e)
except ValueError:
    print("Please enter a valid number.")



---

### 📘 Summary

This example shows how to improve code clarity and maintainability by defining your own error types, making it easier to debug and handle specific conditions.

Would you like to extend this by validating name inputs or writing these logs to a file?
