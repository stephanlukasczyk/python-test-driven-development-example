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


def test_when_play_then_no_winner(tictactoe):
    actual = tictactoe.play(1, 1)
    assert actual == "No winner"


def test_when_play_and_whole_horizontal_line_then_winner(tictactoe):
    tictactoe.play(1, 1)  # X
    tictactoe.play(1, 2)  # O
    tictactoe.play(2, 1)  # X
    tictactoe.play(2, 2)  # O
    actual = tictactoe.play(3, 1)  # X
    assert actual == "X is the winner"


def test_when_play_and_whole_vertical_line_then_winner(tictactoe):
    tictactoe.play(2, 1)  # X
    tictactoe.play(1, 1)  # O
    tictactoe.play(3, 1)  # X
    tictactoe.play(1, 2)  # O
    tictactoe.play(2, 2)  # X
    actual = tictactoe.play(1, 3)  # O
    assert actual == "O is the winner"


def test_when_play_and_top_bottom_diagonal_line_then_winner(tictactoe):
    tictactoe.play(1, 1)  # X
    tictactoe.play(1, 2)  # O
    tictactoe.play(2, 2)  # X
    tictactoe.play(1, 3)  # O
    actual = tictactoe.play(3, 3)  # X
    assert actual == "X is the winner"
