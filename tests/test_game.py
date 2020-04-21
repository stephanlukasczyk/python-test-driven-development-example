import pytest

from tictactoe.game import TicTacToe


@pytest.fixture
def tictactoe():
    return TicTacToe()


def test_when_x_outside_board_then_runtime_error(tictactoe):
    with pytest.raises(RuntimeError):
        tictactoe.play(5, 2)


def test_when_y_outside_board_then_runtime_error(tictactoe):
    with pytest.raises(RuntimeError):
        tictactoe.play(2, 5)
