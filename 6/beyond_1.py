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

def multiline_file(filename):
    output = ''
    with open(f'/Users/sina/Desktop/mentoring_data/50-python-workout_AI_sessions/6/{filename}','r') as file:
        for n,line in enumerate(file):
            sentence = line.split()
            output = output +' '+ sentence[n]
    return pl_sentence(output)

print(multiline_file('textfile.txt'))
    