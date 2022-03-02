import random

class Dice():
    """creating dice with random"""
    def __init__(self):
        self.value = random.randint(1, 6)

    def roll(self):
        """creating roll with random value"""
        self.value = random.randint(1, 6)
        

        return self.value

    def __str__(self):
        return "Rolled " + str(self.value) + "."
