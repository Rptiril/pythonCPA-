# Write a program to store seven fruits in a list entered by the user.
fruits = []
for i in range (7):
    x = input(f"Enter Fruit {i+1} : ")
    fruits.append(x)
print(fruits)