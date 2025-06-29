
# Create a function called life_in_weeks() using maths and f-Strings that tells us 
# how many weeks we have left, if we live until 90 years old.
# def life_in_weeks(age):
#     life_in_weeks = (90-age)*52
#     print(f"You have {life_in_weeks} weeks left.")

# life_in_weeks(56)

# You are going to write a function called calculate_love_score() that tests the compatibility between two names.
# To work out the love score between two people: 
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   
# 2. Then check for the number of times the letters in the word LOVE occurs.   
# 3. Then combine these numbers to make a 2 digit number and print it out. 
# e.g. name1 = "Angela Yu" name2 = "Jack Bauer"

# T occurs 0 times; R occurs 1 time; U occurs 2 times; E occurs 2 times 
# Total = 5 
# L occurs 1 time; O occurs 0 times; V occurs 0 times; E occurs 2 times 
# Total = 3 
# Love Score = 53

# def calculate_love_score(name1, name2):
#     names = (name1 + name2).lower()
#     true_count = 0
#     love_count = 0
#     word_1 = "true"
#     word_2  = "love"
    
#     for char in word_1:
#         true_count += names.count(char)
#     for char in word_2:
#         love_count += names.count(char)
            
#     total_score = str(true_count) + str(love_count)
#     print(f"The love score is: {total_score}")
    
# calculate_love_score("Kanye West", "Kim Kardashian")

## Project 8: Caesar Cipher
# The Caesar Cipher is a type of substitution cipher where each letter in the plaintext is shifted a certain number 
# of places down or up the alphabet. For example, with a shift of 1: A would be replaced by B, B would become C, 
# and so on. The end of the alphabet wraps around, so Z becomes A.

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)

alphabet = 'abcdefghijklmnopqrstuvwxyz'
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

# 1. Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# Inside the 'encrypt' function, shift each letter in the 'text' forward in the alphabet by the 'shift' amount.
# Consider what happens if you try to shift z forwards.
def encript(text, shift):
    encripted_text = ""
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift) % len(alphabet)
            encripted_text += alphabet[new_position]
        else:
            encripted_text += char
    print(f"The encoded text is: {encripted_text}")

# 2. Create a function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# Inside the 'decrypt' function, shift each letter in the 'text' backward in the alphabet by the 'shift' amount.
# Consider what happens if you try to shift a when the shift is negative.
def decrypt(text, shift):  
    decrypted_text = ""
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift) % len(alphabet)
            decrypted_text += alphabet[new_position]
        else:
            decrypted_text += char
    print(f"The decoded text is: {decrypted_text}")

# 3. Combine the encrypt() and decrypt() functions into a single function called caesar().
# Use the 'direction' variable to determine whether to encrypt or decrypt the text.
def caesar(text, shift, direction):
    if direction == "encode":
        encript(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Invalid direction. Please choose 'encode' or 'decode'.")

caesar(text, shift, direction)