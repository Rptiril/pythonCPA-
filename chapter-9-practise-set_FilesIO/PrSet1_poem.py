# Write a program to read the text from a given file “poems.txt” 
# and find out whether it contains the word ‘twinkle’.

f = open('chapter-9-practise-set_FilesIO\poem.txt','r')
content = f.read()
str = input("Enter a string you want to search : ")

if str in content:
    print(f"yes {str} is present")
else:
    print(f"{str} is not present")

f.close()

