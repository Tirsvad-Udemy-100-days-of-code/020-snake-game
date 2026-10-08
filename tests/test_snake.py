"""Tests of the snake body, with fakes instead of real turtles."""

import pytest

from fakes import FakeSegment, imports_turtle, install_fake_turtle
from snake_game import constants
from snake_game.snake import Snake


def make_snake() -> tuple[Snake, list[FakeSegment]]:
    """Make a snake whose segments are fakes, and return the fakes too."""
    created: list[FakeSegment] = []

    def factory() -> FakeSegment:
        segment = FakeSegment()
        created.append(segment)
        return segment

    return Snake(segment_factory=factory), created


def test_snake_has_one_segment_per_starting_position() -> None:
    snake, _ = make_snake()

    assert len(snake.segments) == len(constants.STARTING_POSITIONS) == 3


def test_segments_are_the_created_turtles_in_order() -> None:
    snake, created = make_snake()

    assert snake.segments == created


def test_segments_are_white_squares() -> None:
    _, created = make_snake()

    for segment in created:
        assert ("shape", ("square",)) in segment.calls
        assert ("color", ("white",)) in segment.calls


def test_segments_are_placed_at_the_starting_positions_head_first() -> None:
    _, created = make_snake()

    positions = [segment.calls[-1] for segment in created]

    assert positions == [
        ("goto", position) for position in constants.STARTING_POSITIONS
    ]


def test_pen_is_lifted_before_a_segment_is_moved() -> None:
    _, created = make_snake()

    for segment in created:
        names = segment.call_names()
        assert names.count("goto") == 1
        assert names.index("penup") < names.index("goto")


def test_create_snake_adds_three_more_segments_when_called_again() -> None:
    snake, _ = make_snake()

    snake.create_snake()

    assert len(snake.segments) == 2 * len(constants.STARTING_POSITIONS)


def test_default_segment_factory_makes_turtles(monkeypatch: pytest.MonkeyPatch) -> None:
    turtles, _ = install_fake_turtle(monkeypatch)

    snake = Snake()

    assert snake.segments == turtles
    assert len(turtles) == len(constants.STARTING_POSITIONS)


def test_importing_the_snake_module_does_not_import_turtle() -> None:
    assert not imports_turtle("snake_game.snake")
