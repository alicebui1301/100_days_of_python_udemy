# Coding Exercise 5: Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.
# If the bmi is under 18.5 (not including), print out "underweight"
# If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"
# If the bmi is 25 (including) or over, print out "overweight"

weight = 85
height = 1.85

bmi = weight / (height ** 2)
print(bmi)

if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi < 25:
    print("normal weight")
else:
    print("overweight")

# Pizza Order Practice
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: +$1

# todo: work out how much they need to pay based on their size choice.
bill = 0
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("Invalid size choice. Please choose S, M, or L.")

# todo: work out how much to add to their bill if they want pepperoni.
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# todo: work out their final amount based on whether if they want extra cheese or not.
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}.")

# Project Day 3: Treasure Island
# This is a text-based adventure game where the player has to make choices to find treasure.
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     '"=.|                  |
|___________________|__"=._o'"-._        '"=.______________|___________________
          |                '"=._o'"=._      _'"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; '"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .' ' '' ,  '"-._"-._   ". '__|___________________
          |           |o'"=._' , "' '; .". ,  "-._"-._; ;              |
 _________|___________| ;'-.o'"=._; ." ' ''."' . "-._ /_______________|_______
|                   | |o;    '"-.o'"=._''  '' " ,__.--o;   |
|___________________|_| ;     (#) '-.o '"=.'_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      '".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice_1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right': ")

if choice_1 == "left":
    choice_2 = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across: ")
    if choice_2 == "wait":
        choice_3 = input("You arrive at the island unharmed. There is a house with 3 doors: Red, Yellow, and Blue. Which color do you choose? ")
        if choice_3 == "Yellow":
            print("You win")
        else:
            print("Game over")
    else:
        print("Game over")
else:
    print("Game over")
