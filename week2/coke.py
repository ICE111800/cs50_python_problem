def main():
    amount_due = 50
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))
        if coin == 25:
            amount_due -= 25
        elif coin == 10:
            amount_due -= 10
        elif coin == 5:
            amount_due -= 5
        else:
            pass
    if amount_due == 0:
        print(f"Change Owed: {amount_due}")
    elif amount_due < 0:
        amount_due = abs(amount_due)
        print(f"Change Owed: {amount_due}")

if __name__ == "__main__":
    main()
        

