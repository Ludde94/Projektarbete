import unittest
import computer

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.running = computer.Computer()

    def test_play(self):
        self.assertTrue(self.running)
        
        
    if __name__ == '__main__':
        unittest.main()