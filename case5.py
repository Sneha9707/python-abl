#employee payroll
basic = int(input("Enter basic salary: "))
allowance = int(input("Enter allowances: "))
overtime = int(input("Enter overtime pay: "))
incentive = int(input("Enter incentive: "))

gross = basic + allowance + overtime + incentive

if gross <= 20000:
    deduction = gross * 0.05
elif gross <= 50000:
    deduction = gross * 0.10
else:
    deduction = gross * 0.15

net = gross - deduction

print("Gross salary:", gross)
print("Deduction:", deduction)
print("Net salary:", net)