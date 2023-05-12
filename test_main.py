# test_main.py

import unittest
from unittest.mock import patch
from main import main

class TestMain(unittest.TestCase):

    @patch('utils.Utils.get_input', return_value=[1, 2, 3, 4])
    @patch('utils.Utils.display_challenge', side_effect=[{"type": "shortest_path", "graph_data": [(1, 2), (2, 3), (3, 4)], "start": 1, "end": 4}, None])
    def test_shortest_path_correct(self, mock_input, mock_challenge):
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_once_with('Correct!')
    
    @patch('utils.Utils.get_input', return_value=[1, 2, 4])
    @patch('utils.Utils.display_challenge', side_effect=[{"type": "shortest_path", "graph_data": [(1, 2), (2, 3), (3, 4)], "start": 1, "end": 4}, None])
    def test_shortest_path_incorrect(self, mock_input, mock_challenge):
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_once_with('Incorrect!')

if __name__ == '__main__':
    unittest.main()
