# Write a program that returns True or False whether if a given year is a leap year.
# This is how you work out whether if a particular year is a leap year. 
# - on every year that is divisible by 4 with no remainder
# - except every year that is evenly divisible by 100 with no remainder 
# - unless the year is also divisible by 400 with no remainder   

from ast import operator
from unittest import result
from more_itertools import first


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
        
is_leap_year = is_leap_year(1989)
print(is_leap_year)

# Project 10: Calculator
# Create a simple calculator that can perform addition, subtraction, multiplication, and division.

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2  

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


def calculator():
    should_continue = True
    first_number = float(input("Whats the first number?: "))

    calculators = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }
    
    while should_continue:
        operation = str(input("Pick an operation: +, -, *, /: "))
        second_number = float(input("Whats the second number?: "))

        result =  calculators[operation](first_number, second_number)
        print(f"{first_number} {operation} {second_number} = {result}")
        restart = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        
        if restart == 'y':
            first_number = result
        elif restart == 'n':
            should_continue = False
    
    calculator()    

calculator()