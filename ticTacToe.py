from typing import Tuple

import numpy as np


class TicTacToe():
    def __init__(self):
        self.env = np.full((3, 3), '')
        self.action_space = 9  # TODO

    def reset(self):
        self.env = np.full((3, 3), '')

    def step(self, action: int, symbol: str) -> Tuple[bool, int]:

        def reward() -> int:
            return 1

        if action == 1 and self.env[0][0] == '':
            self.env[0][0] = symbol
            return True, reward()
        if action == 2:
            self.env[0][1] = symbol
            return True, reward()
        else:
            return False, reward()




if __name__ == "__main__":
    game = TicTacToe()
    game.reset()
    ok, r = game.step(action=1, symbol='X')
    print(r)
    print(ok)
    print(game.env)


    ok, r = game.step(action=2, symbol='O')
    print(r)
    print(ok)
    print(game.env)

    ok = game.step(action=1, symbol='O')
    print(r)
    print(ok)
    print(game.env)


