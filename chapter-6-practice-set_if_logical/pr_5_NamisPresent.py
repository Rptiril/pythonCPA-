# Write a program that finds out whether a given name is present in a list or not.

name = input("Enter a name : ")

NameList = ["Noah","Oliver","Elijah","William","James","Benjamin","Lucas","Henry","Alexander","Mason","Michael"]

if name in NameList:
    print("Name is Present.")
else:
    print("Name is not present.")