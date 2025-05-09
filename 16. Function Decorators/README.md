# Function Decorators in Python - Logging Function Call

This project demonstrates how to use **function decorators** in Python. We create a decorator called `log_function_call` that logs a message before calling the actual function.

## ✅ Features

- Defines a custom decorator `log_function_call`
- Prints a message before the target function is executed
- Applied to a function `say_hello()` using the `@` syntax

## 💻 Full Code

```python
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def say_hello():
    print("Hello!Muslim")

# Example usage
say_hello()



---

### 🔍 Summary

- This example shows how decorators work by adding behavior (a log message) before a function runs.
- It uses the `@decorator_name` syntax to apply the decorator to a function.

Would you like to extend this decorator to log the function's name or execution time as well?
