
def ubbi_dubbi(word):
    is_capitalize = word[0].isupper()
    result = []
    output = ''
    
    for letter in word.lower():
        if letter in 'aeiou':
            result.extend(['u','b'])
        result.append(letter)
        
    
    if is_capitalize:
        result[0] = result[0].upper()
        
        
    output = ''.join(result)
    return output
        
print(ubbi_dubbi('Apple'))