from datetime import datetime
from os import system, name

from misc.messages import *
from classes.user import User
from classes.guessingGame import Game

def clear():
    if name =='nt':
        _ = system('clear')
    else:
        _ = system('clear')


playing = True
now = datetime.now()
currentTime = now.strftime("%H:%M:")
while playing:
    clear()
    message = print(f"{welcome}")
    message = print(f"The current time is {currentTime}")
    clear()
    message = str(input(f"{day} \n"))
    message = input(f"\nWould you like to play a game?\n")
    if message[0] == 'n':
        message = print(noGame)
        playing = False
    else:
        message = input(yesGame)
        if message[0] == 'n':
            message = print(go)
            playing = False
        else:
            message = print(cool)
            message = print("\nLets get to playing!\n")
            game = Game()
            game = game.start()
            playing = False