# enumerate returns pairs of index and value from a list.
animals = ["cat", "dog", "rabbit"]
for idx, animal in enumerate(animals, start=1):
    print(idx, animal)

# zip combines two lists element by element into tuples.
names = ["Alice", "Bob", "Charlie"]
scores = [90, 80, 70]
for name, score in zip(names, scores):
    print(f"{name} -> {score}")

# type conversions 
x = "123" 
print("type(x):", type(x)) #hows the data type of variable x.
print("int:", int(x), "type:", type(int(x))) #converts string x to an integer and shows the result and its type.
print("float:", float(x), "type:", type(float(x))) #converts string x to a float and shows the result and its type.
print("str:", str(123), "type:", type(str(123))) #converts integer 123 to a string and shows the result and its type.
