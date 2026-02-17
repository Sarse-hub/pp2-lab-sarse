# ============================================================================
# Return Values - Functions returning values
# ============================================================================

# Function with return statement
def calculate(a, b, operation):
    """Perform calculation based on operation"""
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b if b != 0 else "Error: Division by zero"

result1 = calculate(10, 5, "add")
result2 = calculate(10, 5, "subtract")
print(f"10 + 5 = {result1}")
print(f"10 - 5 = {result2}")




# Multiple return values
def get_min_max(numbers):
    """Return minimum and maximum values from a list"""
    return min(numbers), max(numbers)

values = [15, 3, 42, 8, 99, 5]
min_val, max_val = get_min_max(values)
print(f"Min: {min_val}, Max: {max_val}")
