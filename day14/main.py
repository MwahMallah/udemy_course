import os, random, art, game_data

END_GAME = -1

def homescreen():
    score = 0

    while score != END_GAME:
        os.system("clear")
        print(art.logo)
        if score != 0:
            print(f"You're right! Current score: {score}")
        score = game(score)

def game(score: int) -> int:
    person_a = random.choice(game_data.data)
    person_b = random.choice(game_data.data)
    
    print(f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}")
    print(art.vs)
    print(f"Compare B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}")

    if input("Who has more followers? Type 'A' or 'B': ") == 'A':
        guessed_person = person_a
        other_person = person_b
    else:
        guessed_person = person_b
        other_person = person_a

    if guessed_person['follower_count'] >= other_person['follower_count']:
        return score + 1
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        print(f"{other_person['name']}'s follower count is {other_person['follower_count']}, {guessed_person['name']}'s follower count is {guessed_person['follower_count']}")
        return END_GAME
    
homescreen()