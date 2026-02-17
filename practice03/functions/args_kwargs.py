# ============================================================================
# Args and Kwargs - Variable Arguments
# ============================================================================

# *args - Variable positional arguments
def sum_all(*args):
    """Sum all provided arguments"""
    total = 0
    for num in args:
        total += num
    return total

print(f"Sum of 1, 2, 3: {sum_all(1, 2, 3)}")
print(f"Sum of 1, 2, 3, 4, 5: {sum_all(1, 2, 3, 4, 5)}")




# **kwargs - Variable keyword arguments
def print_info(**kwargs):
    """Print key-value pairs"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Eve", age=28, city="New York")
print_info(product="Laptop", price=999, brand="Dell")
