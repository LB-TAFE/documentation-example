from src.script_version.tic_tac_toe import is_win, tally_wins


def test_is_win_no_win():
    """Test is_win function with no win conditions"""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    assert not is_win('X')
    assert not is_win('O')


def test_is_win_row_win():
    """Test is_win function with a row win condition"""
    board = [['X', 'X', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]
    assert is_win('X', board)


def test_is_win_column_win():
    """Test is_win function with a column win condition"""
    board = [['X', ' ', ' '], ['X', ' ', ' '], ['X', ' ', ' ']]
    assert is_win('X', board)


def test_is_win_diagonal_win():
    """Test is_win function with a diagonal win condition"""
    board = [['X', ' ', ' '], [' ', 'X', ' '], [' ', ' ', 'X']]
    assert is_win('X', board)
