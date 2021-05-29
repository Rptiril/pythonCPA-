def greet(name = "Stranger"):
    print("Good day " + name + " :)")

# greet("Varun")
# greet("Sandhya")
# greet("Vineet")
# greet()

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
    
print(fact(6))