"""module docstring"""
import unittest
from menu import Menu


class TestPlayer(unittest.TestCase):
    """Test Menu object"""
    def test_instance(self):
        """testing instance"""
        menu = Menu()
        self.assertIsInstance(menu, Menu)



if __name__ == '__main__':
    unittest.main()
