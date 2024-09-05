class Board:
    """
    Board class for a Tic Tac Toe game.
    """

    def __init__(self, size=3, empty=" "):
        self.size = size
        self.empty = empty
        self.nodes = [[self.empty for _ in range(size)] for _ in range(size)]

    def check_for_valid_position(self, position: str) -> bool:
        """
        Checks if a position on the board is within the board's bounds and is not marked by a character.

        :param position: int
        :return: bool
        """
        if not position.isdigit():
            return False
        position = int(position)
        if position not in range(self.size**2):
            return False
        if self.get_position(position) != " ":
            return False
        return True

        # TODO: Simplify checks to one line (optional)

    def display(self):
        """
        Prints the board to the terminal.

        :return: None
        """
        print(
            f"\n{"--"*self.size}\n".join(["|".join(row) for row in self.nodes]))
        print("\n"*5)

    def enter_position(self, char: str, position: int):
        """
        Sets a position on the board to a specified character.

        :param char: str
        :param position: int
        :return: None
        """
        self.nodes[position // self.size][position % self.size] = char

    def get_position(self, position: int) -> str:
        """
        Gets the character at a given position on the board.

        :param position: int
        :return: str
        """
        return self.nodes[position // self.size][position % self.size]
