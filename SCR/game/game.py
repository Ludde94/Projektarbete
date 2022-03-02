from game import dice

class box:
    """box holder for value"""
    def __init__(self):
        self.value = 0
        
    def reset(self):
        self.value = 0
        
    def add_dice_value(self, value):
        self.value += value