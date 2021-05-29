# Add a static method in problem 2 to greet the user with hello.

# Write a class calculator capable of finding square, cube and the square root of a number.

# import math
class Calculator:
    
    @staticmethod
    def greet():
        print("hello user!")    
    
    @staticmethod
    def square(a):
        return a*a
    
    @staticmethod
    def cube(a):
        return a*a*a
    
    @staticmethod
    def root(a):
        return pow(a,0.5)


num = int(input("Enter a number : "))

# calci = Calculator()

print(f'square of {num} = {Calculator.square(num)}')
print(f'cube of {num} = {Calculator.cube(num)}')
print(f'root of {num} = {Calculator.root(num)}')
Calculator.greet()