# Human Player_01
def nim_human_01(match_sticks):

    # if (match_sticks < 4):
    #     taken = match_sticks
    #     match_sticks = match_sticks - taken
    #     return(match_sticks)

    user_chance = int(input("Nim Human One chance to remove 1,2 or 3 sticks \n"))

    if (user_chance > 0 and user_chance < 4):
        pass
    else:
        while(user_chance not in [1,2,3]):
            user_chance = int(input("Invalid Input!!..Human One please choose 1,2 or 3 sticks \n"))


    match_sticks = match_sticks - user_chance
    return(match_sticks,user_chance)

# Human Player_02
def nim_human_02(match_sticks):

    # if (match_sticks < 4):
    #     taken = match_sticks
    #     match_sticks = match_sticks - taken
    #     return(match_sticks)

    user_chance = int(input("Nim Human Two chance to remove 1,2 or 3 sticks \n"))

    if (user_chance > 0 and user_chance < 4):
        pass
    else:
        while(user_chance not in [1,2,3]):
            user_chance = int(input("Invalid Input!!..Human Two please choose 1,2 or 3 sticks \n"))


    match_sticks = match_sticks - user_chance
    return(match_sticks,user_chance)