import unittest
import random
from src.modular_version.game import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_check_tie_conditions_empty_board_returns_false(self):
        """
        Test that the check_for_tie method returns False
        when the board is empty
        """
        self.assertFalse(self.game.check_for_tie())

    def test_check_tie_conditions_board_no_tie_returns_false(self):
        """
        Test that the check_for_tie method returns False
        when there is no tie
        """
        self.game.board.enter_position("X", 1)
        self.game.board.enter_position("X", 5)
        self.game.board.enter_position("X", 8)
        self.game.board.enter_position("X", 4)
        self.game.board.enter_position("X", 0)
        self.assertFalse(self.game.check_for_tie())

    def test_check_tie_conditions_full_board_returns_true(self):
        """
        Test that the check_for_tie method returns True
        when the board is full
        """
        for i in range(self.game.board.size**2):
            self.game.board.enter_position(random.choice(("X", "O")), i)
        self.assertTrue(self.game.check_for_tie())

    def test_check_win_conditions_horizontal_win_returns_true(self):
        """
        Test that the check_for_win method returns True
        when there is a horizontal win
        """
        self.game.board.enter_position("X", 3)
        self.game.board.enter_position("X", 4)
        self.game.board.enter_position("X", 5)
        self.assertTrue(self.game.check_for_win("X"))

    def test_check_win_conditions_vertical_win_returns_true(self):
        """
        Test that the check_for_win method returns True
        when there is a vertical win
        """
        self.game.board.enter_position("X", 0)
        self.game.board.enter_position("X", 3)
        self.game.board.enter_position("X", 6)
        self.assertTrue(self.game.check_for_win("X"))

    def test_check_win_conditions_diagonal_win_returns_true(self):
        """
        Test that the check_for_win method returns True
        when there is a diagonal win
        """
        self.game.board.enter_position("X", 0)
        self.game.board.enter_position("X", 4)
        self.game.board.enter_position("X", 8)
        self.assertTrue(self.game.check_for_win("X"))

    def test_check_win_conditions_no_win_returns_false(self):
        """
        Test that the check_for_win method returns False
        when there is no win
        """
        self.game.board.enter_position("X", 0)
        self.game.board.enter_position("O", 4)
        self.game.board.enter_position("O", 8)
        self.assertFalse(self.game.check_for_win("X"))
        self.assertFalse(self.game.check_for_win("O"))
