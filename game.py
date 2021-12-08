from datetime import datetime
from os import system, name

from misc.messages import *
from classes.user import User
from classes.guessingGame import Game

def clear():
    if name =='nt':
        _ = system('cls')
    else:
        _ = system('cls')


playing = True
now = datetime.now()
currentTime = now.strftime("%H:%M:")
while playing:
    clear()
    message = print(f"{welcome}")
    message = print(f"The current time is {currentTime}")
    userName = str(input("Please let us know your name:  "))
    player = User(userName)
    message = print(f"Welcome {player.name}")
    message = str(input(f"{day} \n"))
    message = input(f"\n{player.name}, would you like to play a game?")
    if message[0] == 'n':
        message = print( noGame)
        playing = False
    else:
        message = print(yesGame)
        if message[0] == 'n':
            message = print(go)
            playing = False
        else:
            message = print(cool)
            message = print("Lets get to playing!")
            game = Game()
            game = start()
            playing = False