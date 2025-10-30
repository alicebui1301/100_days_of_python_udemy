import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
alphabet_df = pandas.read_csv("intermediate/26_nato_alphabet/nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in alphabet_df.iterrows()}   

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
input_word = input("Enter a word: ").upper()
output_list = [nato_dict[letter] for letter in input_word]
print(output_list)
