name1 = input("What is your name?: ")
name2 = input("What is their name?: ")

true_sum = 0
love_sum = 0

true_sum = sum([name1.count(character) + name2.count(character) for character in "true"])
love_sum = sum([name1.count(character) + name2.count(character) for character in "love"])

total_sum = int(str(true_sum) + str(love_sum))

print(total_sum)


