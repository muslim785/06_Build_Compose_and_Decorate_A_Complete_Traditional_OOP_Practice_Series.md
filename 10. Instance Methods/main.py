class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking! Woof Woof!")

# Example usage:
dog1 = Dog("Buddy", "Golden Retriever")
dog1.bark()  # Output: Buddy is barking! Woof Woof!
