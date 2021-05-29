# Write a program to find out whether a student is pass or fail. 
# if it requires a total of 40% and at least 33% in each subject to pass. 
# Assume 3 subjects and take marks as an input from the user.

phy  = int(input("Enter Physics Marks : "))
chem = int(input("Enter Chemistry Marks : "))
maths= int(input("Enter Mathematics Marks : "))

avg = (phy+chem+maths)/3

if (avg >= 40):
    if (phy < 33):
        print("your average is ",avg," but phy marks is below 33 so failed.")
    elif (chem < 33):
        print("your average is ",avg," but chem marks is below 33 so failed.")
    elif (maths < 33):
        print("your average is ",avg," but maths marks is below 33 so failed.")
    else:
        print("Passed! hurray having average ",avg)
else:
    print("Failed, try again. improve your ",avg)
