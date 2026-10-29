#multiplan
usage = int(input("Enter data usage in GB: "))
budget = int(input("Enter budget: "))

plan1 = 199 + max(0, usage - 10) * 20
plan2 = 299 + max(0, usage - 20) * 10
plan3 = 399

if plan1 <= budget and plan1 <= plan2 and plan1 <= plan3:
    print("Choose Plan 1:", plan1)
elif plan2 <= budget and plan2 <= plan3:
    print("Choose Plan 2:", plan2)
elif plan3 <= budget:
    print("Choose Plan 3:", plan3)
else:
    print("No plan within budget")