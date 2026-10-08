# Domain Dictionary: Snake Game

## Metadata
| Key | Value |
| --- | --- |
| ID | DICT-001 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-08 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [a2c997e] |
| 2026-10-08 | Accepted | Jens Tirsvad Nielsen | S01 | Added the day-21 terms (food, eat, grow, score, scoreboard, wall, touch, game over); tail now means every segment behind the head | [710784f] |

---

## Purpose and Scope

Maps each Product Owner (PO) term to its professional IT term. PO language:
`en` (domain `it`), from the registry's `Languages` section. The PO terms are
the words of the lectures of days 20 and 21 as the planning documents use them; the IT
terms are the names in the code. The dictionary covers the vocabulary of the
game; it exists so that the planning documents use one word for one thing and so
that S02 can find the lectures' names in the code.

## Dictionary

| PO term | Language | IT term | Definition | Used as PO term in | Used as IT term in |
| --- | --- | --- | --- | --- | --- |
| window | en | Tk window | The desktop window that holds the screen and is opened when the game starts. | BC, SA, PP, MIL | PY |
| screen | en | `Screen` | The drawing area that the game sets up (size, colour, title) and on which the snake is shown. | BC, SA, PP, MIL | PY |
| snake | en | `Snake` | The creature the player steers, made of segments. | BC, SA, PP, MIL | PY |
| segment | en | `Turtle` | One white square of the snake. | BC, SA, PP, MIL | PY |
| head | en | `head` | The first segment, which leads the snake and is turned by the arrow keys. | BC, SA, PP, MIL | PY |
| tail | en | `segments[1:]` | Every segment behind the head; the game is over when the head touches one of them. | BC, MIL | PY |
| body | en | `segments` | All segments of the snake, the head included, in order, the head first. | BC, SA, PP, MIL | PY |
| starting position | en | `STARTING_POSITIONS` | One of the three places at which a segment is drawn when the game starts. | BC, MIL | PY |
| move | en | `move` | One pass in which each segment takes the place of the one before it and the head goes forward by the move distance. | BC, SA, PP, MIL | PY |
| move distance | en | `MOVE_DISTANCE` | How far the head goes in one move, 20 pixels. | BC, MIL | PY |
| direction | en | `heading` | The way the head points: up, down, left or right. | BC, SA, PP, MIL | PY |
| reversal | en | opposite heading | A turn by 180 degrees, so that the head would run into the segment behind it. | BC, SA, PP, MIL | PY |
| arrow key | en | key name `"Up"`, `"Down"`, `"Left"`, `"Right"` | One of the four keys with which the player turns the head. | BC, SA, PP, MIL | PY |
| key binding | en | `onkey` | The link between an arrow key and the method that turns the head. | BC, PP, MIL | PY |
| animation loop | en | `while game_is_on` loop | The loop that refreshes the screen, waits and makes one move, again and again. | BC, PP, MIL | PY |
| refresh delay | en | `REFRESH_DELAY_SECONDS` | The wait between two moves, 0.1 seconds. | BC, MIL | PY |
| food | en | `Food` | The small dot that the snake eats; it is shown at a random place and moves to a new random place when it is eaten. | BC, SA, PP, MIL | PY |
| eat | en | `FOOD_COLLISION_DISTANCE` | The head comes closer to the food than this distance, which makes the snake grow and the score rise. | BC, MIL | PY |
| grow | en | `extend` | The snake gets one more segment, at the place where its last segment is. | BC, MIL | PY |
| score | en | `score` | The number of foods the snake has eaten in this game. | BC, SA, PP, MIL | PY |
| scoreboard | en | `Scoreboard` | The text at the top of the screen that shows the score. | BC, MIL | PY |
| wall | en | `WALL_LIMIT` | The edge of the playing field on every side; the head must stay inside it and the food is shown inside it. | BC, SA, PP, MIL | PY |
| touch | en | `TAIL_COLLISION_DISTANCE` | The head comes closer to a segment of the tail than this distance. | BC, MIL | PY |
| game over | en | `game_over` | The end of the game, shown with the text GAME OVER, when the head passes the wall or touches the tail. | BC, SA, PP, MIL | PY |

## Rules

- The Business Case, Stakeholder Analysis, Project Plan and milestones use the
  PO term; the source code and its tests use the IT term. The other design
  artifacts (Domain Model, Operation Contract, Sequence Diagram, Design Class
  Diagram, ERD) do not exist in this project.
- One IT term per PO term and one PO term per IT term; no synonyms.
- The planning documents use British spelling (colour, centre); identifiers such
  as `color` follow the `turtle` module and the lectures.
- A code identifier written in backticks in a planning document is an IT term
  and is allowed there.
- "Step" is not a PO term of the game. In the planning documents it means a step
  of the project (a task, a milestone), never a move of the snake.

---

[BC-001]: ./business-case.md
[SA-001]: ./stakeholder-analysis.md
[a2c997e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/020-snake-game/commit/a2c997e1413e425050df8c50a976ec839ebb4752
[710784f]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/020-snake-game/commit/710784f2243e7ecf8cec23cbdd9cc58c96cdff96
