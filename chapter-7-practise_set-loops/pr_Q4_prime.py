# Write a program to find whether a given number is prime or not.

num = int(input("Enter a number : "))
count = 0

for i in range(1,num):
    if num%i == 0:
        count+=1

if count == 0:
    print("prime")
else:
    print("Not prime")