import random

names_string = input("Input all people: ")

names = names_string.split(", ")

print(names[random.randint(0, len(names) - 1)])
