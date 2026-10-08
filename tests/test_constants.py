"""Tests of the constants that the four day-20 lectures fix."""

from snake_game import constants

HALF_WIDTH = constants.SCREEN_WIDTH / 2
HALF_HEIGHT = constants.SCREEN_HEIGHT / 2


def test_screen_size_matches_lecture() -> None:
    assert (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT) == (600, 600)


def test_screen_is_black_and_titled_as_in_the_lecture() -> None:
    assert constants.SCREEN_BACKGROUND_COLOR == "black"
    assert constants.SCREEN_TITLE == "My Snake Game"


def test_segments_are_white_squares() -> None:
    assert constants.SEGMENT_SHAPE == "square"
    assert constants.SEGMENT_COLOR == "white"


def test_snake_starts_with_three_segments_at_the_lecture_positions() -> None:
    assert constants.STARTING_POSITIONS == ((0, 0), (-20, 0), (-40, 0))


def test_starting_positions_are_distinct_on_one_row() -> None:
    positions = constants.STARTING_POSITIONS

    assert len(set(positions)) == len(positions)
    assert len({y for _, y in positions}) == 1


def test_starting_positions_run_from_head_to_tail_leftwards() -> None:
    x_values = [x for x, _ in constants.STARTING_POSITIONS]

    assert x_values == sorted(x_values, reverse=True)


def test_starting_positions_are_one_move_distance_apart() -> None:
    x_values = [x for x, _ in constants.STARTING_POSITIONS]
    gaps = {left - right for left, right in zip(x_values, x_values[1:], strict=False)}

    assert gaps == {constants.MOVE_DISTANCE}


def test_starting_positions_are_inside_the_screen() -> None:
    assert all(
        abs(x) < HALF_WIDTH and abs(y) < HALF_HEIGHT
        for x, y in constants.STARTING_POSITIONS
    )


def test_move_distance_is_twenty_pixels() -> None:
    assert constants.MOVE_DISTANCE == 20


def test_directions_match_the_lecture_headings() -> None:
    assert constants.UP == 90
    assert constants.DOWN == 270
    assert constants.LEFT == 180
    assert constants.RIGHT == 0


def test_four_directions_are_distinct() -> None:
    directions = (constants.UP, constants.DOWN, constants.LEFT, constants.RIGHT)

    assert len(set(directions)) == len(directions)


def test_opposite_directions_differ_by_half_a_turn() -> None:
    assert (constants.UP - constants.DOWN) % 360 == 180
    assert (constants.LEFT - constants.RIGHT) % 360 == 180


def test_refresh_delay_is_a_tenth_of_a_second() -> None:
    assert constants.REFRESH_DELAY_SECONDS == 0.1
