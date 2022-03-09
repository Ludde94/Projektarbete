from dice import Dice
from random import randint

class Player():
    """"creating player object"""
    def __init__(self, name):
        self.name = name
        self.dice = Dice()
        self.current_value = 0
        self.current_rolls = 0
        self.current_sum = 0
        self.box = 0

    def changename(self, newname):
        """changing player name"""
        self.name = newname

    def input_number(self, prompt='Please enter a number: ', minimum=0, maximum=None):
        """Read a positive number with the given prompt."""

        while True:
            try:
                number = int(input(prompt))
                if (number < minimum or
                    (maximum is not None and number > maximum)):
                        print('Number is not within range: {} to {}'.format(minimum, maximum))
                else:
                    break

            except ValueError:
                print('You need to enter a number')
                continue

        return number

    def play(self):
        """Decision for keep rolling"""
        self.running = True
        human_decision = self.input_number("  1 - Roll again, 0 - Hold? ", 0, 1)
        while self.running:
            if human_decision == 1:
                result = randint(1, 6) # Här ska vi fortsätta!
            else:
                pass
