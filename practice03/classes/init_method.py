# ============================================================================
# Init Method - The constructor method __init__()
# ============================================================================

class Car:
    """A Car class with constructor"""
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year
    
    def display_info(self):
        print(f"{self.year} {self.color} {self.brand}")

car1 = Car("Tesla", "red", 2023)
car1.display_info()

car2 = Car("BMW", "blue", 2022)
car2.display_info()
