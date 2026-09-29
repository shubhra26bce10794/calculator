"module 1"
def add(a,b):
    c=a+b
    return c
def subtract(a,b):
    c=a-b
    return c
def multiply(a,b):
    c=a*b
    return c
def divide(a,b):
    if b==0:
        raise ZeroDivisionError("Cannot divide by zero")
    c=a/b
    return c
def power(a,b):
    c=a**b
    return c
