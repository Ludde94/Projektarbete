import unittest

import dice

class TestDice(unittest.TestCase):
    
    def test_dice(self):
        
        die = dice.Dice()
        
        self.assertIsInstance(die, dice.Dice)
        
    def test_roll(self):
        
        die1 = dice.Dice()

        res = die1.value
        exp = 1 <= res <= die1.value
        self.assertTrue(exp)

        
if __name__ == '__main__':
    unittest.main()
