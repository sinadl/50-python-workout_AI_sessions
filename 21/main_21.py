import os 

def find_longest_word(filename):
    with open(filename,'r') as f:
        longest_word=''
        for line in f:
            words = line.split()
            for word in words:
                if len(word) > len(longest_word):
                    longest_word = word
    return longest_word,len(longest_word)
    
def find_longest_words(directory):
    letter_counts = {}
    
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        if os.path.isfile(filepath):
            with open(filepath, "r") as f:
                words = []
                for line in f:
                    words += line.split()
                    
                longest = max(words, key=len)
                letter_counts[filename] = longest

    return letter_counts
    
    
path = os.path.join(os.path.dirname(__file__), "longest.txt")
print(find_longest_word(path))

directory = "20"
print(find_longest_words(directory))