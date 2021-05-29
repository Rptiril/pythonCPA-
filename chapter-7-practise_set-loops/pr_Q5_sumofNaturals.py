# Write a program to find the sum of first n natural numbers using a while loop

sum = 0
i = 0 

last = int(input("Enter the number till sum is wanted : "))

while(i <= last):
    sum+=i
    i+=1

print(sum)