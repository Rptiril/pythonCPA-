# Write a program to print the multiplication table of a given number using for loop.

num = int(input("Enter a number to print its table\n"))

for i in range (1,11):
    print(f"{num} X {i} = {num*i}")

print("Done!")