# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas
df = pandas.read_csv("nato_phonetic_alphabet.csv")
letter_dict = {row.letter:row.code for _, row in df.iterrows()}

sentence = input("Enter you message: ")
sentence_list = [letter_dict[letter.upper()] for letter in sentence]
print(sentence_list)