# *arg functions allow you to pass a variable number of arguments to a function.
# This is useful when you don't know in advance how many arguments will be passed to your function
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

# *kwargs allow you to pass a variable number of keyword arguments (i.e., named arguments) to a function.
# This is useful when you want to handle named arguments that you didn't define in advance.
def calculate(n, **kwargs):
    print(n)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n