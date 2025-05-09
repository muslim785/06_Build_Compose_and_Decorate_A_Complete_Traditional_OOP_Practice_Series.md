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
