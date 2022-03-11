"""module docstring"""
import unittest
from computer import Computer

class TestComputer(unittest.TestCase):
    """Test computer"""
    def test_is_instance(self):
        """
        Testing if comp is the instance of Computer class
        """
        comp = Computer(100)
        self.assertIsInstance(comp, Computer)

    def test_set_difficulty(self):
        """
        First testing if the default difficulty is None
        and then we update the difficulty and then test
        if the difficulty was updated and is no longer
        set to None
        """
        comp = Computer(100)
        self.assertEqual(comp.difficulty, None)
        comp.set_difficulty("Easy")
        self.assertNotEqual(comp.difficulty, None)

    def test_set_difficulty_2(self):
        """
        Testing if the difficulty is updated,
        when is set to "Easy"
        """
        comp = Computer(100)
        comp.set_difficulty("Easy")
        self.assertEqual(comp.difficulty, "Easy")

    def test_set_difficulty_3(self):
        """
        Making sure that difficulty is updated and
        is not equal to the previous difficulty
        """
        comp = Computer(100)
        comp.set_difficulty("Easy")
        self.assertNotEqual(comp.difficulty, "Hard")

    def test_set_difficulty_4(self):
        """
        Testing if the difficulty is updated,
        when is set to "Hard"
        """
        comp = Computer(100)
        comp.set_difficulty("Hard")
        self.assertEqual(comp.difficulty, "Hard")

    def test_set_difficulty_5(self):
        """
        Making sure that difficulty is updated and
        is not equal to the previous difficulty
        """
        comp = Computer(100)
        comp.set_difficulty("Hard")
        self.assertNotEqual(comp.difficulty, "Easy")

    def test_set_treshhold_difficulty(self):
        """
        Testing if the correct treshhold is set
        when the difficulty is set to Easy
        """
        comp = Computer(100)
        comp.set_difficulty("Easy")
        threshhold = comp.set_treshhold_difficulty(20, 15)
        self.assertEqual(threshhold, 20)

    def test_set_treshhold_difficulty_2(self):
        """
        Testing if the correct treshhold is set
        when difficulty is set to Hard
        """
        comp = Computer(100)
        comp.set_difficulty("Hard")
        threshhold = comp.set_treshhold_difficulty(20, 15)
        self.assertEqual(threshhold, 15)

    def test_set_treshhold_difficulty_3(self):
        """
        Testing if the treshhold is updated
        when difficulty is set to Easy
        """
        comp = Computer(100)
        comp.set_difficulty("Easy")
        threshhold = comp.set_treshhold_difficulty(20, 15)
        self.assertNotEqual(threshhold, 15)

    def test_set_treshhold_difficulty_4(self):
        """
        Testing if the treshhold is updated
        when difficulty is set to Hard
        """
        comp = Computer(100)
        comp.set_difficulty("Hard")
        threshhold = comp.set_treshhold_difficulty(20, 15)
        self.assertNotEqual(threshhold, 20)

    def test_computer_got_1(self):
        """
        Testing if the computer_got_1 returns
        None when dice value is 1
        """
        comp = Computer(100)
        result = comp.computer_got_1()
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
