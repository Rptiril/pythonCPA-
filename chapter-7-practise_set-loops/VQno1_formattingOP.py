# print numbers in same line on python

for i in range (1,11):
    print(i, end = "      ")

fruits = ["Banana", "Pineapple", "Watermelon", "Grapes", "Mango", "Litchi"]

# print("\n")

for fruit in fruits:
    if fruit == "Grapes":
        break
else: # else with a loop is executed only when the loop is executed completely without breaks.
    print("Break does'nt execute  the loop is executed completly")

print("\nDone!")