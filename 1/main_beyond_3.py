import random

def word_guessing_game():
    # mac/linux users only
    with open('/usr/share/dict/words', 'r') as f:

        all_words = [word.strip().lower() for word in f.readlines()]
        filtered_words = [w for w in all_words if 2 <= len(w) <= 5]

    answer = random.choice(filtered_words)
    while True:
        guess = input(f"Guess the word(only 2 to 5 letters words): ")

        
        if guess == answer:
            print('you guess exactly right') 
            break
        elif guess > answer:
            print(f'{guess} is earlier in dic') 
          
        else :
            print(f'{guess} is later in dic') 
            

word_guessing_game()


