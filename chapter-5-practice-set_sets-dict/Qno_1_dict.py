# Write a program to create a dictionary of Hindi words with values as their English translation. 
# Provide the user with an option to look it up!

hin2eng = {"samay":"time", "antaral":"interval", "viksit":"developed", "hamala":"attack", "tika":"vaccine"}
key = input("enter a hindi word : ")
if key not in hin2eng:
    print("invalid key")
else:
    print(f"{key} means {hin2eng[key]}")
