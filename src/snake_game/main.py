"""! @file
@brief The main flow of the game: set up the screen and the snake.

The flow follows the lecture "Screen Setup and Creating a Snake Body".
"""

from typing import Protocol

from snake_game.constants import (
    SCREEN_BACKGROUND_COLOR,
    SCREEN_HEIGHT,
    SCREEN_TITLE,
    SCREEN_WIDTH,
)
from snake_game.snake import Snake


class ScreenLike(Protocol):
    """! @brief What `configure_screen` needs from the screen.

    A `turtle.Screen` fits this description, and so does a fake in a test.
    """

    def setup(self, width: float, height: float) -> None:
        """! @brief Set the size of the window.

        @param width Width in pixels.
        @param height Height in pixels.
        """
        ...

    def bgcolor(self, color: str, /) -> None:
        """! @brief Set the background colour.

        @param color Name of the colour, for example `black`.
        """
        ...

    def title(self, titlestring: str, /) -> None:
        """! @brief Set the title of the window.

        @param titlestring The title.
        """
        ...


def configure_screen(screen: ScreenLike) -> None:
    """! @brief Give the screen the size, background colour and title of the game.

    @param screen The screen to set up.
    """
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor(SCREEN_BACKGROUND_COLOR)
    screen.title(SCREEN_TITLE)


def main() -> None:
    """! @brief Open the game window, draw the snake and wait for a click.

    `turtle` is imported here and not at the top of the module, so that importing
    this module needs neither a display nor `tkinter`.
    """
    from turtle import Screen

    screen = Screen()
    configure_screen(screen)
    Snake()  # draws its segments itself; the screen keeps the turtles alive
    screen.exitonclick()
