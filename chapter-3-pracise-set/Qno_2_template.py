'''
Write a program to fill in a letter template given below with name and date.
letter =   " Dear <|NAME|>,

                You are selected!

                    <|DATE|>"
'''
name = input("Name : ")
date = input("Date : ")
print(f'''
                  Dear {name},

                You are selected!

                    {date}"
''')
