# Dictionary Comprehension
# new_dict = {key: value for item in list}
import pandas
import random

student_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90,
}

# Create a  new dictionary with students who scored equal to or above 60
passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}

# Dictionary Comprehension 1
# You are going to use Dictionary Comprehension to create a dictionary 
# called result that takes each word in the given sentence and calculates 
# the number of letters in each word.
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}

# Dictionary Comprehension 2
# You are going to use Dictionary Comprehension to create a dictionary called 
# weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit. 
# To convert temp_c into temp_f use this formula: (temp_c * 9/5) + 32 = temp_f.
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day:((temp_c * 9/5) + 32) for (day,temp_c) in weather_c.items()}
print(weather_f)

