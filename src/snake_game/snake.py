"""! @file
@brief The snake: a list of square segments that the game draws.

The class follows the lecture "Create a Snake Class & Move to OOP". It keeps the
lecture's names: `Snake`, `segments` and `create_snake`. The only difference is
that the snake gets the function that makes a segment as a parameter, so that a
test can pass a fake and needs no window.
"""

from collections.abc import Callable
from typing import Protocol

from snake_game.constants import SEGMENT_COLOR, SEGMENT_SHAPE, STARTING_POSITIONS


class Segment(Protocol):
    """! @brief What the snake needs from one of its segments.

    A `turtle.Turtle` fits this description, and so does a fake in a test.
    """

    def shape(self, name: str, /) -> object:
        """! @brief Set the shape of the segment.

        @param name Name of the shape, for example `square`.
        @return Whatever the implementation returns; the snake ignores it.
        """
        ...

    def color(self, color: str, /) -> object:
        """! @brief Set the colour of the segment.

        @param color Name of the colour, for example `white`.
        @return Whatever the implementation returns; the snake ignores it.
        """
        ...

    def penup(self) -> None:
        """! @brief Lift the pen, so that moving the segment draws no line."""
        ...

    def goto(self, x: float, y: float, /) -> None:
        """! @brief Send the segment to a position.

        @param x The x coordinate.
        @param y The y coordinate.
        """
        ...


def make_turtle_segment() -> Segment:
    """! @brief Make a real turtle, the default way to get a segment.

    `turtle` is imported here and not at the top of the module, so that
    importing the snake needs neither a display nor `tkinter`.

    @return A new `turtle.Turtle`.
    """
    from turtle import Turtle

    return Turtle()


class Snake:
    """! @brief The snake of the game, drawn as a row of square segments."""

    def __init__(self, segment_factory: Callable[[], Segment] | None = None) -> None:
        """! @brief Create the snake with its three starting segments.

        @param segment_factory Makes one new segment; defaults to a real turtle.
        """
        ## @brief Makes one new segment.
        self._segment_factory = segment_factory or make_turtle_segment
        ## @brief The segments of the snake, the head first.
        self.segments: list[Segment] = []
        self.create_snake()

    def create_snake(self) -> None:
        """! @brief Draw one white square segment at each starting position.

        The pen is lifted before a segment is sent to its position, so no line is
        drawn. The segments are kept in `segments`, the head first.
        """
        for x, y in STARTING_POSITIONS:
            new_segment = self._segment_factory()
            new_segment.shape(SEGMENT_SHAPE)
            new_segment.color(SEGMENT_COLOR)
            new_segment.penup()
            new_segment.goto(x, y)
            self.segments.append(new_segment)
