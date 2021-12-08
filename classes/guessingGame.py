import random
from .user import User

class Game:
    def __init__(self):
        self.answer = 0
        self.leave = 0


    def getRandomNumber(self):
        self.answer = random.randint(1, 6)
        self.answer
        return self.answer
    
    def checkInput(self, choice):
        if choice > 5 or choice < 1:
            message = print("Number is out of range\n")
            self.leave = 0
            return self.leave
        else:
            if choice == self.answer:
                message = print(f"Great guess {player.name}!\n")
                self.leave = 1
                return self.leave
            else:
                message = print("Sorry wrong answer try again\n")
                self.leave = 0
                return self.leave
    
    def start(self):
        self.getRandomNumber()
        game = True
        while game:
            userName = str(input("Please let us know your name:  "))
            player = User(userName)
            message = print("You have 3 tries to guess the right number\n")
            round = [1,2,3]
            for r in round:
                if r == 1 or 2:
                    message = print(f"Round {r}")
                    choice = input(f"{player.name}, please pick a number between 1 and 5\n")
                    choice = choice.split()
                    self.checkInput(int(choice[0]))
                    if self.leave == 1:
                        game = False
                else:
                    message = print(f"Round {r}")
                    choice = input(f"Please pick a number between 1 and 5\n")
                    choice = choice.split()
                    self.checkInput(int(choice[0]))
                    if self.leave == 1:
                        game = False
            message = print(f"Sorry out of rounds\n")
            self.leave = 1
            game = False
