# Write a recursive function to calculate the sum of first n natural numbers.
# SumOfNaturals(n) = n + SumOfNAturals(n-1) until n becomes 1

n = int(input("Enter n : "))

def SumOfNaturals(n):
    if n == 1:
        return 1
    else:
        return n + SumOfNaturals(n-1)

print(SumOfNaturals(n))