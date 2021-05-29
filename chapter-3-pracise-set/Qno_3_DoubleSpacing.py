'''
Write a program to detect double spaces in a string.
'''
str = " this is a string which contains double spacing"
x = str.find('  ')
if x == -1:
    print("No double spacing found")
else:
    print("Double space found at index",x)