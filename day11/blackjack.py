cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

import art
print(art.logo)

def homescreen():
    ready_to_play = False
    print("\n")
    while not ready_to_play:
        if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
            ready_to_play = True
            game()
            homescreen()

def print_result(player_cards: list, computer_cards: list):
    print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")

import random

def game():
    players_cards = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards), random.choice(cards)]

    print(f"Your cards: {players_cards}, current score: {sum(players_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")

    if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
        players_cards.append(random.choice(cards))
        if players_cards[2] == 11 and sum(players_cards) > 21:
            players_cards[2] = 1

    if sum(computer_cards) < 17:
        computer_cards.append(random.choice(cards))
        if computer_cards[2] == 11 and sum(computer_cards) > 21:
            computer_cards[2] = 1

    if sum(players_cards) > 21 or (sum(players_cards) < sum(computer_cards) and sum(computer_cards) <= 21):
        print_result(players_cards, computer_cards)
        print("You lose 😭")

    elif sum(computer_cards) > 21 or sum(players_cards) > sum(computer_cards):
        print_result(players_cards, computer_cards)
        print("You win 😁")

    else:
        print_result(players_cards, computer_cards)
        print("Draw!")

homescreen()