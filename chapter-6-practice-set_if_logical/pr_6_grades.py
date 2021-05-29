# Write a program to calculate the grade of a student from his marks from the following scheme:
# 90 – 100 -> Ex
# 80 - 90 -> A
# 70 – 80 -> B
# 60 – 70 -> C
# 50 – 60 -> D
# <50 – F

marks = int(input("Enter the marks : "))

if marks > 90 and marks <= 100:
    print("Grade S")
elif marks > 80 :
    print("Grade A")
elif marks > 70 :
    print("Grade B")
elif marks > 60 :
    print("Grade C")
elif marks > 50 :
    print("Grade E")
else:
    print("Grade F")