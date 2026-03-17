from pathlib import Path

file_path = Path("sample_text.txt")

# Write mode (w) creates or truncates
file_path.write_text("Apple\nBanana\nCherry\n", encoding="utf-8")
print("Written sample_text.txt")

# Append mode (a)
with file_path.open("a", encoding="utf-8") as f:
    f.write("Date\nElderberry\n")
print("Appended new lines")

# Verify contents
print("Current file content:")
print(file_path.read_text(encoding="utf-8"))
