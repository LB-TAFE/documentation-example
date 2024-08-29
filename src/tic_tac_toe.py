"""A simple command-line tic-tac-toe game.

The game is played within the terminal when this file is run. No functionality here is intended to be imported elsewhere.

Usage:
    python tic_tac_toe.py
"""
board = [[' ' for _ in range(3)] for _ in range(3)]


def print_board():
    """Prints the tic-tac-toe board to the terminal"""
    for row in board:
        print('|'.join(row))
        print('-' * 5)


def is_win(player: str) -> bool:
    """Checks if a player has won the game through a row, column, or diagonal
    
    Args:
        :player - str: The character that represents a player.

    Returns:
        - bool: True if a row, column or diagonal win condition has been met, False otherwise


    """
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def tally_wins(results: list[bool]) -> int:
    """Tallies the number of wins for each player
    
    Args:
        :results - list[bool]: A list of boolean values representing the win status of each game played.

    Returns:
        - int: The number of wins for the player who won the most games.
    """
    return sum(results)


def main():
    """Main function that runs the tic-tac-toe game, starts the main game loop when called."""
    current_player = 'X'
    moves = 0
    results = []

    while moves < 9:
        print_board()
        try:
            row, col = map(int, input(f"Player {
                           current_player}, enter row and column (0-2) separated by space: ").split())
            if board[row][col] == ' ':
                board[row][col] = current_player
                win = is_win(current_player)
                results.append(win)
                if win:
                    print_board()
                    print(f"Player {current_player} wins!")
                    return
                current_player = 'O' if current_player == 'X' else 'X'
                moves += 1
            else:
                print("Cell already occupied! Try again.")
        except ValueError:
            print("Invalid input! Please enter two integers separated by space.")
        except IndexError:
            print(
                "Invalid input! Please enter row and column values within the range (0-2).")
    print_board()
    print("It's a draw!")
    print(f"Number of wins during the game: {tally_wins(results)}")


if __name__ == "__main__":
    main()
else:
    raise ImportError(
        "This module is not intended to be imported. Please run the file directly.")
