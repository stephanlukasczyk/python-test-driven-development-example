class TicTacToe:

    def play(self, x: int, y: int) -> None:
        if x < 1 or x > 3:
            raise RuntimeError("X is outside board")
        if y < 1 or y > 3:
            raise RuntimeError("Y is outside board")
