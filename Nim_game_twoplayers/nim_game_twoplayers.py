# 1-heap NIM game..
# Rule: Consider a heap of n pieces. Players take turns to remove 1-3 pieces. Whoever manages to take the last piece (match sticks), wins....

from nim_human_code import *
from nim_computer_simple import *
from nim_computer_complex import *
from player_selection_n_toss import *
import random

#game controller
def game_controller(match_sticks, player,ms):

    print('Match Sticks ->', ms)

    if match_sticks == 0:
        raise Exception("Invalid Number!!..Please enter positive number..")

    player = toss(player)

    print("Game Start!!!! ")
    i = 0
    while(match_sticks>0):
        # ms = ms[0:len(ms) - player[i](match_sticks)[1]]
        ret = player[i](match_sticks)
        match_sticks = ret[0]
        ms = ms[0:len(ms)-ret[1]]
        print(player[i].__name__,"Match Sticks left",match_sticks," -> ",ms)
        i = (i+1)%len(player)

    return(player[i-1])

def nim_game():
    player = play_nim_game()

    if player:
        n = int(input('Please enter the number of Match sticks \n'))
        ms = '|'
        ms = ms * n
        obj = game_controller(n, player, ms)
        print(obj.__name__, "Won")
        print("Game End!!..Thank you and Please play again..")

    else:
        print("Thank you for showing some Interest in this game!!..")

nim_game()