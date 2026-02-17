# ============================================================================
# Class Methods - Instance methods and the parameter self
# ============================================================================

class Person:
    """Person class with instance methods"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        """Instance method using self"""
        print(f"Hi, I'm {self.name} and I'm {self.age} years old")
    
    def have_birthday(self):
        """Instance method that modifies self"""
        self.age += 1
        print(f"{self.name} just turned {self.age}!")
    
    def is_adult(self):
        """Instance method returning boolean"""
        return self.age >= 18

person = Person("John", 30)
person.introduce()
person.have_birthday()
print(f"Is {person.name} an adult? {person.is_adult()}")
