# ============================================================================
# Python Iterators and Generators - Practice Exercises
# ============================================================================

# ============================================================================
# 1. ITERATORS: iter() and next()
# ============================================================================

# Creating an iterator from a list
my_list = [1, 2, 3, 4, 5]
my_iterator = iter(my_list)

print("Using iter() and next():")
print(next(my_iterator))  # Output: 1
print(next(my_iterator))  # Output: 2
print(next(my_iterator))  # Output: 3

# ============================================================================
# 2. LOOP THROUGH ITERATOR
# ============================================================================

print("\nLooping through iterator:")
my_iterator = iter(my_list)
for item in my_iterator:
    print(item, end=" ")
print()

# ============================================================================
# 3. CREATE YOUR OWN ITERATOR
# ============================================================================

class MyIterator:
    """Custom iterator class"""
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current
        else:
            raise StopIteration

print("\nCustom iterator:")
my_iter = MyIterator(5)
for num in my_iter:
    print(num, end=" ")
print()

# ============================================================================
# 4. GENERATORS: yield keyword
# ============================================================================

def simple_generator():
    """Simple generator function using yield"""
    yield 1
    yield 2
    yield 3

print("\nGenerator with yield:")
gen = simple_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3

# ============================================================================
# 5. GENERATOR FUNCTIONS
# ============================================================================

def fibonacci_generator(n):
    """Generator function for Fibonacci sequence"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

print("\nFibonacci generator:")
fib_gen = fibonacci_generator(10)
for num in fib_gen:
    print(num, end=" ")
print()

# ============================================================================
# 6. GENERATOR EXPRESSIONS
# ============================================================================

# Generator expression (similar to list comprehension but with parentheses)
squares_gen = (x**2 for x in range(1, 6))

print("\nGenerator expression:")
for square in squares_gen:
    print(square, end=" ")
print()

# Memory efficient: generator vs list comprehension
print("\nMemory comparison:")
import sys

# List comprehension - stores all values in memory
list_comp = [x**2 for x in range(1000)]
print(f"List comprehension memory: {sys.getsizeof(list_comp)} bytes")

# Generator expression - generates values on demand
gen_exp = (x**2 for x in range(1000))
print(f"Generator expression memory: {sys.getsizeof(gen_exp)} bytes")

# ============================================================================
# 7. PRACTICAL EXAMPLES
# ============================================================================

# Generator for reading large files line by line
def read_large_file(file_path):
    """Generator to read large files efficiently"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        yield "File not found"

# Example usage (would work with actual file)
print("\nFile reading generator example:")
# for line in read_large_file('large_file.txt'):
#     print(line)

# Infinite generator with caution
def infinite_counter():
    """Infinite generator - use with caution!"""
    n = 0
    while True:
        yield n
        n += 1

print("\nInfinite generator (first 5 values):")
counter = infinite_counter()
for _ in range(5):
    print(next(counter), end=" ")
print()

# ============================================================================
# 8. ADVANCED GENERATOR PATTERNS
# ============================================================================

# Generator with send() method
def accumulator():
    """Generator that can receive values via send()"""
    total = 0
    while True:
        value = (yield total)
        if value is not None:
            total += value

print("\nGenerator with send():")
acc = accumulator()
next(acc)  # Prime the generator
print(f"Total: {acc.send(10)}")  # Send 10, get total
print(f"Total: {acc.send(5)}")   # Send 5, get total
print(f"Total: {acc.send(3)}")   # Send 3, get total

# Close generator
acc.close()

print("\n=== Iterators and Generators Practice Complete ===")