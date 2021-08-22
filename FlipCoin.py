"""
*Author : Tanmay Ku Mallick
*Date   : 18-08-2021
*Title  : Flip Coin
"""

import random
heads = 0
tails = 0
heads_percent = 0
tails_percent = 0
flip = int(input("Enter the no.of times u need to flip the coin "))
time = flip
for i in range(0,time):
    result =random.randint(0,1)
    if result <0.5:
        heads +=1
    else:
        tails +=1
print("total no.of heads", +heads)
print("total no.of tails", +tails)
heads_percent=(heads*100)/flip
tails_percent=(tails*100)/flip
print("percentage of heads :", +heads_percent)
print("percentage of tails :", +tails_percent)
