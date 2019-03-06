# Assignment_No. 1.1

# Computer Vs Player Game.....



# def computer_nim(sticks):
#
#     taken = 0
#     if (sticks < 4):
#         taken = sticks
#         sticks = sticks - taken
#     else:
#         if (sticks % 4 == 0):
#             taken = random.randint(1, 3)
#             sticks = sticks - taken
#         else:
#             while (sticks % 4 != 0):
#                 taken = taken + 1
#                 sticks = sticks - 1
#
#     return sticks
#
# def player_nim_01(match_sticks):
#
#     if (match_sticks < 4):
#         taken = match_sticks
#         match_sticks = match_sticks - taken
#         return(match_sticks)
#
#     user_chance = int(input("Player One chance to remove 1,2 or 3 sticks \n"))
#
#     if (user_chance > 0 and user_chance < 4):
#         pass
#     else:
#         while(user_chance not in [1,2,3]):
#             user_chance = int(input("Invalid Input!!..Player please choose 1,2 or 3 sticks \n"))
#
#
#     match_sticks = match_sticks - user_chance
#     return(match_sticks)
#
# def game_controller(match_sticks):
#
#     while(match_sticks>0):
#
#         match_sticks = player_nim_01(match_sticks)
#         print('After User Input, Match sticks left ->', match_sticks)
#         if (match_sticks <= 0):
#             return ('Player One Win')
#
#
#         match_sticks = computer_nim(match_sticks)
#         print('After computer input, Match sticks left ->',match_sticks)
#         if(match_sticks<=0):
#             return('Computer Win')
#
#
# n = int(input('Please enter the number of Match sticks \n'))
# obj = game_controller(n)
# print(obj)


# Assignment_No. 1.2

# def sort4(*t):
#     t = list(t)
#     for j in range(0, len(t)-1):
#         for i in range(0,len(t)-1):
#             if(t[i]>t[i+1]):
#                 t[i], t[i+1] = t[i+1], t[i]
#     return(t)
#
#
# obj = sort4(12,3,34,8)
# print(obj)




# def computer_nim(sticks):
#     taken = 0
#     if (sticks < 4):
#         taken = sticks
#         sticks = sticks - taken
#     else:
#         if (sticks % 4 == 0):
#             taken = random.randint(1, 3)
#             sticks = sticks - taken
#         else:
#             while (sticks % 4 != 0):
#                 taken = taken + 1
#                 sticks = sticks - 1
#
#     return sticks

# Player Vs Player Game........

# import random
#
# def player_nim_01(match_sticks):
#
#     if (match_sticks < 4):
#         taken = match_sticks
#         match_sticks = match_sticks - taken
#         return(match_sticks)
#
#     user_chance = int(input("Player One chance to remove 1,2 or 3 sticks \n"))
#
#     if (user_chance > 0 and user_chance < 4):
#         pass
#     else:
#         while(user_chance not in [1,2,3]):
#             user_chance = int(input("Invalid Input!!..Player One please choose 1,2 or 3 sticks \n"))
#
#
#     match_sticks = match_sticks - user_chance
#     return(match_sticks)
#
# def player_nim_02(match_sticks):
#
#     if (match_sticks < 4):
#         taken = match_sticks
#         match_sticks = match_sticks - taken
#         return(match_sticks)
#
#     user_chance = int(input("Player Two chance to remove 1,2 or 3 sticks \n"))
#
#     if (user_chance > 0 and user_chance < 4):
#         pass
#     else:
#         while(user_chance not in [1,2,3]):
#             user_chance = int(input("Invalid Input!!..Player Two please choose 1,2 or 3 sticks \n"))
#
#
#     match_sticks = match_sticks - user_chance
#     return(match_sticks)
#
# def game_controller(match_sticks):
#
#     while(match_sticks>0):
#
#         match_sticks = player_nim_01(match_sticks)
#         print('After Player One Input, Match sticks left ->', match_sticks)
#         if (match_sticks <= 0):
#             return ('Player One Win')
#
#
#         match_sticks = player_nim_02(match_sticks)
#         print('After Player two input, Match sticks left ->',match_sticks)
#         if(match_sticks<=0):
#             return ('Player Two Win')
#
#
# n = int(input('Please enter the number of Match sticks \n'))
# obj = game_controller(n)
# print(obj)

# class Exception(Exception):
#     pass



#
# import random
#
# #Player selection
# def play_nim_game():
#     print("Select 1 - Computer Simple Vs Human, 2 - Computer Complex Vs Human, 3 - Human Vs Human, 0 - Exit")
#     game = int(input("Enter your choice\n"))
#     while(game not in [1,2,3,0]):
#
#         game = int(input("Invalid Number!!..Please Enter your choice again\n"))
#
#     if game == 1:
#         player = [nim_simple, nim_human_01]
#     elif game == 2:
#         player = [nim_complex, nim_human_01]
#     elif game == 3:
#         player = [nim_human_02, nim_human_01]
#     elif game == 0:
#         player = None
#
#     return (player)
#
# # Toss for first chance
# def toss(player):
#     n = int(input('Enter 1 - Head or 2 - Tails for the first chance!!..\n'))
#     while(n not in [1,2]):
#         n = int(input('Invalid Input!!..Please Enter 1 - Head or 2 - Tails for the first chance!!..\n'))
#     if(n==random.randint(1,2)):
#         player[0], player[1] = player[1], player[0]
#         print(player[0].__name__,"won the toss")
#     else:
#         print(player[0].__name__,"won the toss")
#
#     return(player)
#
# # Computer complex player
# def nim_complex(sticks):
#
#     taken = 0
#     if (sticks < 4):
#         taken = sticks
#         sticks = sticks - taken
#     else:
#         if (sticks % 4 == 0):
#             taken = random.randint(1, 3)
#             sticks = sticks - taken
#         else:
#             while (sticks % 4 != 0):
#                 taken = taken + 1
#                 sticks = sticks - 1
#
#     return sticks
#
# # Computer simple player
# def nim_simple(sticks):
#     if sticks >= 3:
#         taken = random.randint(1,3)
#     elif sticks == 2:
#         taken = random.randint(1,2)
#     else:
#         taken = 1
#
#     sticks = sticks - taken
#     return sticks
#
# # Human Player
# def nim_human_01(match_sticks):
#
#     # if (match_sticks < 4):
#     #     taken = match_sticks
#     #     match_sticks = match_sticks - taken
#     #     return(match_sticks)
#
#     user_chance = int(input("Nim Human Onechance to remove 1,2 or 3 sticks \n"))
#
#     if (user_chance > 0 and user_chance < 4):
#         pass
#     else:
#         while(user_chance not in [1,2,3]):
#             user_chance = int(input("Invalid Input!!..Human One please choose 1,2 or 3 sticks \n"))
#
#
#     match_sticks = match_sticks - user_chance
#     return(match_sticks)
#
# def nim_human_02(match_sticks):
#
#     # if (match_sticks < 4):
#     #     taken = match_sticks
#     #     match_sticks = match_sticks - taken
#     #     return(match_sticks)
#
#     user_chance = int(input("Nim Human Two chance to remove 1,2 or 3 sticks \n"))
#
#     if (user_chance > 0 and user_chance < 4):
#         pass
#     else:
#         while(user_chance not in [1,2,3]):
#             user_chance = int(input("Invalid Input!!..Human Two please choose 1,2 or 3 sticks \n"))
#
#
#     match_sticks = match_sticks - user_chance
#     return(match_sticks)
#
# #game controller
# def game_controller(match_sticks, player):
#
#     if match_sticks == 0:
#         raise Exception("Invalid Number!!..Please enter positive number..")
#
#     player = toss(player)
#
#     print("Game Start!!!! ")
#     i = 0
#     while(match_sticks>0):
#         match_sticks = player[i](match_sticks)
#         print(player[i].__name__,"left ->",match_sticks,"Match Sticks")
#         i = (i+1)%len(player)
#
#     return(player[i-1])
#
#
# player = play_nim_game()
#
# if player:
#     n = int(input('Please enter the number of Match sticks \n'))
#     obj = game_controller(n, player)
#     print(obj.__name__, "Won")
#     print("Game End!!..Thank you and Please play again..")
#
# else:
#     print("Thank you for showing some Interest in this game!!..")










