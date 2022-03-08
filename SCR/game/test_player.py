import unittest
from player import Player

class TestPlayer(unittest.TestCase):
    """Test player object"""
    def test_player(self):
        play = Player()
        self.assertIsInstance(play, Player)
        
if __name__ == '__main__':
    unittest.main()
    