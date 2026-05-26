def pig_latin(word):
    if word[0] in 'aeiou':
        return f'{word}way'
    return f'{word[1:]}{word[0]}ay'

def pl_sentence(sentence):
    words = sentence.split()
    output = ''
    for word in words:
       output = output +' '+ pig_latin(word)
    
    return output

print(pl_sentence('this is a test translation'))
    