# Write a program to find out the line number where python is present from question 6.

content = True
LineCount = 0

with open('chapter-9-FilesIO.py/logFile.txt','r') as f:
    while content:
        content = f.readline()
        LineCount+=1

        if 'python' in content:
            print(f"'python' found in line {LineCount} of logFile.txt")
            print(content)

# this tells us how to check if it is end of file
# content will be False when f.readline() will return a blank string() 
# i.e  when we are done with all the lines
