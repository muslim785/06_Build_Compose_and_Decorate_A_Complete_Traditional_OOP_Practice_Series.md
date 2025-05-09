# Book Class - Class Methods in Python

This Python project demonstrates the use of **class methods** and **class variables** by creating a `Book` class. The class keeps track of the total number of books using a class variable `total_books` and a class method `increment_book_count()` to update the count whenever a new book is added.

## ✅ Features

- **Class variable** `total_books`: Tracks the total number of books created.
- **Class method** `increment_book_count()`: Increments the total count when a new book is instantiated.
- Demonstrates how to use class methods to manipulate class-level data.

## 💻 Full Code

```python
class Book:
    total_books = 0  # Class variable to track total number of books
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        # When a new book is created, increment the total_books count
        Book.increment_book_count()
    
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1  # Increment the class variable total_books

# Example usage:
book1 = Book("To Kill a Mockingbird", "Harper Lee")
book2 = Book("Pride and Prejudice", "Jane Austen")

# Display the total number of books
print(f"Total books: {Book.total_books}")
