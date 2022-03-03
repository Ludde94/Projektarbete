import dice

class computer: 
    create = dice.Dice
    turnvalue = create.get_value
    
    def __init__(self):
        self.computer = computer
        
    def computer_roll_hard(self,turnvalue): #beslut utifrån turnvalue
        """computer hard setting"""
        while turnvalue < 20: #lägga till rollsmade<6
            print("computer will roll")
            return True
        return False
        
    def computer_roll_easy(self,turnvalue):
        """computer easy setting"""
        while turnvalue < 30:
            print("computer will roll")
            return True
        return False
    
    