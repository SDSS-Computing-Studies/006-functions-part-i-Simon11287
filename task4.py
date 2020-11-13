#! python3
"""
Create a function called isInteger()
Input is a float number
Return True if the number is an integer
Return False if the number is not an integer
(2 points)
"""
import math

a= float(input("what is the length of A side"))

b= float(input("what is the length of B side"))

c = sqrt(a**2 + b**2)

print("The length of the hypotenuse is", c )
