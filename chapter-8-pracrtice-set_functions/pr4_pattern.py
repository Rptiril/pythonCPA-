# Write a python function to print the first n lines of the following pattern.
# ***

# **       #For n = 3

# *

n = int(input("Enter nos of lines : "))

for i in range (n,0,-1):
    print("X"*i)