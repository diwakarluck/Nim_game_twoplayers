from nim_human_code import *
from nim_computer_simple import *
from nim_computer_complex import *
import random

#Player selection
def play_nim_game():
    print("Select 1 - Computer Simple Vs Human, 2 - Computer Complex Vs Human, 3 - Human Vs Human, 0 - Exit")
    game = int(input("Enter your choice\n"))
    while(game not in [1,2,3,0]):

        game = int(input("Invalid Number!!..Please Enter your choice again\n"))

    if game == 1:
        player = [nim_simple, nim_human_01]
    elif game == 2:
        player = [nim_complex, nim_human_01]
    elif game == 3:
        player = [nim_human_02, nim_human_01]
    elif game == 0:
        player = None

    return (player)

# Toss for first chance
def toss(player):
    n = int(input('Enter 1 - Head or 2 - Tails for the first chance!!..\n'))
    while(n not in [1,2]):
        n = int(input('Invalid Input!!..Please Enter 1 - Head or 2 - Tails for the first chance!!..\n'))
    if(n==random.randint(1,2)):
        player[0], player[1] = player[1], player[0]
        print(player[0].__name__,"won the toss")
    else:
        print(player[0].__name__,"won the toss")

    return(player)