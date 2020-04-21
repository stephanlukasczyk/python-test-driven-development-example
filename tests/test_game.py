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


def test_when_occupied_then_runtime_error(tictactoe):
    tictactoe.play(2, 1)
    with pytest.raises(RuntimeError):
        tictactoe.play(2, 1)


def test_given_first_turn_when_next_player_then_x(tictactoe):
    assert tictactoe.next_player == "X"


def test_given_last_turn_was_x_when_next_player_then_o(tictactoe):
    tictactoe.play(1, 1)
    assert tictactoe.next_player == "O"
