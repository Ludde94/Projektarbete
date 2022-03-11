"""module docstring"""
import unittest
import os
from high_score import HighScore


class TestHighScore(unittest.TestCase):
    """Test high-scoring"""
    def test_read_file(self):
        """
        Testing if we are reading the correct
        sample data from the file
        """
        high_score = HighScore()
        path = os.getcwd()
        data = high_score.read_file(path + '\\SCR\\game\\testfile.json')
        self.assertEqual(data, [{"name": "John Doe", "rolls": 20}])

    def test_update_high_score(self):
        """
        Testing if we are updating the high score,
        by first reading data and then updating
        that data
        """
        high_score = HighScore()
        path = os.getcwd()
        data = high_score.read_file(path + '\\SCR\\game\\testfile.json')
        entry = {"name": "New User", "rolls": 13}
        updated_data = high_score.update_high_score(data, entry)

        self.assertEqual(updated_data, data)

    def test_save_high_score(self):
        """
        Testing if the new data is saved in the file,
        first we get the already existing data and add
        our new entry and then feed it to the file and
        the data is saved,
        Also in the end we update the file with the initial
        testing sample data to make the tests work each time
        """
        high_score = HighScore()
        path = os.getcwd()

        prev_data = high_score.read_file(path + '\\SCR\\game\\testfile.json')

        entry = prev_data + [{"name": "TestUser", "rolls": 15}]

        high_score.save_high_score(path + '\\SCR\\game\\testfile.json', entry)
        new_data = high_score.read_file(path + '\\SCR\\game\\testfile.json')

        self.assertEqual(new_data, entry)

        high_score.save_high_score(path + '\\SCR\\game\\testfile.json', [{"name": "John Doe", "rolls": 20}])


if __name__ == '__main__':
    unittest.main()
