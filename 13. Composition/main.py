class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  # Composition: Car HAS-A Engine

    def start_car(self):
        print(f"{self.brand} car: {self.engine.start()}")

# Example usage:
my_engine = Engine()
my_car = Car("Toyota", my_engine)
my_car.start_car()
