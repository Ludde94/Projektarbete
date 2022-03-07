import dice

class Computer(): 
    
    create = dice.Dice
    turnvalue = create.get_sum_rolls
    rollsmade = create.get_rolls_made
    
    def __init__(self):
        """computer object"""
        self.computer_roll_easy
        self.computer_roll_hard
        
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
        
