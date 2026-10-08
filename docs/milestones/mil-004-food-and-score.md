# MIL-004: Food and score

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-08 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

This gate decides whether the first half of the day-21 rules is done: food is shown at a random place, the snake eats it and grows, and the score on the scoreboard rises. It covers the day-21 steps "adding food", "detecting collisions between the snake and the food" and "updating the score", and the lesson on inheritance: `Food` and `Scoreboard` inherit from `Turtle`. The work is delivered on the branch `mil-004-food-and-score` and one pull request.

## Deliverable

`src/snake_game/food.py` with the class `Food`, `src/snake_game/scoreboard.py` with the class `Scoreboard`, `Snake.add_segment` and `Snake.extend` in `snake.py`, the eating check in `main.py`, the food and score constants in `constants.py`, the tests for each, and the README sections that describe food and score. Running the game shows food, the snake grows when it eats, and the score at the top rises.

The request gives day 21 only as an outline, so the numbers below are the usual values of the course and are **assumptions**. S01 confirms or replaces each against the lecture video before task 1 is started (Go/No-Go criterion 1).

| Value | Assumed | Constant |
| --- | --- | --- |
| Shape of the food | circle | `FOOD_SHAPE` |
| Size of the food | half the size of a default turtle (0.5 by 0.5) | `FOOD_SIZE` |
| Colour of the food | blue | `FOOD_COLOR` |
| Speed of the food | fastest, so that it does not animate when it moves | `FOOD_SPEED` |
| Wall, also the range of the random place of the food | 280 on every side | `WALL_LIMIT` |
| Distance at which the food is eaten | less than 15 pixels | `FOOD_COLLISION_DISTANCE` |
| Growth | one segment per food, at the place of the last segment | none |
| Points per food | 1 | none |
| Text of the scoreboard | `Score: ` followed by the score | `SCORE_LABEL` |
| Colour, place and alignment of the scoreboard | white, at (0, 270), centred | `SCOREBOARD_COLOR`, `SCOREBOARD_POSITION`, `SCOREBOARD_ALIGNMENT` |
| Font of the scoreboard | Arial, 24, normal | `SCOREBOARD_FONT` |

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The assumed values are confirmed | S01 confirmed or replaced every value of the table in the Deliverable section against the video, and the pull request lists the final values | A value is unconfirmed or missing from the pull request |
| 2 | Food is shown | A manual run shows one small blue circle at a random place inside the walls; a second run shows another place | No food, not a circle, or outside the walls |
| 3 | The snake eats | When the snake eats the food (the head comes closer than `FOOD_COLLISION_DISTANCE`), the food moves to a new random place, the snake grows by one segment and the score rises by 1; it works again for the next food | Any of the three does not happen, or the score rises without the food being eaten |
| 4 | Growth keeps the body joined | After eating while turning, the new segment appears at the place of the last segment and the segments show no gap | A gap, or a segment at the wrong place |
| 5 | The scoreboard shows the score | White text `Score: 0` at the top centre; after eating it shows `Score: 1` and the old text is gone | Text overlaps, is missing or is not at the top centre |
| 6 | The classes inherit | `Food` and `Scoreboard` are subclasses of `turtle.Turtle` and call `super().__init__()` | Either class does not inherit from `Turtle` |
| 7 | Constants are in one place | Every value of the table is a constant with a Doxygen comment, and no other module defines it | A value is a literal in another module |
| 8 | Day-20 behaviour is unchanged | The 61 tests of phase 1 still pass; the snake moves, turns, refuses a reversal and the window closes quietly | A regression |
| 9 | Tests prove the behaviour | `pytest` exits 0 with no display; tests cover the food, `refresh`, `add_segment` and `extend`, the scoreboard and `increase_score`, and eating (inside and outside the distance), using fakes only; importing `main` loads neither `turtle` nor `tkinter` | A failing test, or one of those behaviours has no test |
| 10 | `doxygen Doxyfile` builds | 0 warnings | Any warning |
| 11 | The code is reviewed | `RC-*` against `QC-PY-001` has the verdict `Go` | Verdict `No-Go` or `Go-with-conditions` |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-003] accepted and merged | The snake moves, has a head and `segments`, and the loop and the key bindings exist there |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 8: food, eating, growth, score, inheritance | [BC-001], criterion 9 in Success Criteria |
| Objective 2: the assignment's names (`Food`, `Scoreboard`, `extend`) | [BC-001], criterion 6 in Success Criteria |
| Objective 4: tests without a display | [BC-001], criterion 2 in Success Criteria |
| Objective 5: Doxygen and README | [BC-001], criteria 3, 4 in Success Criteria |
| Objective 6: traceable steps | [BC-001], criterion 7 in Success Criteria |
| Design of `Food`, `Scoreboard` and `Snake.extend`: no Design Class Diagram exists; they trace to the day-21 outline and to tasks 2 to 5 below, a recorded deviation from `QC-PY-001` criterion 10 as in [MIL-002] | [PP-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-17 — first of the two gateways of phase 2 (day 21), inside the plan of [PP-001] that ends 2026-10-21.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add the food and score constants | Add to `src/snake_game/constants.py` the constants of the table in the Deliverable section of this milestone (food shape, size, colour and speed; `WALL_LIMIT`; `FOOD_COLLISION_DISTANCE`; the scoreboard label, colour, position, alignment and font), each with a Doxygen comment, and extend `tests/test_constants.py` (the wall is inside the screen, the scoreboard is inside the screen, the eating distance is smaller than the move distance). Start only after S01 confirmed the values. | No | |
| 2 | Add the Food class | Create `src/snake_game/food.py` with `class Food(Turtle)`, as the lecture on inheritance teaches. `__init__` calls `super().__init__()`, then sets the shape, `penup`, `shapesize` (half size), colour and speed from the constants, and calls `refresh`. `refresh` sends the food to a random place with x and y between `-WALL_LIMIT` and `WALL_LIMIT`; the random numbers come from one small function so that a test can replace it. | No | |
| 3 | Make the snake grow | In `snake.py` move the body of the loop in `create_snake` into `add_segment(position)` (shape, colour, pen up, go to the position, append to `segments`) and add `extend`, which adds a segment at the place of the last segment. The `Segment` description gains `position`. The new segment must not break `move`: the body stays joined. | No | |
| 4 | Add the Scoreboard class | Create `src/snake_game/scoreboard.py` with `class Scoreboard(Turtle)`. `__init__` calls `super().__init__()`, starts `score` at 0, sets colour, pen up, hides the turtle and goes to the scoreboard place, then calls `update_scoreboard`. `update_scoreboard` clears the old text and writes the label and the score, centred, with the font. `increase_score` adds 1 and updates the text. | No | |
| 5 | Eat the food in the main flow | In `main` create the `Food` and the `Scoreboard` (imported there, so that importing `main` still needs neither `turtle` nor `tkinter`). In every frame call a small function that checks whether the head is closer to the food than `FOOD_COLLISION_DISTANCE`; if so it calls `food.refresh()`, `snake.extend()` and `scoreboard.increase_score()`. The `Segment` description gains `distance`. | No | |
| 6 | Test food, growth, score and eating without a display | Extend `tests/fakes.py` with a fake `Turtle` base class that records its calls, and install a fake `turtle` module before `food` and `scoreboard` are imported, because a class that inherits from `Turtle` needs the module at import time (see Open Issues of [PP-001]). Test the food (shape, colour, size, `refresh` inside the walls with a replaced random function), `add_segment` and `extend` (a segment at the place of the last one, the body joined after a turn), the scoreboard (text `Score: 0`, `Score: 1`, centred, old text cleared) and eating (inside the distance, at the distance, outside it). | No | |
| 7 | Update the README and the documentation | Describe food and score in the Run section of `README.md`, add `food.py` and `scoreboard.py` to the Project layout, and confirm that `doxygen Doxyfile` ends with 0 warnings. | No | |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-003]: ./mil-003-movement-and-keys.md
[MIL-002]: ./mil-002-screen-and-snake-body.md
