# Create an empty dictionary. 
# Allow 4 friends to enter their favorite language as keys and their names as values. 
# Assume that the names are unique.

# MyDict = {"C":"Dennis Ritchie", "C++":"Bjarne Stroatop", "Python":"Guido van Rossum",
#             "SQL":"Donald and Boyce"}
# print(MyDict['C++'])

FavLang = {}
lang1 = input("Ritchie's favourite lnguage : ")
lang2 = input("Bjarne's favourite language : ")
lang3 = input("Rossum's favourite language : ")
lang4 = input("DnB's favourite language : ")

FavLang['Ritchie'] = lang1
FavLang['Bjarne'] = lang2
FavLang['Rossum'] = lang3
FavLang['DnB'] = lang4

print(FavLang)
