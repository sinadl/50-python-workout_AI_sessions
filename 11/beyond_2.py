def vowels_sort(words):
    points = []
    vowels = 'aeiouAEIOU'
    for word in words:
        counts = 0
        for letter in word:
            if letter in vowels:
                counts += 1
        points.append(counts)
    return points
        
words = ["banana", "apple", "sky", "education", "why", "queue"]

sorted_words = sorted(words, key=vowels_sort)
print(sorted_words)