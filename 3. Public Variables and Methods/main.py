class Car:
    # Public variable
    brand = "Toyota"

    def start(self):
        # Public method
        print(f"The {self.brand} car is starting.")

# Example usage:
car1 = Car()  # Instantiate the Car class

# Accessing the public variable from outside the class
print(car1.brand)  # Output: Toyota

# Calling the public method from outside the class
car1.start()  # Output: The Toyota car is starting.
