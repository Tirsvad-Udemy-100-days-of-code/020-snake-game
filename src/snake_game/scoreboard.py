"""! @file
@brief The scoreboard: the text at the top of the screen that shows the score.

The class follows the day-21 lecture on inheritance: `Scoreboard` is a `Turtle`
that writes text. Like `food`, this module needs `turtle` when it is imported;
the game imports it only when it starts, and the tests install a fake `turtle`
module first.
"""

from turtle import Turtle

from snake_game.constants import (
    SCORE_LABEL,
    SCOREBOARD_ALIGNMENT,
    SCOREBOARD_COLOR,
    SCOREBOARD_FONT,
    SCOREBOARD_POSITION,
)


class Scoreboard(Turtle):
    """! @brief Shows the score as text at the top centre of the screen."""

    def __init__(self) -> None:
        """! @brief Set the scoreboard up and write the score 0."""
        super().__init__()
        ## @brief The number of foods the snake has eaten in this game.
        self.score = 0
        self.color(SCOREBOARD_COLOR)
        self.penup()
        self.hideturtle()
        self.goto(SCOREBOARD_POSITION)
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        """! @brief Wipe the old text and write the label and the score."""
        self.clear()
        self.write(
            f"{SCORE_LABEL}{self.score}",
            align=SCOREBOARD_ALIGNMENT,
            font=SCOREBOARD_FONT,
        )

    def increase_score(self) -> None:
        """! @brief Add 1 to the score and write it."""
        self.score += 1
        self.update_scoreboard()
