def pig_latin(word):
    is_capitalize = word[0].isupper()

    word = word.lower()
    if word[0] in 'aeiou':
        pigLatin_word =  f'{word}way'
    else:
        pigLatin_word =  f'{word[1:]}{word[0]}ay'

    if is_capitalize:
        return pigLatin_word.capitalize()
    return pigLatin_word

print(pig_latin('Apple'))