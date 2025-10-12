def add(n1, n2):
    return n1 + n2 

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator(n1, n2, operation):
    return operation(n1, n2)    

result = calculator(10, 5, add)
print(result)
#15