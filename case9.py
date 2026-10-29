#manufacturing
material = int(input("Material cost: "))
labour = int(input("Labour cost: "))
machine = int(input("Machine cost: "))
wastage = int(input("Wastage cost: "))
selling = int(input("Selling price: "))
quantity = int(input("Quantity produced: "))

cost = material + labour + machine + wastage
profit = selling * quantity - cost

print("Total cost:", cost)
print("Profit:", profit)

if profit >= 5000:
    print("Target achieved")
else:
    print("Target not achieved")