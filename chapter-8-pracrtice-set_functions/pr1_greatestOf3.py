# Write a program using the function to find the greatest of three numbers.

def greatest(n1,n2,n3):
    if n1>=n2 and n1>=n3:
        return n1
    elif n2>=n1 and n2>=n3:
        return n2
    else:
        return n3

print(greatest(3,5,12))
print(greatest(3,55,12)) 
print(greatest(23,5,12)) 
