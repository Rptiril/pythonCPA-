# Write a program to greet all the person names stored in a list l1 and which starts with S.
# l1 = ["Harry", "Sohan", "Sachin", "Rahul"]
 
# list
l1 = ["Harry", "Sohan", "Sachin", "Rahul"]

for name in l1:
    if(name.startswith('S')):
        print("Hello " + name + "!")

