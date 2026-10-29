#university scholarship
marks = int(input("Enter aggregate marks: "))
subject = int(input("Enter minimum subject marks: "))
attendance = int(input("Enter attendance: "))
income = int(input("Enter family income: "))

if marks >= 85 and subject >= 70 and attendance >= 75 and income <= 200000:
    print("Scholarship Eligible")
elif marks >= 85:
    print("Waitlist")
else:
    print("Not Eligible")