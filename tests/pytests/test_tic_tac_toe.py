from src.script_version.tic_tac_toe import is_win, tally_wins


def test_is_win_no_win():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    assert not is_win('X')
    assert not is_win('O')


def test_is_win_row_win():
    board = [['X', 'X', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]
    assert is_win('X')
