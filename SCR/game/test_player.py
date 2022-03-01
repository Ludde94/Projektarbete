import unittest
import Player

class TestPlayer(unittest.TestCase):
    def test_player(self):
        play= Player.player()
        self.assertIsInstance(play, Player.player)
        
if __name__ == '__main__':
    unittest.main()
    