## @file constants.py
#  @brief Constants of the snake game.
#
#  Every value that the four day-20 lectures fix lives here, so that no other
#  module contains a magic number. The turtle coordinate system has its centre
#  at (0, 0); the 600 by 600 screen therefore reaches from -300 to 300 on both
#  axes. A direction is a turtle heading in degrees: 0 points right and the
#  angle grows counter-clockwise.

"""Constants of the snake game, as fixed by the four day-20 lectures."""

from typing import Final

## @brief Width of the screen in pixels.
SCREEN_WIDTH: Final[int] = 600

## @brief Height of the screen in pixels.
SCREEN_HEIGHT: Final[int] = 600

## @brief Background colour of the screen.
SCREEN_BACKGROUND_COLOR: Final[str] = "black"

## @brief Title of the game window.
SCREEN_TITLE: Final[str] = "My Snake Game"

## @brief Shape of every segment of the snake.
SEGMENT_SHAPE: Final[str] = "square"

## @brief Colour of every segment of the snake.
SEGMENT_COLOR: Final[str] = "white"

## @brief Where the segments are drawn when the game starts, from head to tail.
#
#  The positions lie on one row, 20 pixels apart, which is the width of a
#  default turtle square, so the segments touch without overlapping.
STARTING_POSITIONS: Final[tuple[tuple[int, int], ...]] = ((0, 0), (-20, 0), (-40, 0))

## @brief Distance in pixels that the head moves in one move.
MOVE_DISTANCE: Final[int] = 20

## @brief Direction up, as a turtle heading in degrees.
UP: Final[int] = 90

## @brief Direction down, as a turtle heading in degrees.
DOWN: Final[int] = 270

## @brief Direction left, as a turtle heading in degrees.
LEFT: Final[int] = 180

## @brief Direction right, as a turtle heading in degrees.
RIGHT: Final[int] = 0

## @brief Wait in seconds between two moves.
REFRESH_DELAY_SECONDS: Final[float] = 0.1
