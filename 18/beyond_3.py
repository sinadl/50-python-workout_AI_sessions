import os

vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

path = os.path.join(os.path.dirname(__file__), "textfile.txt")

with open(path, "r") as file:
    for line in file:
        line = line.lower()

        for word in line:

               if word in  vowels:
                    vowels[word] += 1
    
print(vowels)
    
    