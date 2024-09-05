from .board import Board


class Game:

    def __init__(self):

        self.board = Board()
        self.player_one = "X"
        self.player_two = "O"
        self.current_player = self.player_one

    def get_input(self, player: str) -> int:
        """
        Prompts the player to enter a position on the board, loops until a valid position is entered.

        :param player:
        :return: int
        """
        while True:
            move = input(f"Next move for player {
                         player} (0-{self.board.size**2-1}): ")
            if not self.board.check_for_valid_position(move):
                print("Invalid move, try again.")
                continue
            return int(move)

    def check_for_win(self, player: str) -> bool:
        """
        Checks if any of the game's win conditions have been met for a specific player.

        :param player:
        :return: bool
        """
        # To allow the board's size to be changed, algorithms have been made to check if a win condition is met
        # rather than hardcoding win positions.
        # This is split up into 3 methods for readability.
        return any([self.__check_horizontal_wins(player), self.__check_vertical_wins(player), self.__check_diagonal_wins(player)])

    def __check_horizontal_wins(self, player: str) -> bool:
        """
        Checks if there is a horizontal line in the board.

        :param player:
        :return: bool
        """
        return any([all([char == player for char in row]) for row in self.board.nodes])

    def __check_vertical_wins(self, player: str) -> bool:
        """
        Checks if there is a vertical line in the board.

        :param player:
        :return: bool
        """
        # TODO: Refactor into a one-line return statement (optional)
        for column in range(self.board.size):
            if all([self.board.nodes[row][column] == player for row in range(self.board.size)]):
                return True
        return False

    def __check_diagonal_wins(self, player: str) -> bool:
        """
        Checks if there is a diagonal line in the board.

        :param player:
        :return: bool
        """
        # TODO: Simplify algorithm (optional)
        results = [True, True]
        for position in range(self.board.size-1, self.board.size**2-(self.board.size-1), self.board.size-1):
            if self.board.get_position(position) != player:
                results[0] = False
                break

        for position in range(0, self.board.size**2, self.board.size+1):
            if self.board.get_position(position) != player:
                results[1] = False
                break

        return any(results)

    def check_for_tie(self) -> bool:
        """
        Checks if there is a tie in the board. (Currently a tie is defined as there being no possible moves left)

        :return: bool
        """
        # TODO: Refactor into one line (optional)
        # TODO: Refactor to check if win conditions are impossible instead of checking for no playable moves (optional)
        for row in self.board.nodes:
            if " " in row:
                return False
        return True

    def play(self):
        """
        Main game loop, used to start a game of tic-tac-toe.

        :return: None
        """
        while True:
            self.board.display()
            move = self.get_input(self.current_player)
            self.board.enter_position(self.current_player, move)

            if self.check_for_win(self.current_player):
                self.board.display()
                print(f"Player {self.current_player} wins!")
                break

            if self.check_for_tie():
                self.board.display()
                print("It's a tie!")
                break
            self.current_player = self.player_two if (
                self.current_player == self.player_one) else self.player_one
