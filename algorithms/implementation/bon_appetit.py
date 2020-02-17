def bon_appetit(bill, k, b):
    bill.pop(k)
    if sum(bill)/2 == b:
        print("Bon Appetit")
    else:
        print(f"{b - sum(bill)/2:.0f}")

