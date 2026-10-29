#multi currency
budget = int(input("Enter budget in rupees: "))
rate = float(input("Exchange rate: "))
fee = 100
total = 0

n = int(input("Number of expenses: "))

for i in range(n):
    expense = int(input("Enter expense in foreign currency: "))
    total = total + expense * rate

total = total + fee
print("Total expense in rupees:", total)

if total <= budget:
    print("Within budget")
else:
    print("Budget exceeded")