"""module docstring"""
import unittest
from unittest.mock import patch
import io

from menu import Menu


class TestPlayer(unittest.TestCase):
    """Test Menu object"""
    def test_IsInstance(self):
        menu = Menu()
        self.assertIsInstance(menu, Menu)

    # @patch('sys.stdout', new_callable=io.StringIO)
    # def test_welcome(self, mock_stdout):
    #     menu = Menu()
    #     TEXT = "*" * 50 + """\n\n
    #     Welcome to Pig Dice!
    #     Press Enter to start game.
    #     """.center(50) + "\n\n"
    #     TEXT + "*" * 50 + "\n"

    #     TEXT_2 = """**************************************************

    #     Welcome to Pig Dice!
    #     Press Enter to start game.

    #     **************************************************
    #     """
    #     # print(TEXT_2)
    #     menu.welcome()
    #     # self.assertEqual(mock_stdout.getvalue(), TEXT_2)
    #     # self.assertEqual("", TEXT_2)
    #     self.assertEqual("", mock_stdout.getvalue())

    # @patch('sys.stdout', new_callable=io.StringIO)
    # @patch('builtins.input', return_value="Hola")
    # def test_set_name(self, expected_output, mock_stdout):
    #     menu = Menu()
    #     menu.set_name()
    #     self.assertEqual(mock_stdout.getvalue(), "Wrong! Please enter a valid name.\n")


    # @patch('sys.stdout', new_callable=io.StringIO)
    # def test_rules(self, mock_stdout):
    #     self.maxDiff = None
    #     Text = "*" * 50
    #     Text += "\n"
    #     Text += """
    #     * The objective of the game is to be the first one to reach 100 points
    #     * Each turn, a player will roll a die
    #     * until either a 1 is rolled or the player decides to hold
    #     * If the player rolls any other number,
    #     it is added to their turn total and the player's turn continues
    #     * If a player chooses to hold, their turn total is added to their score
    #     * and it becomes the next player's turn
    #     """.center(50)
    #     Text += "\n"
    #     Text += "*" * 100
    #     Text += "\n"
    #     Text += "\n"

    #     menu = Menu()
    #     menu.rules()
    #     self.assertEqual(mock_stdout.getvalue(), Text)


if __name__ == '__main__':
    unittest.main()
