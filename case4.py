#hospital billing
consult = int(input("Consultation charge: "))
tests = int(input("Diagnostic charges: "))
treatment = int(input("Treatment charges: "))
age = int(input("Enter patient age: "))

total = consult + tests + treatment

if age >= 60:
    total = total - total * 0.10
    print("Senior citizen concession applied")

if total > 5000:
    print("High-cost patient")
else:
    print("Regular patient")

print("Total bill:", total)