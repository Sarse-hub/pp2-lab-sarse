from pathlib import Path

# Define file path
file_path = Path("sample_text.txt")

# Ensure file exists for reading demo
if not file_path.exists():
    file_path.write_text("Line 1\nLine 2\nLine 3\n")

# read() entire content
text = file_path.read_text()
print("=== read() ===")
print(text)

# readline() line by line
print("=== readline() ===")
with file_path.open("r", encoding="utf-8") as f:
    print(repr(f.readline()))
    print(repr(f.readline()))

# readlines() into list
print("=== readlines() ===")
with file_path.open("r", encoding="utf-8") as f:
    lines = f.readlines()
print(lines)
