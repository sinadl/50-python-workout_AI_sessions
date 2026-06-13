import os

letter_counts = {}

directory = "20"

for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)

    if os.path.isfile(filepath):
        with open(filepath, "r") as f:
            for line in f:
                for char in line.lower():
                    if char.isalpha():
                        letter_counts[char] = letter_counts.get(char, 0) + 1

top_five = sorted(
    letter_counts.items(),
    key=lambda item: item[1],
    reverse=True
)[:5]

print("Top 5 letters:")
for letter, count in top_five:
    print(f"{letter}: {count}")