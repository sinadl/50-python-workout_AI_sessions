WORDS = ['this', 'is', 'bananananan', 'elementary', 'test', 'example']

def most_repeating_vowels(words):
    best_word = ''
    best_count = 0
    vowels = 'aeiouAEIOU'
    result = {}

    for word in words:
        letter_counts = 0
        
        for letter in word:
            if letter in vowels:
                letter_counts += 1

        if word in result:
            result[word] += letter_counts
        else:
            result[word] = letter_counts
        
        current_max = 0
        result_word = ''
        for word in result:
            if result[word] > current_max:
                current_max = result[word]
                result_word = word


    return current_max,result_word

print(most_repeating_vowels(WORDS))
