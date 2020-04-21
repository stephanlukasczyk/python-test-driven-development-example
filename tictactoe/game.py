from typing import List


class TicTacToe:

    def __init__(self) -> None:
        self._board: List[List[str]] = [
            ["\0", "\0", "\0"],
            ["\0", "\0", "\0"],
            ["\0", "\0", "\0"],
        ]
        self._last_player = "\0"
        self._size = 3

    def play(self, x: int, y: int) -> str:
        self._check_axis(x)
        self._check_axis(y)
        self._last_player = self.next_player
        self._set_box(x, y, self._last_player)
        if self._is_win():
            return f"{self._last_player} is the winner"
        return "No winner"

    @staticmethod
    def _check_axis(axis: int) -> None:
        if axis < 1 or axis > 3:
            raise RuntimeError("Tile outside board")

    def _set_box(self, x: int, y: int, last_player: str) -> None:
        if self._board[x - 1][y - 1] != "\0":
            raise RuntimeError("Slot is occupied")
        self._board[x - 1][y - 1] = last_player

    @property
    def next_player(self) -> str:
        if self._last_player == "X":
            return "O"
        return "X"

    def _is_win(self) -> bool:
        for i in range(self._size):
            if (
                self._board[0][i] == self._last_player
                and self._board[1][i] == self._last_player
                and self._board[2][i] == self._last_player
            ):
                return True
            if (
                self._board[i][0] == self._last_player
                and self._board[i][1] == self._last_player
                and self._board[i][2] == self._last_player
            ):
                return True
        return False
