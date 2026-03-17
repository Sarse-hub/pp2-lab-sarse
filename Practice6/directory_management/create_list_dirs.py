import os
from pathlib import Path

root = Path("Practice6_demo")

# Create nested directories (makedirs equivalent)
nested = root / "level1" / "level2"
nested.mkdir(parents=True, exist_ok=True)
print(f"Created nested directories: {nested}")

# List files and folders
print("Directory listing of root")
for p in root.iterdir():
    print(p)

# Create sample files for extension search
for ext_file in [root / "a.txt", root / "b.py", root / "c.txt"]:
    ext_file.write_text("demo")

# Find files by extension
print("Text files:")
for p in root.rglob("*.txt"):
    print(p)
