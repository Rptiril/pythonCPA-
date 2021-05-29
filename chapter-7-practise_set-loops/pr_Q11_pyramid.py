# Write a program to print the following star pattern.
#     *
#    ***  
#   ***** for n=3

lines = int(input("Eneter the number of lines for the pattern : "))

# for i in range(lines):
for j in range(1,lines+1):
    print(" "*(lines-j) + "*"*(2*j-1) )
    # print("\n")

