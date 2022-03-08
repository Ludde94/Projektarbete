from random import randint,choice


class Dice():
    
    def __init__(self):
        """creating dice with random"""
        self.sum_rolls = 0
        self.sum_rolls_made = 0
        self.value = randint(1, 6)

    def roll(self):
        """creating roll with random value"""
        self.sum_rolls_made += 1
        self.value = randint(1, 6)
        self.sum_rolls += self.value
        return self.value
       
    
    def get_rolls_made(self):
        """get how many rolls were made"""
        return self.sum_rolls_made
    
    
    def get_sum_rolls(self):
        """Get sum of all rolls made."""
        return self.sum_rolls
        
        
    def __str__(self):
        """Print rolled value"""
        return "Rolled " + str(self.value) + "."
