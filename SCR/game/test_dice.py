import unittest

from dice import Dice

# class TestDice(unittest.TestCase):
#     """Test dice class"""
#     def setUp(self):
#         self.die = dice.Dice()
#         self.die1 = dice.Dice()


#     def test_dice(self):
#         """Test dice object"""
#         self.assertIsInstance(self.die, dice.Dice)

#     def test_roll(self):
#         """Test dice roll"""

#         res = self.die1.value
#         exp = 1 <= res <= self.die1.value
#         self.assertTrue(exp)

#     def test_roll_betweem_one_to_six(self):
#         """Testing if rolled dice gives value between 1-6"""
#         self.die1.roll()
#         self.assertIn(self.die1.value, [1,2,3,4,5,6])


class TestDice(unittest.TestCase):
    
    def test_is_instance(self):
        dice = Dice()
        self.assertIsInstance(dice, Dice)

    def test_get_rolls_made(self):
        dice = Dice()
        rolls = dice.get_rolls_made()
        self.assertEqual(rolls, 0)

    def test_get_rolls_made_2(self):
        dice = Dice()
        dice.sum_rolls_made = 4
        rolls = dice.get_rolls_made()
        self.assertEqual(rolls, 4)

    def test_get_rolls_made_3(self):
        dice = Dice()
        dice.sum_rolls_made = 4
        rolls = dice.get_rolls_made()
        self.assertNotEqual(rolls, 0)

    def test_get_sum_rolls(self):
        dice = Dice()
        _sum = dice.get_sum_rolls()
        self.assertEqual(_sum, 0)

    def test_get_sum_rolls_2(self):
        dice = Dice()
        dice.sum_rolls = 10
        _sum = dice.get_sum_rolls()
        self.assertEqual(_sum, 10)

    def test_get_sum_rolls_3(self):
        dice = Dice()
        dice.sum_rolls = 10
        _sum = dice.get_sum_rolls()
        self.assertNotEqual(_sum, 0)

    def test_str(self):
        dice = Dice()
        TEXT = "Rolled " + str(dice.value) + "."
        self.assertEqual(str(dice), TEXT)

    def test_str_2(self):
        dice = Dice()
        dice.value = 5
        TEXT = "Rolled " + str(dice.value) + "."
        self.assertEqual(str(dice), TEXT)

    def test_str_3(self):
        dice = Dice()
        TEXT = "Rolled " + str(dice.value) + "."
        dice.value = 5
        self.assertNotEqual(str(dice), TEXT)

if __name__ == '__main__':
    unittest.main()
