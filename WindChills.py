"""
*Author : Tanmay Ku Mallick
*Date   : 19-08-2021
*Title  : Wind Chills
"""

import math


class WindChills:
    @staticmethod
    def Wind_chills_evaluation():
        try:
            w = 0
            t = float(input("Enter temperature in Fahrenheit "))
            v = float(input("Enter speed in miles/hour"))
            if t > 50:
                print("Enter the Value Below 50")
                raise ValueError
            elif 3 < v < 120:
                w = 35.74 + (0.6215 * t) + ((0.4275 * t) - 35.75) * (v ** 0.16)
            else:
                print("Enter the correct value for Speed i.e 3<V<120")
                raise ValueError
        except ValueError:
            print("Invalid Input")
        return w


windChill = WindChills()
result = WindChills.Wind_chills_evaluation()
print("The temperature for the wind chill is :-> ", result)
