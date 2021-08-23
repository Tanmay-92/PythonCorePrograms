import random


class Gambler:
    Winner = 0
    Lose = 0
    initialAmount = int(input("Enter Your Amount:"))
    goal = int(input("Enter goal:"))
    flag = True
    count = 0
    goalCheck = initialAmount

    while flag:
        betAmount = int(input("Enter Your Betting Amount:"))
        randomCheck = random.uniform(0, 1)
        basicAmount = initialAmount - betAmount
        count += 1
        if initialAmount < 0:
            flag = False
            break
        elif initialAmount == goal:
            break
        elif basicAmount < 0:
            print("Amount is Not Enough")
            print("Amount Available: ", initialAmount)
            break
        elif goal < goalCheck:
            print("Invalid Goal")
        elif randomCheck < 0.5:
            print("Lose")
            basicAmount = initialAmount - betAmount
            Lose += 1
        else:
            print("Winner")
            basicAmount = initialAmount + betAmount
            Winner += 1

    winPercentage = (Winner * 100) / count
    losePercentage = (Lose * 100) / count
    print("At End Of The  Game Total Amount:", initialAmount)
    print("Winning Percentage:", winPercentage)
    print("Losing Percentage:", losePercentage)


gambler = Gambler()
