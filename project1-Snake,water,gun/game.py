import random

def Game(you,comp):
    if you == comp:
        return None
    elif you == 's':
        if comp == 'w':
            return True
        elif comp == 'g':
            return False
    elif you == 'w':
        if comp == 'g':
            return True
        elif comp == 's':
            return False
    elif you == 'g':
        if comp == 's':
            return True
        elif comp == 'w':
            return False


print("Computer's Turn: Choose 's' for Snake, 'w' for Water or 'g' for Gun")

val = random.randint(1,3)

if val == 1:
    comp = 's'
elif val == 2:
    comp = 'w'
else:
    comp = 'g'

you = input("Your's Turn : Choose 's' for Snake, 'w' for Water or 'g' for Gun ->  ")
result = Game(you,comp)

print(f"You Choose {you} and Computer choose {comp}")

if result is None:
    print("Game Tied!")
elif result is True:
    print("You Won!")
else:
    print("You Lose!")