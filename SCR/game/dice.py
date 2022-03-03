import random

class Dice():
    
    def __init__(self):
        """creating dice with random"""
        self.sum_rolls = 0
        self.sum_rolls_made = 0
        self.value = random.randint(1, 6)

    def roll(self):
        """creating roll with random value"""
        self.sum_rolls_made += 1
        self.value = random.randint(1, 6)
        self.sum_rolls += self.value
        return self.value
    
    def get_value(self):#funkar inte att addera, får ingen output
        """get value all rolls"""
        return self.sum_rolls
    
    def get_rolls_made(self):
        """get how many rolls were made"""
        return self.sum_rolls_made
    
    def get_sum_rolls(self):
        """Get sum of all rolls made."""
        return self.sum_rolls
        
    def __str__(self):
        """Print rolled value"""
        return "Rolled " + str(self.value) + "."
