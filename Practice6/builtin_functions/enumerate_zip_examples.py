# enumerate
animals = ["cat", "dog", "rabbit"]
for idx, animal in enumerate(animals, start=1):
    print(idx, animal)

# zip
names = ["Alice", "Bob", "Charlie"]
scores = [90, 80, 70]
for name, score in zip(names, scores):
    print(f"{name} -> {score}")

# type conversions
x = "123"
print("type(x):", type(x))
print("int:", int(x), "type:", type(int(x)))
print("float:", float(x), "type:", type(float(x)))
print("str:", str(123), "type:", type(str(123)))
