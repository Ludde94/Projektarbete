from time import sleep
from random import choices
from dice import Dice




class Computer:
    """class of computer player"""

    def __init__(self, winning_number):
        """computer object"""
        self.name = "Ultimate computer"
        self.dice = Dice()
        self.current_rolls = 0
        self.current_sum = 0
        self.box = 0
        self.winning_number = winning_number

    def set_difficulty(self, difficulty):
        """set difficulty on computer"""
        self.difficulty = difficulty

    def play(self):
        """computer play function"""
        self.running = True
        weights_easy = [170, 100, 100, 100, 100, 100]  # 25% för en etta
        weights_hard = [110, 100, 100, 100, 100, 100]  # 18% för en etta
        hold_hard = [5, 1]
        hold_easy = [1, 3]
        threshold_easy = 20
        threshold_hard = 15

        while self.running:
            if self.current_sum >= self.winning_number:
                self.running = False
                break
            if self.difficulty == "Easy":
                result = choices(self.dice.sides, weights_easy)[0]
                sleep(1.5)
            elif self.difficulty == "Hard":
                result = choices(self.dice.sides, weights_hard)[0]
                sleep(1.5)
            self.current_rolls += 1
            if result == 1:
                self.box = 0
                print("Opps i got a 1, your turn")
                print(f'Computer still has a score of {self.current_sum}')
                self.running = False
            else:
                print(f'Bot rolled: {result}')
                self.box += result
                if self.current_sum >= self.winning_number or (self.box + self.current_sum) >= self.winning_number:
                    return "winner"

                if self.difficulty == "Easy":
                    threshold = threshold_easy
                elif self.difficulty == "Hard":
                    threshold = threshold_hard

                if self.box >= threshold:
                    if self.difficulty == "Easy":
                        hold = choices([True, False], weights=hold_easy)[0]
                    elif self.difficulty == "Hard":
                        hold = choices([True, False], weights=hold_hard)[0]
                    if hold == True:
                        self.current_sum += self.box
                        self.box = 0
                        print(
                            f'Computer chooses to hold, with a value of {self.current_sum}')
                        self.running = False
                    else:
                        print("chooses to continue")
        return "player"
