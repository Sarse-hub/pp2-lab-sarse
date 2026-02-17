# ============================================================================
# Lambda Basics - Lambda syntax and basic usage
# ============================================================================

# Simple lambda function to square a number
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")
print(f"Square of 10: {square(10)}")

# Lambda with multiple arguments
add = lambda x, y: x + y
print(f"5 + 3 = {add(5, 3)}")
