WORDS = ['this', 'is', 'an', 'elementary', 'test', 'example']

def most_repeating_word(words):
    best_word = ''
    best_count = 0

    for word in words:
        letter_counts = {}

        for letter in word:
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1

        current_max = 0
        for letter in letter_counts:
            if letter_counts[letter] > current_max:
                current_max = letter_counts[letter]

        if current_max > best_count:
            best_count = current_max
            best_word = word

    return best_word

print(most_repeating_word(WORDS))
