# test_main.py
import unittest
from unittest.mock import patch, MagicMock
import main
import utils
import shortest_path
import minimum_spanning_tree
import graph_isomorphism


class TestMain(unittest.TestCase):
    @patch.object(utils, 'display_challenge')
    @patch.object(utils, 'get_input')
    @patch.object(shortest_path, 'shortest_path')
    @patch.object(minimum_spanning_tree, 'minimum_spanning_tree')
    @patch.object(graph_isomorphism, 'graph_isomorphism')
    def test_main(self, mock_isomorphism, mock_mst, mock_path, mock_input, mock_challenge):
        # Setup
        mock_challenge.side_effect = [
            {"type": "shortest_path", "graph_data": [(1, 2), (2, 3), (3, 4)], "start": 1, "end": 4},
            {"type": "minimum_spanning_tree", "graph_data": [(1, 2), (2, 3), (3, 4), (4, 1)]},
            {"type": "graph_isomorphism", "graph_data": [(1, 2), (2, 3), (3, 4)], "other_graph": [(5, 6), (6, 7), (7, 8)]},
            None  # To stop the loop
        ]
        mock_input.side_effect = [
            [(1, 2), (2, 3), (3, 4)],  # Shortest path input
            [(1, 2), (2, 3), (3, 4), (4, 1)],  # MST input
            [(5, 6), (6, 7), (7, 8)]  # Graph isomorphism input
        ]
        mock_path.return_value = True
        mock_mst.return_value = True
        mock_isomorphism.return_value = True

        # Execute
        main.main()

        # Verify
        mock_path.assert_called_once_with(mock_challenge.side_effect[0], mock_input.side_effect[0])
        mock_mst.assert_called_once_with(mock_challenge.side_effect[1], mock_input.side_effect[1])
        mock_isomorphism.assert_called_once_with(mock_challenge.side_effect[2], mock_input.side_effect[2])


if __name__ == '__main__':
    unittest.main()
