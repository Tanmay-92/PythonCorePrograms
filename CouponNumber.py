"""
*Author : Tanmay Ku Mallick
*Date   : 20-08-2021
*Title  : CouponNumber
"""
import math
import random


class CouponNumber:

    @staticmethod
    def Coupon_numbers():
        count = 0
        coupon = []
        coupon_count = int(input("enter the no.of coupons u wants to generate"))
        flag = True
        while coupon_count >= (count + 1):
            randomNumber = random.randrange(1, 1000)
            if (not (coupon.__contains__(randomNumber))):
                coupon.append(randomNumber)
                count += 1
            elif coupon_count:
                flag = False
            else:
                print("no contain")
            print(coupon)


couponNo = CouponNumber()
couponNo.Coupon_numbers()
