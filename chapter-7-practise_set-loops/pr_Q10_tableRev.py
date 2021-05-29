# Write a program to print the multiplication table of n using for loop in reversed order

num = int(input("Enter a number to print its table\n"))

for i in range (10,0,-1):
    print(f"{num} X {i} = {num*i}")

print("Done!")