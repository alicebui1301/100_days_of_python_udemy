# Coding Exercise 4: BMI Calculator
# bmi is equal to the person's weight divided by the person's height squared.
height = 1.65 
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight / (height ** 2)

print(round(bmi))

# f-strings
score = 0
height = 1.8
is_winning = True

print(f"Your score is {score}, your height is {height}, you are winning is {is_winning}")

# Day 2 Project: Tip Calculator
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = total_bill * tip_as_percent
total_bill_with_tip = total_bill + total_tip_amount
bill_per_person = total_bill_with_tip / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")