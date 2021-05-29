# Write a program to input eight numbers from the user and display all the unique numbers (once).

UniqueNumbers = set()
for i in range (8):
    item = int(input(f"enter {i+1}th value : "))
    UniqueNumbers.add(item)
print(UniqueNumbers)
# AnotherSet = {1, 3, 5, 7 ,9}
# print(UniqueNumbers.union(AnotherSet))
# print(UniqueNumbers.intersection(AnotherSet))
