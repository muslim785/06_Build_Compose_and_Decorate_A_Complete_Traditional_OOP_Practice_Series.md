# Custom Iterable Class in Python - Countdown

This project demonstrates how to make a custom class iterable in Python. The `Countdown` class takes a start number and counts down to 0 using the `__iter__()` and `__next__()` methods.

## ✅ Features

- Implements `__iter__()` and `__next__()` to make the class iterable
- Counts down from a starting number to 1 (stopping at 0)
- Works in a `for` loop like a generator

## 💻 Full Code

```python
class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        return self  # The object itself is the iterator

    def __next__(self):
        if self.current <= 0:
            raise StopIteration  # Stop iteration when countdown reaches 0
        self.current -= 1
        return self.current + 1  # Return the current number before decrementing

# Example usage
countdown = Countdown(5)

# Using the Countdown object in a for-loop
for num in countdown:
    print(num)



---

### 📘 Summary

In this example, we use `__iter__()` and `__next__()` to make the `Countdown` class iterable. When using this class in a `for` loop, it counts down from the starting number to 1, stopping when it reaches 0.

Would you like to add features like custom step increments or reverse counting?
