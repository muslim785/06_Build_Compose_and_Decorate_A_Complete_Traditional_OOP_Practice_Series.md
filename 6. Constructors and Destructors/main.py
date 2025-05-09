class Logger:
    def __init__(self):
        print("Logger initialized: Object created.")

    def __del__(self):
        print("Logger destroyed: Object deleted.")

# Example usage:
logger1 = Logger()

# Forcing deletion to demonstrate destructor call (optional)
del logger1

# Note: The destructor may also be called automatically when the script ends or object goes out of scope.
