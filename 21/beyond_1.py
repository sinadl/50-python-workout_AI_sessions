import os
import hashlib

directory = input("Enter directory: ")

for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)

    if os.path.isfile(filepath):
        with open(filepath, "rb") as f:
            data = f.read()

        md5_hash = hashlib.md5(data).hexdigest()

        print(f"{filename}: {md5_hash}")