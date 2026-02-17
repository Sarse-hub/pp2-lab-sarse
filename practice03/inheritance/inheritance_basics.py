# ============================================================================
# Inheritance Basics - Parent and child class relationships
# ============================================================================

class Animal:
    """Parent class - Animal"""
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    """Child class - Dog inherits from Animal"""
    def speak(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    """Child class - Cat inherits from Animal"""
    def speak(self):
        print(f"{self.name} says Meow!")

dog = Dog("Buddy")
dog.speak()

cat = Cat("Whiskers")
cat.speak()
