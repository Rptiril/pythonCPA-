# The game() function in a program lets a user play a game and returns the score as an integer. 
# You need to read a file “Hiscore.txt” which is either blank or contains the previous Hi-score. 
# You need to write a program to update the Hi-score whenever game() breaks the Hi-Score

import random

def game():
    score =  random.randint(1,10)
    return score

val = game()
val = str(val)
print("val is " + val)

f = open('chapter-9-FilesIO.py\HiScore.txt')
content = f.read()

print("content is " + content)

print(val > content)
print(int(val) > int(content))

if int(val) > int(content):
    print("##############")
    f = open('chapter-9-FilesIO.py\HiScore.txt','w')
    f.write(val)


# for i in range(10):
# print(random.randint(1,10))