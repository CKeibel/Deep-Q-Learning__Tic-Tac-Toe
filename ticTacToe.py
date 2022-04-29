import numpy as np


class TicTacToe():
    def __init__(self):
        self.env = np.full((3, 3), '')
        self.action_space = 9  # TODO

    def reset(self):
        self.env = np.full((3, 3), '')

    def step(self, action: int):
        pass


if __name__ == "__main__":
    game = TicTacToe()
    game.env[0][0] = 'X'
    print(game.env)

    game.reset()
    print(game.env)
