# Diamond Inheritance and Method Resolution Order (MRO) in Python

This project demonstrates how **Method Resolution Order (MRO)** works in the context of **Diamond Inheritance** using Python classes.

## 🧱 Structure

We define four classes:
- `A`: Base class with a `show()` method
- `B` and `C`: Inherit from `A` and override `show()`
- `D`: Inherits from both `B` and `C`

## 💻 Code

```python
class A:
    def show(self):
        print("A's show() method")

class B(A):
    def show(self):
        print("B's show() method")

class C(A):
    def show(self):
        print("C's show() method")

class D(B, C):
    pass

# Create an object of class D and call show()
d = D()
d.show()

# Display the method resolution order
print("MRO:", [cls.__name__ for cls in D.__mro__])





---

### 📘 Summary

This assignment clearly demonstrates how Python resolves methods in multiple inheritance scenarios using MRO. The order of base classes matters!

Would you like to experiment by reversing the inheritance order to `class D(C, B)` to see the change in behavior?
