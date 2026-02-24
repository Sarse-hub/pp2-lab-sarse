# ============================================================================
# Python Math and Random Operations - Practice Exercises
# ============================================================================

import math
import random

# ============================================================================
# 1. BUILT-IN MATHEMATICAL FUNCTIONS
# ============================================================================

print("=== Built-in Mathematical Functions ===")

numbers = [3.7, -5.2, 10, 2.1, -8.9]

print(f"Numbers: {numbers}")
print(f"Minimum: {min(numbers)}")
print(f"Maximum: {max(numbers)}")
print(f"Absolute value of -5.2: {abs(-5.2)}")
print(f"Round 3.7: {round(3.7)}")
print(f"Round 3.14159 to 2 decimals: {round(3.14159, 2)}")
print(f"Power (2^3): {pow(2, 3)}")
print(f"Power (3^2): {pow(3, 2)}")

# ============================================================================
# 2. MATH MODULE FUNCTIONS
# ============================================================================

print("\n=== Math Module Functions ===")

# Square root
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Square root of 2: {math.sqrt(2):.4f}")

# Ceiling and floor
print(f"Ceiling of 3.2: {math.ceil(3.2)}")
print(f"Floor of 3.8: {math.floor(3.8)}")
print(f"Ceiling of -3.2: {math.ceil(-3.2)}")
print(f"Floor of -3.8: {math.floor(-3.8)}")

# Trigonometric functions (in radians)
angle_rad = math.pi / 4  # 45 degrees
print(f"Sine of π/4: {math.sin(angle_rad):.4f}")
print(f"Cosine of π/4: {math.cos(angle_rad):.4f}")
print(f"Tangent of π/4: {math.tan(angle_rad):.4f}")

# Convert degrees to radians
angle_deg = 45
angle_rad = math.radians(angle_deg)
print(f"45 degrees in radians: {angle_rad:.4f}")

# Convert radians to degrees
back_to_deg = math.degrees(angle_rad)
print(f"Back to degrees: {back_to_deg}")

# ============================================================================
# 3. MATH CONSTANTS
# ============================================================================

print("\n=== Math Constants ===")

print(f"π (pi): {math.pi:.6f}")
print(f"e (Euler's number): {math.e:.6f}")
print(f"τ (tau, 2π): {math.tau:.6f}")

# ============================================================================
# 4. RANDOM MODULE BASICS
# ============================================================================

print("\n=== Random Module Basics ===")

# Random float between 0 and 1
print(f"Random float (0-1): {random.random():.4f}")

# Random float in range
print(f"Random float (1-10): {random.uniform(1, 10):.4f}")

# Random integer
print(f"Random integer (1-10): {random.randint(1, 10)}")

# Random choice from sequence
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(f"Random fruit: {random.choice(fruits)}")

# Random sample (without replacement)
print(f"Random sample of 3 fruits: {random.sample(fruits, 3)}")

# ============================================================================
# 5. RANDOM: SHUFFLE AND MORE
# ============================================================================

print("\n=== Shuffle and Advanced Random ===")

# Shuffle a list
cards = ['Ace', 'King', 'Queen', 'Jack', '10']
print(f"Original cards: {cards}")
random.shuffle(cards)
print(f"Shuffled cards: {cards}")

# Random choices (with replacement)
print(f"Random choices (with replacement): {random.choices(fruits, k=5)}")

# Weighted random choice
weights = [0.1, 0.2, 0.3, 0.2, 0.2]  # Different probabilities
print(f"Weighted choice: {random.choices(fruits, weights=weights, k=3)}")

# ============================================================================
# 6. PRACTICAL MATH EXAMPLES
# ============================================================================

print("\n=== Practical Math Examples ===")

# Calculate distance between two points
def euclidean_distance(x1, y1, x2, y2):
    """Calculate Euclidean distance between two points"""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

distance = euclidean_distance(0, 0, 3, 4)
print(f"Distance between (0,0) and (3,4): {distance}")

# Calculate circle area
def circle_area(radius):
    """Calculate area of a circle"""
    return math.pi * radius ** 2

area = circle_area(5)
print(f"Area of circle with radius 5: {area:.2f}")

# Generate random password
def generate_password(length=8):
    """Generate a random password"""
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

print(f"Random password: {generate_password()}")

# ============================================================================
# 7. STATISTICAL FUNCTIONS
# ============================================================================

print("\n=== Statistical Functions ===")

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using statistics module (Python 3.4+)
import statistics

print(f"Data: {data}")
print(f"Mean: {statistics.mean(data):.2f}")
print(f"Median: {statistics.median(data)}")
print(f"Mode: {statistics.mode(data)}")
print(f"Standard deviation: {statistics.stdev(data):.2f}")
print(f"Variance: {statistics.variance(data):.2f}")

# ============================================================================
# 8. ADVANCED MATH OPERATIONS
# ============================================================================

print("\n=== Advanced Math Operations ===")

# Factorial
print(f"Factorial of 5: {math.factorial(5)}")

# Greatest common divisor
print(f"GCD of 48 and 18: {math.gcd(48, 18)}")

# Logarithms
print(f"Natural log of e: {math.log(math.e):.6f}")
print(f"Log base 10 of 100: {math.log10(100)}")
print(f"Log base 2 of 8: {math.log2(8)}")

# Exponential
print(f"e^2: {math.exp(2):.6f}")
print(f"2^3: {math.pow(2, 3)}")

# ============================================================================
# 9. RANDOM NUMBER GENERATION PATTERNS
# ============================================================================

print("\n=== Random Number Generation Patterns ===")

# Seed for reproducible results
random.seed(42)
print("With seed 42:")
for _ in range(3):
    print(f"Random number: {random.randint(1, 100)}")

# Reset seed and generate same sequence
random.seed(42)
print("Same seed 42 (should be identical):")
for _ in range(3):
    print(f"Random number: {random.randint(1, 100)}")

# Generate random coordinates
def random_point_in_circle(radius):
    """Generate random point inside a circle"""
    angle = random.uniform(0, 2 * math.pi)
    r = radius * math.sqrt(random.random())
    x = r * math.cos(angle)
    y = r * math.sin(angle)
    return x, y

print(f"Random point in unit circle: {random_point_in_circle(1)}")

print("\n=== Math and Random Practice Complete ===")