from dice import Dice
from random import randint, choice

class Computer(): 
    
    def __init__(self):
        """computer object"""
        self.name = "Ultimate computer"
        self.dice = Dice()
        self.current_value = 0
        self.current_rolls = 0
        self.current_sum = 0
        
        
    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
        
    def roll(self):
        self.current_value = self.dice.value
        self.current_sum = self.dice.sum_rolls
        self.current_rolls = self.dice.sum_rolls_made
        
    def play(self):
        if self.difficulty == "Easy":
            result = choice(self.dice.sides, weights = [10, 10, 10, 5, 5, 5])
            return result
        elif self.difficulty == "Hard":
            result = choice(self.dice.sides, weights = [5, 5, 5, 10, 10, 10])
            return result


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