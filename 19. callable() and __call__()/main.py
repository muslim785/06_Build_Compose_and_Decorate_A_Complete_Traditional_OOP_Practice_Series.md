class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

# Example usage
m = Multiplier(5)

# Check if the object is callable
print("Is m callable?", callable(m))

# Use the object like a function
result = m(10)
print("Result of m(10):", result)
