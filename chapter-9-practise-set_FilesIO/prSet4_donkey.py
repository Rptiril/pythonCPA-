# A file contains the word “Donkey” multiple times. 
# You need to write a program which replaces this word with ###### by updating the same file.

# from os import replace


with open('chapter-9-FilesIO.py/story.txt','r') as f:
    content = f.read()
    print(content)
    edited1 = content.replace('donkey','######')
    edited1 = content.replace('cried','decho-dechon')

    

with open('chapter-9-FilesIO.py/story.txt','w') as f:
    f.write(edited1)




# chat = 'it is a good day, good for all'
# NewChat = chat.replace('good','bad')
# print(NewChat)    
