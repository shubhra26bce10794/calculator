"module 2"
import math

def square(n):
    return n**2
def square_root(n):
    if n<0:
        raise ValueError("Cannot calculate real square root of a negative number")
    return math.sqrt(n)
def factorial(n):
    if n<0 or not isinstance(n, int):
        raise ValueError("Factorial requires a non-negative integer")
    return math.factorial(n)
def sine(n):
    return math.sin(math.radians(n))
def cosine(n):
    return math.cos(math.radians(n))
def tangent(n):
    if n%180==90:
        raise ValueError("Tangent is undefined at this angle")
    return math.tan(math.radians(n))
def logarithm(n):
    if n<=0:
        raise ValueError("Logarithm requires a positive number")
    return math.log10(n)
def natural_log(n):
    if n<=0:
        raise ValueError("Natural logarithm requires a positive number")
    return math.log(n)