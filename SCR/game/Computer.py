from dice import Dice
from random import randint

class Computer(): 
    
    create = Dice
    turnvalue = create.get_sum_rolls
    rollsmade = create.get_rolls_made
    
    def __init__(self):
        """computer object"""
        self.computer_roll_easy
        self.computer_roll_hard
        
    def computer_hard(self, rollsmade): #test
        auto = randint(1, 35)
        while rollsmade < 4 and auto <= 25:
            print("computer will roll")
            return True
        else:
            print("computer will hold")
            return False
    
    def computer_easy(self, rollsmade): #test
        auto = randint(1, 35)
        while rollsmade < 6 and auto <= 20:
            print("computer will roll")
            return True
        else:
            print("computer will hold")
            return False
        
        
        
    def computer_roll_hard(self, turnvalue, rollsmade):  # beslut utifrån turnvalue
        """computer hard setting"""
        while turnvalue < 20 and rollsmade < 4: 
            print("Computer will roll")
            return True
        else:
            print("Computer will hold")
            return False
        
    def computer_roll_easy(self, turnvalue, rollsmade):
        """computer easy setting"""
        while turnvalue < 30 and rollsmade < 8:
            print("Computer will roll")
            return True
        else:
            print("Computer will hold")
        return False
    
    def comp_decision():
       print("Which computer setting would you like to play against?")
       comp_decision = int(input("1 - Easy, 2 - hard"))
       return comp_decision