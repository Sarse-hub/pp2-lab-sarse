import shutil
from pathlib import Path

src_dir = Path("Practice6_demo")
dst_dir = Path("Practice6_demo") / "moved"
dst_dir.mkdir(parents=True, exist_ok=True)

# Move a file
src_file = src_dir / "a.txt"
if src_file.exists():
    shutil.move(str(src_file), str(dst_dir / src_file.name))
    print(f"Moved {src_file} to {dst_dir}")
else:
    print("Source file not found for move")

# Copy another file in place
cpy_src = src_dir / "b.py"
cpy_dst = dst_dir / "b_copy.py"
if cpy_src.exists():
    shutil.copy2(cpy_src, cpy_dst)
    print(f"Copied {cpy_src} to {cpy_dst}")
else:
    print("Source file not found for copy")
