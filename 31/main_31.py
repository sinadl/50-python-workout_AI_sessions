def plword(word):
    if word[0] in "aeiou":
        return word + "way"
    else:
        return word[1:] + word[0] + "ay"


def pig_latin_file(filename):
    with open(filename) as f:
        return " ".join(
            plword(word)
            for line in f
            for word in line.split()
        )
        
        
print(pig_latin_file('31/input.txt'))