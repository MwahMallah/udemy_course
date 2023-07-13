import art
import os

print(art.logo)
print("Welcome to the secret auction program.")

other_players = True
players = {}

os.system()

while other_players:
    name = input('What is your name?: ')
    bid = int(input("What's your bid?: "))
    players[name] = bid

    if input("Are there any other bidders? Type 'yes' or 'no': ")  != 'yes':
        other_players = False
    os.system('clear')

winner = max(players, key=players.get)

print(f"The winner is {winner} with a bid of {players[winner]}")


os.system()