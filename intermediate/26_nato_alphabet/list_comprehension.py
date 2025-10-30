# List Comprehension
# new_list = [new_item for item in list]
number = [1,2,3]
new_number = [n + 1 for n in number]
print(new_number)

name = "Alice"
letters_list = [letter for letter in name]
print(letters_list)

range_list = [num * 2 for num in range(1,5)]
print(range_list)

# Conditional List Comprehension
# new_list = [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

# Coding Exercise 1: Squaring Numbers
numbers = [1, 2, 3, 4, 5]
squared_numbers = [number ** 2 for number in numbers]
print(squared_numbers)

# Coding Exercise 2: Filtering Even Numbers
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(string) for string in list_of_strings]
result = [n for n in numbers if n%2 == 0]
print(result)

# Coding Exercise 3: Data Overlap

