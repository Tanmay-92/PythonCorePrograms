"""
*Author : Tanmay Ku Mallick
*Date   : 19-08-2021
*Title  : Distance between the two points
"""


import math


class Distance:
    try:
        X = int(input("Enter the value for X"))
        Y = int(input("Enter the value for Y"))
        if (X and Y) == 0:
            raise ValueError
        else:
            result = (X * X) + (Y * Y)
            distance = math.sqrt(result)
            print("Distance between the two points ", +distance)
    except ValueError:
        print("Invalid Input")
