def largest_word(file_obj):
    largest = ""
    
    for line in file_obj:
        words = line.split()
        for word in words:
            if len(word) > len(largest):
                largest = word
    
    return largest

# test case
with open(f'/Users/sina/Desktop/mentoring_data/50-python-workout_AI_sessions/6/textfile.txt','r') as f:
    print(largest_word(f))