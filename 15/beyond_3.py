import os
def word_lengths(filename):
    counts = {}

    with open(filename) as f:
        for line in f:
            words = line.split()

            for word in words:
                length = len(word)

                if length not in counts:
                    counts[length] = 0

                counts[length] += 1

    return counts

path = os.path.join(os.path.dirname(__file__), "words.txt")
result = word_lengths(path)

for length, count in sorted(result.items()):
    print(f"{length} letters: {count}")
