import unittest
import menu

class TestPlayer(unittest.TestCase):
    """Test Menu object"""
    def test_player(self):
        test_menu= menu.Menu()
        self.assertIsInstance(test_menu,menu.Menu)
        
        
    if __name__ == '__main__':
        unittest.main()