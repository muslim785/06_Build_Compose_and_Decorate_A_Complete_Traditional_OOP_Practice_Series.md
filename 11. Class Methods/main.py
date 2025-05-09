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
print(f"Total books: {Book.total_books}")  # Output: Total books: 2
