import art 
print(art.logo)

import random

def homescreen():
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    chosed_difficulty = False
    while not chosed_difficulty:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if difficulty == "easy":
            chosed_difficulty = True
            game(answer=answer, lifes=10)
        elif difficulty == "hard":
            chosed_difficulty = True
            game(answer=answer, lifes=5)
        else: 
            continue

def game(answer: int, lifes: int) -> None:
    while lifes != 0:
        print(f"You have {lifes} attempts remaining to guess the number.")
        lifes -= 1
        guessed_number = int(input("Make a guess: "))
        if guessed_number == answer:
            print(f"You got it! The answer was {answer}.")
            return
        elif guessed_number > answer:
            print("Too high")
        else:
            print("Too low")
    print(f"You've run out of guesses, you lose. Answer was {answer}")

homescreen()