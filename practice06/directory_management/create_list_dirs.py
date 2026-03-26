import os #Import the standard os module for filesystem operations.
from pathlib import Path #Import the Path class from the pathlib module for object-oriented filesystem paths.

root = Path("Practice6_demo") #Create a Path object representing the root directory "Practice6_demo".

# Create nested directories (makedirs equivalent)
nested = root / "level1" / "level2" #Build nested path
nested.mkdir(parents=True, exist_ok=True) #Make directories recursively; no error if they already exist.
print(f"Created nested directories: {nested}")

# List files and folders
print("Directory listing of root")
for p in root.iterdir():#Iterate items directly inside Practice6_demo and print them.
    print(p)

# Create sample files for extension search
for ext_file in [root / "a.txt", root / "b.py", root / "c.txt"]: #Create sample files with different extensions.
    ext_file.write_text("demo")

# Find files by extension
print("Text files:")
for p in root.rglob("*.txt"): #Recursively find all .txt files in Practice6_demo and print their paths.
    print(p)
