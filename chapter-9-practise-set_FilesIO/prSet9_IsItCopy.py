# Write a program to find out whether a file is identical 
# and matches the content of another file.

with open('chapter-9-FilesIO.py/story.txt','r') as f:
    content1 = f.read()

with open('chapter-9-FilesIO.py/StoryCopy.txt','r') as f:
    content2 = f.read()

if content1 == content2:
    print("Content are exactly same")
else:
    print("content is different")
