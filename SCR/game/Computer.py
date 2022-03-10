"""module docstring"""
from time import sleep
from random import choices
from dice import Dice


class Computer:
    """class of computer player"""

    def __init__(self, winning_number):
        """computer object"""
        self.difficulty = None
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
        running = True
        weights_easy = [170, 100, 100, 100, 100, 100]  # 25% för en etta
        weights_hard = [110, 100, 100, 100, 100, 100]  # 18% för en etta
        weights_cheat = [1, 0 ,0 ,0 ,0 ,0] #100% etta
        hold_hard = [5, 1]
        hold_easy = [1, 3]
        threshold_easy = 20
        threshold_hard = 15

        while running:
            result = self.roll_dice(weights_easy, weights_hard, weights_cheat)
            self.current_rolls += 1  # count total rolls

            if result == 1:
                running = self.computer_got_1()
            else:
                self.box += result
                print(f"[Computer] rolled: {result}, and it's turnscore is: {self.box}")
                if self.current_sum >= self.winning_number:
                    self.box = 0
                    return "winner"
                elif self.box + self.current_sum >= self.winning_number:
                    self.box = 0
                    return "winner"
                elif self.box >= self.winning_number:
                    self.box = 0
                    return "winner"

                threshold = self.set_treshhold_difficulty(threshold_easy, threshold_hard)

                if self.box >= threshold or (self.box + self.current_sum) >= threshold:
                    if self.difficulty == "Easy":
                        hold = choices([True, False], weights=hold_easy)[0]
                    elif self.difficulty == "Hard":
                        hold = choices([True, False], weights=hold_hard)[0]
                    if hold is True:
                        self.current_sum += self.box
                        self.box = 0
                        print(
                            f'\n[Computer] chooses to hold, with a value of {self.current_sum}')
                        break
        return "player"

    def set_treshhold_difficulty(self, threshold_easy, threshold_hard):
        """"set difficulty threshold"""
        if self.difficulty == "Easy":
            threshold = threshold_easy
        elif self.difficulty == "Hard":
            threshold = threshold_hard
        return threshold

    def computer_got_1(self):
        """function for computer getting 1 score"""
        self.box = 0
        print("\n[Computer] got a 1, passing turn...")
        print(f'[Computer] still has a score of {self.current_sum}\n')
        running = False
        return running

    def roll_dice(self, weights_easy, weights_hard, weights_cheat):
        """roll dice function"""
        if self.difficulty == "Easy":
            result = choices(self.dice.sides, weights_easy)[0]
            sleep(1.5)
        elif self.difficulty == "Hard":
            result = choices(self.dice.sides, weights_hard)[0]
            sleep(1.5)
        elif self.difficulty == "Cheat":
            result = choices(self.dice.sides, weights_cheat)[0]
        return result
