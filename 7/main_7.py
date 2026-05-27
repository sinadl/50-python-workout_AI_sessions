def ubbi_dubbi(word):
    result = []
    output = ''
    for letter in word:
        if letter in 'aeiou':
            result.extend(['u','b'])
        result.append(letter)
    output = ''.join(result)
    return output
        
print(ubbi_dubbi('apple'))