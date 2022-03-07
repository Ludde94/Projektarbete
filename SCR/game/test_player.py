import unittest
import player

class TestPlayer(unittest.TestCase):
    """Test player object"""
    def test_player(self):
        play= player.player()
        self.assertIsInstance(play, player.player)
        
if __name__ == '__main__':
    unittest.main()
    