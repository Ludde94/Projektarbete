import unittest
from unittest.mock import patch
import io
from Player import Player

class TestPlayer(unittest.TestCase):
    """Test player object"""

    def test_player(self):
        """ Testing if the player is the instance of Player class """
        player = Player("John Doe", 100)
        self.assertIsInstance(player, Player)

    def test_changename(self):
        """ 
        Testing if the changename method properly 
        updates the name of the player 
        """
        player = Player("John Doe", 100)
        CHANGED_NAME = "New Name"
        
        player.changename(CHANGED_NAME)
        self.assertEqual(player.name, CHANGED_NAME)

    def test_changename_2(self):
        """ 
        Testing if the changename method properly 
        updates the name of the player, by comparing
        the previous value of the name 
        """
        NAME = "John Doe"
        CHANGED_NAME = "New Name"

        player = Player(NAME, 100)

        player.changename(CHANGED_NAME)

        self.assertNotEqual(player.name, NAME)

    @patch('Player.Player.input_number', return_value=1)
    def test_input_number(self, input):
        """
        Testing if the input_number method properly returns
        the number '1' if the user inputs "1"
        """
        player = Player("John Doe", 100)
        self.assertEqual(player.input_number(), 1)
    
    @patch('Player.Player.input_number', return_value=0)
    def test_input_number_2(self, input):
        """
        Testing if the input_number method properly returns
        the number '0' if the user inputs "0"
        """
        player = Player("John Doe", 100)
        self.assertEqual(player.input_number(), 0)

    @patch('Player.Player.input_number', return_value="random text")
    def test_input_number_3(self, input):
        """
        Testing if the input_number method does not returns
        the number if the user inputs any other value than 0 or 1
        """
        player = Player("John Doe", 100)
        self.assertNotEqual(player.input_number(), 0)

    @patch('Player.Player.input_number', return_value=0)
    def test_play(self, input):
        """
        Testing if the user inputs '0', then it completes 
        the play method and returns "computer" indicating it 
        has completed the method meanwhile writing 
        "wise choice [John Doe] your total score is 0"
        to the console
        """
        player = Player("John Doe", 100)
        self.assertEqual(player.play(), "computer")

    @patch('Player.Player.input_number', return_value=1)
    def test_play_2(self, input):
        """
        Testing if the user inputs '1', then it completes 
        the play method and returns "computer" indicating it 
        has completed the method meanwhile writing to the console
        results based on the random outputs from the dice
        e.g. [John Doe] rolled: 5, and your turnscore: 35
        """
        player = Player("John Doe", 100)
        self.assertEqual(player.play(), "computer")

    @patch('Player.Player.input_number', return_value=1)
    def test_play_3(self, input):
        """
        Testing if the user wins by returning "winner"
        when the maximum score limit is reached, which 
        is in this case 1 (for the sake of this testcase)
        """
        player = Player("John Doe", 1)
        self.assertEqual(player.play(), "winner")

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('Player.Player.input_number', return_value=0)
    def test_play_4(self, expected_output, mock_stdout):
        """
        Testing if the correct output is printed to the 
        console when the user enters 0 which should print 
        "wise choice [John Doe] your total score is 0\n\n"
        to the console.
        """
        player = Player("John Doe", 100)
        player.play()
        self.assertEqual(mock_stdout.getvalue(), "wise choice [John Doe] your total score is 0\n\n")

        self.assertNotEqual(mock_stdout.getvalue(), "Any other random text")
        
if __name__ == '__main__':
    unittest.main()
    