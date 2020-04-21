from typing import List


class TicTacToe:

    def __init__(self) -> None:
        self._board: List[List[str]] = [
            ["\0", "\0", "\0"],
            ["\0", "\0", "\0"],
            ["\0", "\0", "\0"],
        ]

    def play(self, x: int, y: int) -> None:
        self._check_axis(x)
        self._check_axis(y)
        self._set_box(x, y)

    @staticmethod
    def _check_axis(axis: int) -> None:
        if axis < 1 or axis > 3:
            raise RuntimeError("Tile outside board")

    def _set_box(self, x: int, y: int) -> None:
        if self._board[x - 1][y - 1] != "\0":
            raise RuntimeError("Slot is occupied")
        self._board[x - 1][y - 1] = "X"
