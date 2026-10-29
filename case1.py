#grading system
subjects = int(input("Enter number of subjects: "))
total = 0

for i in range(subjects):
    marks = int(input("Enter marks out of 100: "))

    if marks < 0 or marks > 100:
        print("Invalid marks!")
    elif marks >= 35:
        print("Pass")
        total = total + marks
    elif marks >= 32:
        marks = marks + 3
        if marks >= 35:
            print("Pass with grace marks:", marks)
            total = total + marks
    else:
        print("Fail")
        total = total + marks

print("Total marks:", total)

if total >= subjects * 75:
    print("Distinction")
elif total >= subjects * 60:
    print("First Class")
elif total >= subjects * 50:
    print("Second Class")
else:
    print("Third Class or Fail")