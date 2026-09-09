import os

def count_lines(filepath):
    try:
        # Read in binary to avoid encoding errors and speed up counting
        with open(filepath, 'rb') as f:
            return sum(1 for _ in f)
    except Exception:
        return 0

total_lines = 0
total_files = 0
ignore_dirs = {'.git', 'node_modules', '__pycache__', 'venv', 'env', '.expo'}

for root, dirs, files in os.walk('.'):
    # Modify dirs in-place to skip ignored directories
    dirs[:] = [d for d in dirs if d not in ignore_dirs]
    for file in files:
        filepath = os.path.join(root, file)
        total_lines += count_lines(filepath)
        total_files += 1

print(f"--- PROJECT STATISTICS ---")
print(f"Total Files: {total_files}")
print(f"Total Lines of Code (LOC): {total_lines:,}")
