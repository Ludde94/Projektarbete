import unittest
from menu import Menu

class TestPlayer(unittest.TestCase):
    """Test Menu object"""
    def test_player(self):
        test_menu = Menu()
        self.assertIsInstance(test_menu, Menu)
        
        
    if __name__ == '__main__':
        unittest.main()