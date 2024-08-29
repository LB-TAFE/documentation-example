# pylint: disable=missing-module-docstring
import unittest
from src.tic_tac_toe import print_board, is_win, tally_wins  # pylint: disable=unused-import


class TestTicTacToe(unittest.TestCase):  # pylint: disable=missing-class-docstring

    def setUp(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def test_print_board(self):
        """Test that the print_board function prints the board to the terminal"""
        self.assertIsNone(print_board())
