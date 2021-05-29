# Attempt problem 1 using a while loop.
# Write a program to print the multiplication table of a given number using for loop.

num = int(input("Enter a number to print its table\n"))

start = 1
while(start <= 10):
    print(f"{num} X {start} = {num*start}")
    start+=1

print("Done!")