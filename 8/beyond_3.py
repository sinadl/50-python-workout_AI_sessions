
def find_last(words):
    result = max(words.split(),key=len)
    
    return result
    
    
print(find_last('Tom Dick Harry'))