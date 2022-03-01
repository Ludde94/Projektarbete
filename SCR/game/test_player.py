import unittest
import Player

class TestPlayer(unittest.TestCase):
    """Test player object"""
    def test_player(self):
        play= Player.player()
        self.assertIsInstance(play, Player.player)
        
if __name__ == '__main__':
    unittest.main()
    