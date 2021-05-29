# Create a class programmer for storing information of a few programmers working at Microsoft.

class Programmer:
    def __init__(self,name,salary,position):
        self.name = name
        self.salary = salary
        self.position = position
    
    def showDetails(self):
        print(f'name of the programmer = {self.name}')
        print(f'salary of the programmer = {self.salary}')
        print(f'position of the programmer = {self.position}')


vineet = Programmer("Vineet Gulecha","12k","junior assistant software engineer")
vineet.showDetails()





