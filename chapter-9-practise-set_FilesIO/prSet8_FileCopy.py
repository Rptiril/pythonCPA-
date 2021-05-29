# Write a program to make a copy of a text file “story.txt” as "StoryCopy.txt".

with open('chapter-9-FilesIO.py/story.txt','r') as f:
    content = f.read()

with open('chapter-9-FilesIO.py/StoryCopy.txt','w') as f:
    f.write(content)