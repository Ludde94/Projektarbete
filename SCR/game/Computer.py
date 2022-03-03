import dice

class computer: 
    create = dice.Dice
    turnvalue = create.get_value
    rollsmade = create.get_rolls_made
    
    def __init__(self):
        self.computer = computer
        
    def computer_roll_hard(self,turnvalue,rollsmade): #beslut utifrån turnvalue
        """computer hard setting"""
        while turnvalue < 20 and rollsmade < 6: 
            print("computer will roll")
            return True
        return False
        
    def computer_roll_easy(self,turnvalue,rollsmade):
        """computer easy setting"""
        while turnvalue < 30 and rollsmade < 10:
            print("computer will roll")
            return True
        return False
    
    