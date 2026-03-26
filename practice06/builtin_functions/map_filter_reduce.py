from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map: square each number
squares = list(map(lambda x: x * x, numbers))
print("squares:", squares)

# filter: only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("evens:", evens)

# reduce: sum of numbers
total = reduce(lambda a, b: a + b, numbers)
print("sum via reduce:", total)

# built-in aggregations
print("len:", len(numbers))
print("min:", min(numbers))
print("max:", max(numbers))
print("sum:", sum(numbers))
