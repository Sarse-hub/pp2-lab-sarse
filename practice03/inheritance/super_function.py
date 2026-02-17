# ============================================================================
# Super Function - Using super() to call parent methods
# ============================================================================

class Vehicle:
    """Parent class - Vehicle"""
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    def display(self):
        print(f"Brand: {self.brand}, Color: {self.color}")

class Car(Vehicle):
    """Child class - Car inherits from Vehicle"""
    def __init__(self, brand, color, car_type):
        super().__init__(brand, color)  # Call parent constructor
        self.car_type = car_type
    
    def display(self):
        super().display()  # Call parent method
        print(f"Type: {self.car_type}")

car = Car("Toyota", "blue", "Sedan")
car.display()
