
def find_last(words):
    words = sorted(words.split(), key=str.casefold)
    result = words[len(words)-1]
    return result
    
    
print(find_last('Tom Dick Harry'))