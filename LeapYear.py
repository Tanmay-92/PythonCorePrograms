"""
*Author : Tanmay Ku Mallick
*Date   : 18-08-2021
*Title  : Leap Year
"""
flag=True
while flag:
    try:
        year=int(input("Enter the Year :"))
        if year < 999:
            print("enter the correct year")
            flag = False
            raise ValueError
        elif year > 9999:
            print ("enter the Correct Year")
            raise ValueError
        else:
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        print("year is leap year")
                    else:
                        print("not a leap year")
                else:
                    print("not a leap year")
            else:
                print("not a leap year")
            flag = False
    except ValueError:
        print("invalid input")
