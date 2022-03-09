from dice import Dice
from random import randint, choices

class Computer():

    def __init__(self):
        """computer object"""
        self.name = "Ultimate computer"
        self.dice = Dice()
        self.current_value = 0
        self.current_rolls = 0
        self.current_sum = 0
        self.box = 0


    def set_difficulty(self, difficulty):
        """set difficulty on computer"""
        self.difficulty = difficulty


    def play(self):
        """computer play function"""
        self.running = True
        weights_easy = [170, 100, 100, 100, 100, 100]#25% för en etta
        weights_hard = [110, 100, 100, 100, 100, 100]#18% för en etta
        hold_hard = [3, 1] #en av tre slag = hold
        hold_easy = [1, 3] #två av tre slag = hold
        threshold_easy = 40
        threshold_hard = 20


        while self.running:
            if self.difficulty == "Easy":
                result = choices(self.dice.sides, weights_easy)[0]
            elif self.difficulty == "Hard":
                result = choices(self.dice.sides, weights_hard)[0]
            self.current_rolls += 1
            if result == 1:
                print("Opps i got a 1, your turn")
                print(f'Computer still has a score of {self.current_sum}')
                self.box = 0
                self.running = False
            else:
                print(f'Bot rolled: {result}')
                self.box += result

                if self.difficulty == "Easy":
                    threshold = threshold_easy
                elif self.difficulty == "Hard":
                    threshold = threshold_hard 

                if self.current_sum >= threshold:
                    if self.difficulty == "Easy":
                        hold = choices([True, False], weights = hold_easy)[0]
                    elif self.difficulty == "Hard":
                        hold = choices([True, False], weights = hold_hard)[0]
                    if hold:
                        print(f'Computer chooses to hold, with a value of {self.current_sum}')
                        self.current_sum += self.box
                        self.running = False
