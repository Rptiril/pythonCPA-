n = int(input("Enter the lines in X pattern : "))

for i in range (1,n+1):
    for j in range (1,n+1):
        if i==j or i+j == n+1:
            print("*",end='')
        else:
            print(" ",end='')
    print('')
    

    