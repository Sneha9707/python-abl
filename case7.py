#railway
distance = int(input("Enter distance: "))
age = int(input("Enter age: "))
print("1. Sleeper  2. AC")
cls = int(input("Choose class: "))

fare = distance * 2

if cls == 2:
    fare = distance * 4

if age < 12 or age >= 60:
    fare = fare * 0.5

total = fare + 50
print("Total fare:", total)

cancel = input("Cancel ticket? yes/no: ")
if cancel == "yes":
    print("Refund:", total - 100)