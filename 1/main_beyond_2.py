import random

def guessing_game():
    answer = random.randint(0,100)
    base = random.randint(2, 16)



    c = 0
    while c < 3:
        user_answer = input(f"Guess the number (in base {base}): ")
        try:
            guess = int(user_answer, base)
        except ValueError:
            print(f"Invalid input! Please enter a valid number for base {base}.")
            continue

        if guess == answer:
            print('you guess exactly right') 
            break
        elif guess > answer:
            print(f'{guess} is too high') 
            c = c+1
        else :
            print(f'{guess} is too low') 
            c = c+1
    if c ==3 :
        print('ran out of guess!!')
guessing_game()


