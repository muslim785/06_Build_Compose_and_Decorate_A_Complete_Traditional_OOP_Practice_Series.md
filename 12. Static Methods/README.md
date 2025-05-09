# TemperatureConverter Class - Static Method Example

This Python project demonstrates the use of a **static method** in a utility-style class. The `TemperatureConverter` class provides a method for converting temperatures from Celsius to Fahrenheit.

## ✅ Features

- Defines a static method `celsius_to_fahrenheit(c)`
- No need to create an object to use the method
- Ideal for utility functions that don't require instance or class context

## 💻 Full Code

```python
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Example usage:
temp_c = 25
temp_f = TemperatureConverter.celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C is equal to {temp_f}°F")
