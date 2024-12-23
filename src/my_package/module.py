def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main(a, b):

    print("add:", add(a, b))
    print("sub:", subtract(a, b))
    print("mul:", multiply(a, b))
    print("div:", divide(a, b))