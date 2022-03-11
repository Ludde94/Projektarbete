import unittest

from dice import Dice

class TestDice(unittest.TestCase):
    
    def test_is_instance(self):
        """
        Testing if the dice is the instance of 
        the Dice class
        """
        dice = Dice()
        self.assertIsInstance(dice, Dice)

    def test_get_rolls_made(self):
        """
        Testing if the get_rolls_made returns
        default 0 when it is not updated
        """
        dice = Dice()
        rolls = dice.get_rolls_made()
        self.assertEqual(rolls, 0)

    def test_get_rolls_made_2(self):
        """
        Testing if the method returns the updated
        value, when it is changed
        """
        dice = Dice()
        dice.sum_rolls_made = 4
        rolls = dice.get_rolls_made()
        self.assertEqual(rolls, 4)

    def test_get_rolls_made_3(self):
        """
        Testing if the method does not return 
        the default value which is 0 when it 
        has beeen updated
        """
        dice = Dice()
        dice.sum_rolls_made = 4
        rolls = dice.get_rolls_made()
        self.assertNotEqual(rolls, 0)

    def test_get_sum_rolls(self):
        """ 
        Testing the method returns the default
        value for sum which is 0
        """
        dice = Dice()
        _sum = dice.get_sum_rolls()
        self.assertEqual(_sum, 0)

    def test_get_sum_rolls_2(self):
        """
        Testing if the method properly returns 
        the updated value of the sum
        """
        dice = Dice()
        dice.sum_rolls = 10
        _sum = dice.get_sum_rolls()
        self.assertEqual(_sum, 10)

    def test_get_sum_rolls_3(self):
        """
        Testing if the method does not return
        the default value when it has been 
        updated
        """
        dice = Dice()
        dice.sum_rolls = 10
        _sum = dice.get_sum_rolls()
        self.assertNotEqual(_sum, 0)

    def test_str(self):
        """
        Testing if our __str__ method properly
        logs to the console with the default 
        values
        """
        dice = Dice()
        TEXT = "Rolled " + str(dice.value) + "."
        self.assertEqual(str(dice), TEXT)

    def test_str_2(self):
        """
        Testing if our __str__ method properly
        logs to the console with the updated 
        values
        """
        dice = Dice()
        dice.value = 5
        TEXT = "Rolled " + str(dice.value) + "."
        self.assertEqual(str(dice), TEXT)

    def test_str_3(self):
        """
        Testing if our __str__ method does not
        log the previous values
        """
        dice = Dice()
        TEXT = "Rolled " + str(dice.value) + "."
        dice.value = 5
        self.assertNotEqual(str(dice), TEXT)

if __name__ == '__main__':
    unittest.main()
