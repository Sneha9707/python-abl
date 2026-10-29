#progressive electric billing
n = int(input("Enter number of months: "))
bills = []

for i in range(n):
    units = int(input("Enter units: "))

    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = 200 + (units - 100) * 3
    else:
        bill = 500 + (units - 200) * 5

    bill = bill + 50
    bills.append(bill)
    print("Bill:", bill)

for i in range(1, len(bills)):
    if bills[i] > bills[i-1] * 1.3:
        print("Unusual increase!")