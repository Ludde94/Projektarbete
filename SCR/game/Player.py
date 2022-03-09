
from dice import Dice
from random import randint


class Player():
    """"creating player object"""
    def __init__(self, name, winning_number):
        self.name = name
        self.dice = Dice()
        self.current_value = 0
        self.current_rolls = 0
        self.current_sum = 0
        self.box = 0
        self.winning_number = winning_number

    def changename(self, newname):
        """changing player name"""
        self.name = newname

    def input_number(self, prompt='Please enter a number: '):
        """Read a positive number with the given prompt."""

        while True:
            try:
                number = int(input(prompt))
                if number in [1, 0]: 
                    return number
            except ValueError:
                print('You need to enter a number')
                continue

    def play(self):
        """Decision for keep rolling"""
        self.running = True
        while self.running:
            human_decision = self.input_number("  1 - Roll, 0 - Hold? ")
            if human_decision == 1:
                result = randint(1, 6)
                if result != 1:

                    self.box += result
                    print(f"You rolled: {result}, and your turnscore: {self.box}")
                    if self.current_sum >= self.winning_number or (self.box + self.current_sum) >= self.winning_number:
                        return "winner"
                else:
                    self.box = 0
                    print(f"Opps i got a {result}, passing turn")
                    print(f'{self.name} still has a score of {self.current_sum}')
                    self.running = False

            else:
                self.current_sum += self.box
                self.box = 0
                print(f"wise choice {self.name} your total score is {self.current_sum}")
                self.running = False
        return "computer"