
import hashlib
from pathlib import Path

print("=== File Integrity Checker ===")

file_path = Path(input("Enter file name: "))

if not file_path.is_file():
    print("File not found!")
else:
    file_hash = hashlib.sha256(file_path.read_bytes()).hexdigest()

    hash_file = Path(str(file_path) + ".sha256")

    if hash_file.exists():
        saved_hash = hash_file.read_text().strip()

        if file_hash == saved_hash:
            print("PASS: File has not changed.")
        else:
            print("ALERT: File has been modified!")
    else:
        hash_file.write_text(file_hash)
        print("Baseline hash saved.")
