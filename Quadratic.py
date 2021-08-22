"""
*Author : Tanmay Ku Mallick
*Date   : 20-08-2021
*Title  : Quadratic Equation
"""
from math import sqrt


class Quadratic:
    @staticmethod
    def quadratic_equation():
        try:
            a = int(input("Enter the value for A :"))
            b = int(input("Enter the value for B :"))
            c = int(input("Enter the value for C :"))
            if (a and b and c) == 0:
                print("Enter the value not Equal to zero")
                raise ValueError
            else:
                d = (b ** 2) - (4 * a * c)
                print("The value for D :=")
            if d > 0:
                x1 = (-b + sqrt(d)) / (2 * a)
                x2 = (-b - sqrt(d)) / (2 * a)
                print("the value for X1", x1)
                print("the value for X2", x2)
            elif d == 0:
                x3 = -b / (2 * a)
                print("the Value for X3", x3)
            else:
                print("No Roots")
                raise ValueError
        except ValueError:
            print("Invalid Input")
obj=Quadratic()
obj.quadratic_equation()