# Write a program to accept marks of 6 students and display them in a sorted manner.
marks = []
for i in range (6):
    x = input(f"Enter the marks of {i+1}th student : ")
    marks.append(x)
marks.sort()
print("Marks in sorted order : \n",marks)