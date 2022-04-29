from typing import Tuple

import numpy as np


class TicTacToe():
    def __init__(self):
        self.env = np.full((3, 3), '')
        self.action_space = 9  # TODO

    def reset(self):
        self.env = np.full((3, 3), '')

    def step(self, action: int, symbol: str) -> Tuple[bool, int]:

        def done() -> bool:
            pass

        def reward() -> int:
            return 1

        if action == 0 and self.env[0][0] == '':
            self.env[0][0] = symbol
            return True, reward()
        if action == 1:
            self.env[0][1] = symbol
            return True, reward()
        if action == 2:
            self.env[0][2] = symbol
            return True, reward()
        if action == 3:
            self.env[1][0] = symbol
            return True, reward()
        if action == 4:
            self.env[1][1] = symbol
            return True, reward()
        if action == 5:
            self.env[1][2] = symbol
            return True, reward()
        if action == 6:
            self.env[2][0] = symbol
            return True, reward()
        if action == 7:
            self.env[2][1] = symbol
            return True, reward()
        if action == 8:
            self.env[2][2] = symbol
            return True, reward()
        else:
            return False, reward()


if __name__ == "__main__":
    game = TicTacToe()
    game.reset()

    for i in range(9):
        if i % 2 == 0:
            game.step(action=i, symbol='X')
        else:
            game.step(action=i, symbol='O')
        print(game.env)
