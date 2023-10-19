def addNums(a, b):
    return a + b

def subtractNums(a, b):
    return a - b

def multiplicateNums(a, b):
    return a * b

def divideNums(a, b):
    try:
        return a / b
    except ZeroDivisionError: 
        print("Division by zero is not allowed!")
    