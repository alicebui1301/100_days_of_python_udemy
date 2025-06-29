# Write a program that converts their scores to grades.
# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# def convert_student_grade(student_scores):
#     student_grades_dict = {}
#     for name, score in student_scores.items():
#         if 91 <= score <= 100:
#             grade = "Outstanding"
#         elif 81 <= score <= 90:
#             grade = "Exceeds Expectations"
#         elif 71 <= score <= 80:
#             grade = "Acceptable"
#         else:
#             grade = "Fail"
#         student_grades_dict[name] = grade
#     return student_grades_dict

# student_grades = convert_student_grade(student_scores)
# print(student_grades)

# Project 9: The Secret Auction
# Create a program that allows users to bid on items.
# The program should store the bids in a dictionary and determine the highest bid at the end.
# Ask if there are any other bidders after each bid. If yes, clear the screen and continue taking bids.

import os

logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

def find_highest_bid(bids):
    highest_bid = 0
    winner = ""
    for bidder, amount in bids.items():
        if amount > highest_bid:
            highest_bid = amount
            winner = bidder
    print(f"The winner is {winner} with {highest_bid} bid")

bids = {}
while True:
    print(logo)
    bidder = input("What is your name? ")
    amount = float(input("What is your bid? $"))
    
    bids[bidder] = amount
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    
    if more_bidders == 'yes':
        # Clearing the Screen
        os.system('cls' if os.name == 'nt' else 'clear')
    elif more_bidders == 'no':
        find_highest_bid(bids)
        break
    else:
        print("Please type 'yes' or 'no'.")



