# Car and Engine Classes - Composition in Python

This Python project demonstrates the concept of **composition**, where one class contains an object of another class as part of its state. Specifically, a `Car` class is composed with an `Engine` object and uses its method.

## ✅ Features

- Defines two classes: `Engine` and `Car`
- The `Car` class accepts an `Engine` object through its constructor
- The `Car` class accesses the `start()` method from the `Engine` class

## 💻 Full Code

```python
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


---

### 📘 Explanation

- `Engine` class has a method `start()` that returns a message.
- `Car` class takes an `Engine` object and stores it as an instance variable.
- `Car.start_car()` method calls `self.engine.start()` to delegate the task to the engine.

Would you like to add more engine behaviors like `stop()` or `status()` and use them in the `Car` class?
