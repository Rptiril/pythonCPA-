# Write a program to calculate the factorial of a given number using for loop.

num = int(input("Enter a number whose factorial is required : "))

fact = 1

for i in range(1,num+1):
    fact*=i 

print(f"Factorial = {fact}")