import unittest

import dice

class TestDice(unittest.TestCase):
    
    def test_dice(self):
        
        die = dice.Dice()
        
        self.assertIsInstance(die, dice.Dice)
        res = die.faces
        exp = 1, 6
        self.assertEqual(res, exp)
        
if __name__ == '__main__':
    unittest.main()
