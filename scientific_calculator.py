"module 3"
import math

def square(number):
    return number*number
def square_root(number):
    if number<0:
        raise ValueError("Square root of a negative number is not possible")
    return math.sqrt(number)
def factorial(number):
    if number<0 or number !=int(number):
        raise ValueError("Please enter a positive whole number")
    return math.factorial(int(number))
def sine(angle):
    angle=math.radians(angle)
    return math.sin(angle)
def cosine(angle):
    angle = math.radians(angle)
    return math.cos(angle)
def tangent(angle):
    if angle%180==90:
        raise ValueError("Tangent is not defined for this angle")
    angle=math.radians(angle)
    return math.tan(angle)
def logarithm(number):
    if number<=0:
        raise ValueError("Number must be greater than zero")
    return math.log10(number)
def natural_log(number):
    if number<=0:
        raise ValueError("Number must be greater than zero")
    return math.log(number)