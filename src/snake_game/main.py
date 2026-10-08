"""! @file
@brief The main flow of the game: set up the screen, draw the snake and run it.

The flow follows the lectures "Screen Setup and Creating a Snake Body",
"Animating the Snake Segments on Screen" and "Controlling the Snake with
Keypresses".
"""

import time
from collections.abc import Callable
from typing import Protocol

from snake_game.constants import (
    REFRESH_DELAY_SECONDS,
    SCREEN_BACKGROUND_COLOR,
    SCREEN_HEIGHT,
    SCREEN_TITLE,
    SCREEN_WIDTH,
)
from snake_game.snake import Snake


class ScreenLike(Protocol):
    """! @brief What the helper functions need from the screen.

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

    def update(self) -> None:
        """! @brief Draw everything that has changed since the last update."""
        ...

    def listen(self) -> None:
        """! @brief Make the screen receive the key presses."""
        ...

    def onkey(self, fun: Callable[[], object], key: str) -> None:
        """! @brief Call a function when a key is pressed.

        @param fun The function to call.
        @param key Name of the key, for example `Up`.
        """
        ...


def configure_screen(screen: ScreenLike) -> None:
    """! @brief Give the screen the size, background colour and title of the game.

    @param screen The screen to set up.
    """
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor(SCREEN_BACKGROUND_COLOR)
    screen.title(SCREEN_TITLE)


def bind_keys(screen: ScreenLike, snake: Snake) -> None:
    """! @brief Turn the snake with the arrow keys.

    @param screen The screen that receives the key presses.
    @param snake The snake to steer.
    """
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


def play_frame(screen: ScreenLike, snake: Snake) -> None:
    """! @brief Show the snake, wait for `REFRESH_DELAY_SECONDS`, then move it.

    This is one pass of the animation loop. The screen is updated by hand because
    automatic drawing is off, so the whole snake appears at once.

    @param screen The screen to update.
    @param snake The snake to move.
    """
    screen.update()
    time.sleep(REFRESH_DELAY_SECONDS)
    snake.move()


def main() -> None:
    """! @brief Open the game window and run the snake until the window is closed.

    Closing the window during the animation loop makes `screen.update()` raise
    `tkinter.TclError` ("invalid command name"), and `turtle` raises
    `turtle.Terminator` in some other calls once its window is gone. Both mean
    "the player closed the window", so the game ends quietly with exit code 0.
    `screen.exitonclick()` after the loop waits for a click once the game is over,
    which the day-21 rules will cause.

    `turtle` and `tkinter` are imported here and not at the top of the module, so
    that importing this module needs neither a display nor `tkinter`.
    """
    from tkinter import TclError
    from turtle import Screen, Terminator

    screen = Screen()
    configure_screen(screen)
    screen.tracer(0)
    snake = Snake()
    bind_keys(screen, snake)

    game_is_on = True
    try:
        while game_is_on:
            play_frame(screen, snake)
        screen.exitonclick()
    except (Terminator, TclError):
        return  # the window was closed: there is nothing left to do
