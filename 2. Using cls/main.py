class Counter:
    # Class variable to keep track of the number of objects
    count = 0

    def __init__(self):
        # Every time a new object is created, increment the count
        Counter.count += 1

    @classmethod
    def display_count(cls):
        # Class method to display the current count of objects
        print(f"Number of objects created: {cls.count}")

# Example usage:
counter1 = Counter()
counter2 = Counter()
counter3 = Counter()
counter4 = Counter()
counter5 = Counter()

# Display the count of objects created
Counter.display_count()  # Should print: Number of objects created: 5
