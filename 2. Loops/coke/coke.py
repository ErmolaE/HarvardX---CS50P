amount = 0
while amount < 50:
    coin = input("Insert Coin: ")
    if coin == "5":
        amount += 5
    if coin == "10":
        amount += 10
    if coin == "25":
        amount += 25
    if 50 - amount > 0:
        print("Amount Due: " + str(50 - amount))
    if 50 - amount <= 0:
        print("Change Owed: " + str(amount - 50))