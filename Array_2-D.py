"""
*Author : Tanmay Ku Mallick
*Date   : 20-08-2021
*Title  : 2-D Array Problem
"""

from array import *


class array:
    @staticmethod
    def Two_D_Array(m, n):

        Output = []
        for i in range(m):
            row = []
        for j in range(n):
            colmn = int(input(f"enter the matrix[{0}][{j}]"))
            row.append(colmn)
            Output.append(row)
        return Output


obj = array()
m = int(input("enter the value for rows :"))
n = int(input("enter the value for column :"))
A = array.Two_D_Array(m, n)
print("Displaying the matrix", A)
