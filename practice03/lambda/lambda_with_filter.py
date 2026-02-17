# ============================================================================
# Lambda with Filter - Using lambda with filter() for selection
# ============================================================================

# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"All numbers: {numbers}")
print(f"Even numbers: {even_numbers}")




# Filter numbers greater than 5
greater_than_5 = list(filter(lambda x: x > 5, numbers))
print(f"Numbers greater than 5: {greater_than_5}")
