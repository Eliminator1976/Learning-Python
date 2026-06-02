def main():
    amount = 0
    while amount != 50:
        money = int(input("Insert Coin: "))
        if money == 25 or money == 10 or money==5:
            amount = amount + money
            if amount >= 50:
                break
            print(F"Amount due: {50-amount}")
            
        else:
            print("Amount not accepted")
            continue
    if amount > 50:
        print("Change Owed: " + str(amount-50))
    print("Elevate your day, one crisp sip at a time!")
main()