# Day 4 Project: Rock Paper Scissors
import random

rock = """
    _______
---'   ____)
          ______)
         _______)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
        _______)
---'_______)
"""

paper = """
    _______
---'   ____)____
              ______)
             _______)
            _______)
---'_______)
"""

scissors = """
    _______
---'   ____)____
              ______)
           __________)
          (____)
---'_______)
"""
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
print(f"You chose: {user_choice}")
if 0<= user_choice <= 2:
    print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print(f"Computer chose: {computer_choice}")
print(game_images[computer_choice])

if user_choice >=3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
elif user_choice == "0" and computer_choice == 2:
    print("You win!")
if user_choice == "2" and computer_choice == 0:
    print("You lose!")
elif user_choice < computer_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif user_choice == computer_choice:
    print("It's a draw!")
