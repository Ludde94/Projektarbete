class computer: 
    
    def __init__(self):
        self.computer = computer
        
    def computer_roll_hard(self,turn_value): #beslut utifrån turnvalue
        while turn_value < 20: #lägga till rollsmade<6
            print("computer will roll")
            return True
        return False
        
    def computer_roll_easy(self,turn_value):
        while turn_value < 25:
            print("computer will roll")
            return True
        return False
    
    