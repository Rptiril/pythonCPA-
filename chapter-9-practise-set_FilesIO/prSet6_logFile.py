# Write a program to mine a log file and find out whether it contains ‘python’.

with open("chapter-9-FilesIO.py/logFile.txt") as f:
    content = f.read()
    if 'python' in content:
        print("python is present")
    else:
        print("python not found")
    