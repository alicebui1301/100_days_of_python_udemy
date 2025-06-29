# Project 7: Hangman Game
# Create a hangman game where the player has to guess a word by guessing letters one at a time.
# The player has a limited number of lives, and they lose a life for each incorrect guess.
# The game ends when the player either guesses the word or runs out of lives.

### STEP 1 - Picking a Random Words and Checking Answers
# 1.1 - Randomly select a word from a list of words. Assign it to a variable called `chosen_word` and print it out.
# 1.2 - Ask the player to guess a letter. Assign their answer to a variable called `guess` and convert it to lowercase.
# 1.3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right!" if it is, otherwise print "Wrong!".

# word_list = ["ardvark", "baboon", "camel"]
# from mimetypes import guess_extension
# import random 
# chosen_word = random.choice(word_list)
# print(f"Chosen word is: {chosen_word}")

# guess = input("Guess a letter: ").lower()
# if guess in chosen_word:
#     print("Right!")
# else:
#     print("Wrong!")

### STEP 2 - Replacing Blanks with Guesses
# 2.1 - Create a list called "placeholders" with the same number of blanks as the chosen_word. Each blank should be represented by "_".

# placeholders = ["_" for _ in chosen_word]
# print(f"Placeholders: {placeholders}")

# 2.2 - Create a list called `display` that puts the guessed letters in the correct positions in the placeholders list. 
# If a letter has not been guessed yet, it should remain as "_". Print the display list as a string.

# display = placeholders
# for index, letter in enumerate(chosen_word):
#         if letter == guess:
#             display[index] = letter
# print(f"Display: {''.join(display)}")

### STEP 3 - Checking if the Player has Won
# 3.1 - Use a while loop to let the player guess again.
# 3.2 - Change the for loop so that you keep the previous code that checks if the letter is in the chosen_word, 
# but also check if the player has won by comparing the display list to the chosen_word. If they match, print "You win!" and break out of the loop.

# game_over = False
# placeholders = ["_" for _ in chosen_word]
# while not game_over:
#     guess = input("Guess a letter: ").lower()
#     correct_letters = []
#     for index, letter in enumerate(chosen_word):
#         if letter == guess:
#             placeholders[index] = letter
#             correct_letters.append(letter)
#             print("Right!")
#         elif letter in correct_letters:
#             placeholders[index] = letter
#     print(f"Display: {''.join(placeholders)}")
#     if "_" not in placeholders:
#         print("You win!")
#         game_over = True

### STEP 4 - Keeping Track of the Player's Lives
# 4.1 - Add a variable called `lives` and set it to 6. This will keep track of the number of lives the player has.
# 4.2 - If the guessed letter is not in the chosen_word, reduce the number of lives by 1 and print the number of lives left. 
# If the player runs out of lives, print "You lose." and break out of the loop.

# game_over = False
# placeholders = ["_" for _ in chosen_word]
# lives = 6
# print(f"You have {lives} lives.")
# while not game_over:
#     guess = input("Guess a letter: ").lower()
#     correct_letters = []
#     if guess in chosen_word:
#         for index, letter in enumerate(chosen_word):
#             if letter == guess:
#                 placeholders[index] = letter
#         print("Right!")
#     else:
#         lives -= 1
#         print(f"Wrong! You have {lives} lives left.")
#         if lives == 0:
#             print("You lose.")
#             game_over = True
#             break
#     print(f"Display: {''.join(placeholders)}")
#     if "_" not in placeholders:
#         print("You win!")
#         game_over = True

### STEP 5 - Improving the User Experience
# 5.1 - Update the word list to use the `word_list` from hangman_words.py.
# 5.2 - Import the log from hangman_art.py and print the logo at the start of the game.
# 5.3 - Update the code to tell the user how many lives they have left after each guess.

import random
import beginner.hangman_words as hangman_words
import beginner.hangman_art as hangman_art

chosen_word = random.choice(hangman_words.word_list)

print(hangman_art.logo)

game_over = False
placeholders = ["_" for _ in chosen_word]
lives = 6
print(f"You have {lives} lives.")
while not game_over:
    guess = input("Guess a letter: ").lower()
    correct_letters = []
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                placeholders[index] = letter
        print("Right! You have {lives} lives left.")
    else:
        lives -= 1
        print(f"Wrong! You have {lives} lives left.")
        if lives == 0:
            print("You lose.")
            game_over = True
            break
    print(f"Display: {''.join(placeholders)}")
    if "_" not in placeholders:
        print("You win!")
        game_over = True

print(f"The chosen word is: {chosen_word}")