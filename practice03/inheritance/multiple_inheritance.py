# ============================================================================
# Multiple Inheritance - Inheriting from multiple parent classes
# ============================================================================

class Flyer:
    """Mixin class - Flyer"""
    def fly(self):
        print("Flying...")

class Swimmer:
    """Mixin class - Swimmer"""
    def swim(self):
        print("Swimming...")

class Diver:
    """Mixin class - Diver"""
    def dive(self):
        print("Diving...")

class Duck(Flyer, Swimmer):
    """Child class inheriting from Flyer and Swimmer"""
    def quack(self):
        print("Quack!")

duck = Duck()
duck.fly()
duck.swim()
duck.quack()

print()

class Penguin(Swimmer, Diver):
    """Child class inheriting from Swimmer and Diver"""
    def waddle(self):
        print("Waddling...")

penguin = Penguin()
penguin.swim()
penguin.dive()
penguin.waddle()
