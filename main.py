"""Main module that runs the tic-tac-toe game."""
from src.modular_version.game import Game


def main():
    """Main function that runs the tic-tac-toe game, starts the main game loop when called."""
    game = Game()
    game.play()


if __name__ == "__main__":
    main()
