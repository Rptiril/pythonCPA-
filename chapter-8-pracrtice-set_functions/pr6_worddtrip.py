# Write a python function to remove a given word from a list and strip it at the same time.

str = "     there is an old lady who lives by a river            "
# x = str.strip()
# print(x)

def Remove(s,word):
    word1 = word + " "
    str1 = s.replace(word1,"")
    str1 = str1.strip()
    return str1

print(Remove(str,"an"))

