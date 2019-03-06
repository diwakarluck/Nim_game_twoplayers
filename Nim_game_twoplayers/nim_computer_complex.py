import random

# Computer complex player
def nim_complex(sticks):

    taken = 0
    if (sticks < 4):
        taken = sticks
        sticks = sticks - taken
    else:
        if (sticks % 4 == 0):
            taken = random.randint(1, 3)
            sticks = sticks - taken
        else:
            while (sticks % 4 != 0):
                taken = taken + 1
                sticks = sticks - 1

    return sticks,taken