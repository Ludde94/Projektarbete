"""module docstring"""
class Dice:
    """class of the die"""
    def __init__(self):
        """creating dice with random"""
        self.sum_rolls = 0
        self.sum_rolls_made = 0
        self.value = 0
        self.sides = [1, 2, 3, 4, 5, 6]

    def get_rolls_made(self):
        """get how many rolls were made"""
        return self.sum_rolls_made

    def get_sum_rolls(self):
        """Get sum of all rolls made."""
        return self.sum_rolls

    def __str__(self):
        """Print rolled value"""
        return "Rolled " + str(self.value) + "."
