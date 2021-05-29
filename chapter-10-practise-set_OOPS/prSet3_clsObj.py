# Create a class with a class attribute a; 
# create an object from it and set a directly using object.
# a=0 Does this change the class attribute?

class Bottle:
    name = "Bislery"

aqua = Bottle()
aqua.name = 'Kinley'
print(Bottle.name)
print(aqua.name)
