"""

You are given two interior angles (in degrees) of a triangle.

Write a function to return the 3rd.

Note: only positive integers will be tested.

"""


def other_angle(a, b):
    if (a or b) < 0:
        return "angle cannot be smaller than 0"

    else:
        return 180 - (a + b)
        
