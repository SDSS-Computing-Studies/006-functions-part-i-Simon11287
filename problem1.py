#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side
(2 points)
"""

import math

def hypotenuse(a,b,c):
    if True==c:
        if a<b:
            x=(math.pow(b,2)-math.pow(a,2))
            x=float(x)
            x=math.sqrt(x)
            return x
        elif b<a:
            x=(math.pow(a,2)-math.pow(b,2))
            x=float(x)
            x=math.sqrt(x)
            return x

    elif False==c:
        x=(math.pow(a,2)+math.pow(b,2))
        x=math.sqrt(x)
        return x

a=hypotenuse(13,5,True)
print(a)
b=hypotenuse(3,4,False)
print(b)
