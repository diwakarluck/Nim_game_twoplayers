import random

# Computer simple player
def nim_simple(sticks):
    if sticks >= 3:
        taken = random.randint(1,3)
    elif sticks == 2:
        taken = random.randint(1,2)
    else:
        taken = 1

    sticks = sticks - taken
    return sticks,taken