# ============================================================================
# Class Definition - Basic class definition and object creation
# ============================================================================

class Dog:
    """A simple Dog class"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} says Woof!")

dog1 = Dog("Buddy", 3)
dog1.bark()
print(f"Dog's name: {dog1.name}, Age: {dog1.age}")

dog2 = Dog("Max", 5)
dog2.bark()
