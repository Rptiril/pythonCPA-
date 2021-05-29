# Write a program to generate multiplication tables from 2 to 20 
# and write it to the different files. 
# Place these files in a folder for a 13- year old boy.

for i in range (2,21):
    with open(f"chapter-9-FilesIO.py/multiplication_Table_of_{i}.txt",'w') as f:
        for j in range (1,11):
            f.write(f"{i} * {j} = {i*j}\n")

# with open("chapter-9-FilesIO.py/poem.txt",'w') as f:
#     f.write('when the blazing sun is gone\n')
#     f.write('when theres nothing light upon\n')
#     f.write("hello!")
