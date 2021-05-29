# Write a python program using the function to convert Celsius to Fahrenheit.
# F = (9/5)*C + 32
# C = (5/9)*(F - 32) or (5*(F - 32))/9

C = int(input("Enter Celcius Value : "))

def CelToFah(C):
   F = (9/5)*C + 32
   return F

print(f"Fahrenheight value = {CelToFah(C)}") 