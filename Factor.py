"""
*Author : Tanmay Ku Mallick
*Date   : 18-08-2021
*Title  : Factor
"""
try:
    N = int(input("Enter Number to calculate Factor::"))
    if N <= 0:
        print("Number", N, "is Not valid")
        raise ValueError
    else:
        for i in range(1, N + 1):
            if N % i == 0:
             print(i)
except ValueError:
    print("Invalid Input")