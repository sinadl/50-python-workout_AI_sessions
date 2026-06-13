import os
def wordcount(filename):
    with open(filename, "r") as file:
        text = file.read()

    chars = len(text)

    words = text.split()
    word_count = len(words)

    lines = len(text.splitlines())

    unique_words = len(set(words))

    print(f"Characters: {chars}")
    print(f"Words: {word_count}")
    print(f"Lines: {lines}")
    print(f"Unique words: {unique_words}")


path = os.path.join(os.path.dirname(__file__), "sample.txt")
wordcount(path)