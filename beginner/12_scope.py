# Prime number checker function
# This function checks if a number is prime by checking if it has any divisors other than 1 and itself.
# Note: 4 and 1 are not considered prime numbers.

def is_prime(num):
    divisors = []
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                divisors.append(i)
        if len(divisors) >= 1:
            return False
        else:
            return True     
    else:
        return False
    
print(is_prime(75))
print(is_prime(73))
print(is_prime(4))
print(is_prime(2))

# Modifying global scope variables
enemies = 1

## NOT A GOOD PRACTICE
def increase_enemies():
    global enemies  # Declare that we are using the global variable 'enemies'
    enemies += 1
    print(f"Enemies increased to {enemies}")

## A GOOD PRACTICE
def increase_enemies(enemies):
    enemies += 1
    print(f"Enemies inside function: {enemies}")

increase_enemies(enemies)
print(f"Enemies outside function: {enemies}")

# Project 12: Number Guessing Game
# This is a simple number guessing game where the player has to guess a randomly generated number within a certain range.
# The player can choose between two difficulty levels: easy (10 attempts) and hard (5 attempts).
# The game provides feedback on whether the guess is too high or too low, and it
# ends when the player guesses the number or runs out of attempts.
# The game also informs the player of the number of attempts remaining after each guess.
# The game continues until the player either guesses the number or runs out of attempts.
# The game uses the random module to generate a random number between 1 and 100.

import random

def check_guess(guess, number_to_guess):
    if guess < number_to_guess:
        print("Too low. Try again.")
        return False
    elif guess > number_to_guess:
        print("Too high. Try again.")
        return False
    else:
        print(f"You got it! The answer was {number_to_guess}.")
        return True

def set_attempts(difficulty):
    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5
    return attempts

def guessing_number():
    print(f"Welcome to the Number Guessing Game!\n I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts = set_attempts(difficulty)
    print(f"You have {attempts} attempts to guess the number.")
    
    number_to_guess = random.randint(1, 100)
        
    while attempts > 0:
        guess = int(input("Make a guess: "))
        attempts -= 1
        result = check_guess(guess, number_to_guess)
        print(f"You have {attempts} remaining attempts to guess the number.")
        
        if result:
            attempts = 0  # End the game if the guess is correct

guessing_number()
