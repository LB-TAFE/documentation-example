import unittest
from src.modular_version.board import Board


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_validate_position_out_of_bounds_returns_false(self):
        self.assertFalse(self.board.check_for_valid_position("19"))
        self.assertFalse(self.board.check_for_valid_position("31"))
        self.assertFalse(self.board.check_for_valid_position("100"))
        self.assertFalse(self.board.check_for_valid_position("9"))
        self.assertFalse(self.board.check_for_valid_position("-1"))
        self.assertFalse(self.board.check_for_valid_position("O1"))
        self.assertFalse(self.board.check_for_valid_position("A"))
        self.assertFalse(self.board.check_for_valid_position("1AA"))

    def test_validate_position_valid_position_returns_true(self):
        self.assertTrue(self.board.check_for_valid_position("0"))
        self.assertTrue(self.board.check_for_valid_position("1"))
        self.assertTrue(self.board.check_for_valid_position("2"))
        self.assertTrue(self.board.check_for_valid_position("3"))
        self.assertTrue(self.board.check_for_valid_position("4"))
        self.assertTrue(self.board.check_for_valid_position("5"))
        self.assertTrue(self.board.check_for_valid_position("6"))
        self.assertTrue(self.board.check_for_valid_position("7"))
        self.assertTrue(self.board.check_for_valid_position("8"))

    def test_validate_position_filled_position_returns_false(self):
        self.board.enter_position("X", 0)
        self.board.enter_position("X", 7)
        self.board.check_for_valid_position("0")
        self.board.check_for_valid_position("7")

    def test_get_position_returns_correct_character(self):
        self.board.nodes[2][1] = "X"
        self.board.nodes[2][0] = "?"

        self.assertEqual(self.board.get_position(7), "X")
        self.assertEqual(self.board.get_position(6), "?")
        self.assertEqual(self.board.get_position(5), self.board.empty)

    def test_enter_position_sets_correctly(self):
        self.board.enter_position("X", 7)
        self.board.enter_position("X", 3)

        self.assertEqual(self.board.nodes[1][0], "X")
        self.assertEqual(self.board.nodes[2][1], "X")
