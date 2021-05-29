# 4-> file contains the word “Donkey” multiple times. 
# You need to write a program which replaces this word with ###### by updating the same file.
# Repeat program 4 for a list of such words to be censored.

sensored = ['donkey','beat','kill','bomb','kaddu','criminal']
edited = ''

with open('chapter-9-practise-set_FilesIO\Srnsored.txt','r') as f:
    content = f.read()
    for word in sensored:
        content = content.replace(word,'#@$^%!#')

with open('chapter-9-practise-set_FilesIO\Srnsored.txt','w') as f:
    f.write(content)