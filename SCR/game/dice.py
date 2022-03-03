import random

class Dice():
    
    def __init__(self):
        """creating dice with random"""
        self.sum_rolls = 0
        self.value = random.randint(1, 6)

    def roll(self):
        """creating roll with random value"""
        self.value = random.randint(1, 6)
        self.sum_rolls += self.value #funkar inte att addera här, hjälp
        return self.value
    
    def get_value(self):#funkar inte att addera, får ingen output
        """get value all rolls"""
        return self.sum_rolls
        
    def __str__(self):
        """Print rolled value"""
        return "Rolled " + str(self.value) + "."
