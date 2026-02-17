# ============================================================================
# Function Arguments - Positional and Default Arguments
# ============================================================================

# Positional arguments
def greet(name, age):
    """Greet a person with their name and age"""
    print(f"Hello, {name}! You are {age} years old.")

greet("Alice", 25)
greet("Bob", 30)




# Default arguments
def welcome(name="Guest", status="user"):
    """Welcome a person with default values"""
    print(f"Welcome, {name}! Status: {status}")

welcome()
welcome("Charlie")
welcome("Diana", "admin")
