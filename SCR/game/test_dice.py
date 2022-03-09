import unittest

import dice

class TestDice(unittest.TestCase):
    """Test dice class"""
    def setUp(self):
        self.die = dice.Dice()
        self.die1 = dice.Dice()


    def test_dice(self):
        """Test dice object"""
        self.assertIsInstance(self.die, dice.Dice)

    def test_roll(self):
        """Test dice roll"""

        res = self.die1.value
        exp = 1 <= res <= self.die1.value
        self.assertTrue(exp)

    def test_roll_betweem_one_to_six(self):
        """Testing if rolled dice gives value between 1-6"""
        self.die1.roll()
        self.assertIn(self.die1.value, [1,2,3,4,5,6])


if __name__ == '__main__':
    unittest.main()
