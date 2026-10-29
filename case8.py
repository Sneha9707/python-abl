#retail
n = int(input("Enter number of products: "))
total = 0

for i in range(n):
    price = int(input("Enter price: "))
    qty = int(input("Enter quantity: "))
    amount = price * qty

    if amount >= 1000:
        amount = amount - amount * 0.10

    tax = amount * 0.05
    total = total + amount + tax

print("Final bill:", total)