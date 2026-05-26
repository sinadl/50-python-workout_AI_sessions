import string

def pig_latin(word):
    is_capitalize = word[0].isupper()
    counter = 0
    vowel_letter = 'aeiou'
    for letter in word.lower():
        if letter in vowel_letter:
            counter += 1
            vowel_letter.replace(letter,'',1)


    if word[-1] in string.punctuation:
        punct = word[-1]
        word = word[:-1]

    word = word.lower()
    if counter >=2:
        pigLatin_word =  f'{word}way'
    else:
        pigLatin_word =  f'{word[1:]}{word[0]}ay'

    if is_capitalize:
        pigLatin_word =  pigLatin_word.capitalize()
    return pigLatin_word + punct

print(pig_latin('Apple#'))