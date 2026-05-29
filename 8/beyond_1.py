
def sort_comb(words):
    words = sorted(words.split(), key=str.casefold)
    result = ''
    for word in words:
        if result:  
            result += ',' + word
        else:
            result = word 
    return result
    
    
print(sort_comb('Tom Dick Harry'))