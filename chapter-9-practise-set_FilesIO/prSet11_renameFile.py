# Write a python program to rename a file to “renamed_by_python.txt”.

import os

old = "chapter-9-practise-set_FilesIO\sample.txt"
new = "renamed_by_python.txt"

with open(old,'r') as f:
    content = f.read()

with open(new,'w') as f:
    f.write(content)

os.remove(ol)