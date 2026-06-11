import os

extensions = set()

for filename in os.listdir('.'):
    name, ext = os.path.splitext(filename)

    if ext:
        extensions.add(ext)

print("Extensions found:")
for ext in sorted(extensions):
    print(ext)