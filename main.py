#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

import pandas as pd
a = pd.read_csv("alphabet.csv")

phonetic_dict = {row.letter:row.code for (index,row) in a.iterrows()}
# # print(phonetic_dict)

# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# c = input("Enter a word: ").upper()
# b = [phonetic_dict[letter] for letter in c]
# print(b)
