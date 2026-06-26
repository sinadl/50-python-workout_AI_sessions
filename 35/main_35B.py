from main_35A import gematria_dict

GEMATRIA = gematria_dict()

def gematria_for(word):
    return sum(GEMATRIA.get(char,0) for char in word) 

def gematria_equal_words(input_word):
    word_score = gematria_for(input_word)
    return [word.strip() for word in open('/usr/share/dict/words')
            if gematria_for(word) == word_score]
    
print(gematria_equal_words('sina'))