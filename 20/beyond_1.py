import os
filename = input("Enter filename: ")
search_words = input("Enter words to count: ").split()

path = os.path.join(os.path.dirname(__file__), filename)
counts = {word: 0 for word in search_words}

with open(path, "r") as file:
    for line in file:
        words = line.split()

        for word in words:
            if word in counts:
                counts[word] += 1

print(counts)