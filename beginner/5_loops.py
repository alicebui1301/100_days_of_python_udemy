# FizzBuzz
# You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:
# Your program should print each number from 1 to 100 in turn and include number 100.
# But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

for i in range (1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#  Day 5 Project: Create a Password Generator
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

import random
# #Easy level password generator
# password = ""

# # Add letters to the password list
# for char in range(0, nr_letters):
#     password += random.choice(letters)
    
# # Add symbols to the password list
# for char in range(0, nr_symbols):
#     password += random.choice(letters)

# # Add numbers to the password list
# for char in range(0, nr_numbers):
#     password += random.choice(letters)

# Difficult level password generator
password_list = []

# Add letters to the password list
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

# Add symbols to the password list
for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

# Add numbers to the password list
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

# Shuffle the password list
random.shuffle(password_list)
# Join the password list to create a string
password = "".join(password_list)
print(f"Your password is: {password}")