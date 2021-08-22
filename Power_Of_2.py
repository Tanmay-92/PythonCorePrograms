"""
*Author : Tanmay Ku Mallick
*Date   : 18-08-2021
*Title  : Power Of 2
"""

Number = int(input("Enter Number to Calculate The series::"))
Base = 2
Result = 1
if Number > 31:
    print("Enter the value Below 31")
elif Number < 0:
    print("Enter the value Above 0")
else:
    for i in range(1, Number+1):
        Result = Result * Base
        print("2 ^", i, ":", Result)
