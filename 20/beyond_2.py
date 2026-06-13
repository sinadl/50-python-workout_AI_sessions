import os

file_sizes = {}
path = os.path.dirname(os.path.abspath(__file__))
for filename in os.listdir(path):
    if os.path.isfile(filename):
        file_sizes[filename] = os.stat(filename).st_size

print(file_sizes)


