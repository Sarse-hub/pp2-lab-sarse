import shutil
from pathlib import Path

original = Path("sample_text.txt")
backup = Path("sample_text_backup.txt")

# Copy file
if original.exists():
    shutil.copy2(original, backup)
    print(f"Copied {original} to {backup}")
else:
    print("Original file missing. Run write_files first.")

# Delete backup safely
if backup.exists():
    backup.unlink()
    print(f"Deleted backup {backup}")
else:
    print("Backup does not exist, nothing to delete")
