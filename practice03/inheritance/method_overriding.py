# ============================================================================
# Method Overriding - Override parent methods in child classes
# ============================================================================

class Shape:
    """Parent class - Shape"""
    def __init__(self, name):
        self.name = name
    
    def area(self):
        """This method will be overridden in child classes"""
        pass

class Rectangle(Shape):
    """Child class - Rectangle overrides area method"""
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height
    
    def area(self):
        """Overridden method"""
        return self.width * self.height

class Circle(Shape):
    """Child class - Circle overrides area method"""
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    
    def area(self):
        """Overridden method"""
        import math
        return math.pi * self.radius ** 2

rectangle = Rectangle("Rectangle", 5, 10)
print(f"{rectangle.name} area: {rectangle.area()}")

circle = Circle("Circle", 5)
print(f"{circle.name} area: {circle.area():.2f}")
