import unittest
from computer import Computer

class TestComputer(unittest.TestCase):
    
    def test_is_instance(self):
        comp = Computer(100)
        self.assertIsInstance(comp, Computer)

    def test_set_difficulty(self):
        comp = Computer(100)
        self.assertEqual(comp.difficulty, None)
        comp.set_difficulty("Easy")
        self.assertNotEqual(comp.difficulty, None)

    def test_set_difficulty_2(self):
        comp = Computer(100)
        comp.set_difficulty("Easy")
        self.assertEqual(comp.difficulty, "Easy")

    def test_set_difficulty_3(self):
        comp = Computer(100)
        comp.set_difficulty("Easy")
        self.assertNotEqual(comp.difficulty, "Hard")

    def test_set_difficulty_4(self):
        comp = Computer(100)
        comp.set_difficulty("Hard")
        self.assertEqual(comp.difficulty, "Hard")

    def test_set_difficulty_5(self):
        comp = Computer(100)
        comp.set_difficulty("Hard")
        self.assertNotEqual(comp.difficulty, "Easy")

    def test_set_treshhold_difficulty(self):
        comp = Computer(100)
        comp.set_difficulty("Easy")
        threshhold = comp.set_treshhold_difficulty(20, 15)
        self.assertEqual(threshhold, 20)

    def test_set_treshhold_difficulty_2(self):
        comp = Computer(100)
        comp.set_difficulty("Hard")
        threshhold = comp.set_treshhold_difficulty(20, 15)
        self.assertEqual(threshhold, 15)

    def test_set_treshhold_difficulty_3(self):
        comp = Computer(100)
        comp.set_difficulty("Easy")
        threshhold = comp.set_treshhold_difficulty(20, 15)
        self.assertNotEqual(threshhold, 15)

    def test_set_treshhold_difficulty_4(self):
        comp = Computer(100)
        comp.set_difficulty("Hard")
        threshhold = comp.set_treshhold_difficulty(20, 15)
        self.assertNotEqual(threshhold, 20)

    def test_computer_got_1(self):
        comp = Computer(100)
        result = comp.computer_got_1()
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
    
        
        
    