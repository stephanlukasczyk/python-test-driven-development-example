from typing import List


class TicTacToe:

    def __init__(self) -> None:
        self._board: List[List[str]] = [
            ["\0", "\0", "\0"],
            ["\0", "\0", "\0"],
            ["\0", "\0", "\0"],
        ]

    def play(self, x: int, y: int) -> None:
        if x < 1 or x > 3:
            raise RuntimeError("X is outside board")
        if y < 1 or y > 3:
            raise RuntimeError("Y is outside board")
        if self._board[x - 1][y - 1] != "\0":
            raise RuntimeError("Slot is occupied")
        self._board[x - 1][y - 1] = "X"
