class Box():
    """box holder for value"""
    def __init__(self):
        self.value = 0
        
    def reset(self):
        self.value = 0
        
    def add_dice_value(self,sum_rolls_made):
        self.value += sum_rolls_made