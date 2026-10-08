# MIL-002: Screen and snake body

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-08 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [a2c997e] |
| 2026-10-08 | Accepted | Jens Tirsvad Nielsen | S01 | Recorded that the `Snake` class has no Design Class Diagram and traces to the lecture (Traceability) | pending |

---

## Purpose

This gate decides whether the first lecture and the class part of the third are done: the game window is set up and the three-segment snake is drawn by a `Snake` class. It covers the lecture "Screen Setup and Creating a Snake Body" and the class part of "Create a Snake Class & Move to OOP" (OOP is object-oriented programming). The work is delivered on the branch `mil-002-screen-and-snake-body` and one pull request.

## Deliverable

`src/snake_game/snake.py` with the class `Snake` (a `segments` list and `create_snake`), `src/snake_game/main.py` with the screen set-up and a `main` function, `src/snake_game/__main__.py` so that `python -m snake_game` starts the game, and the tests `tests/test_snake.py` and `tests/test_main.py`. Running the game shows the static snake until the window is clicked.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The window matches the lecture | A manual run by S01 shows a 600 by 600 black window titled "My Snake Game" that closes on a click | Size, colour, title or the click-to-close differs |
| 2 | The snake body is drawn | A manual run shows three white squares side by side on one row, touching, with the head at the centre of the window | Fewer or more than three segments, a gap or an overlap, or a trail drawn behind a segment |
| 3 | `Snake` follows the lecture | The class lives in `snake.py`, has `segments` (a list) and `create_snake`, builds one segment per entry of `STARTING_POSITIONS`, lifts the pen before moving a segment, and uses no literal for a position, shape or colour | A name is different, or a value is a literal in `snake.py` |
| 4 | The window code is testable | `configure_screen` takes the screen as a parameter, and `Snake` takes its segment factory as a parameter; `turtle` is imported only inside the default factory and in `main` | `snake.py` imports `turtle` at module level, or a test needs a display |
| 5 | Tests prove the body | `pytest` exits 0; tests cover the number, shape, colour, order and positions of the segments and the screen settings, using fakes only | A failing test, or one of those behaviours has no test |
| 6 | `doxygen Doxyfile` builds | 0 warnings; every public name has a Doxygen comment | Any warning |
| 7 | The code is reviewed | `RC-*` against `QC-PY-001` has the verdict `Go` | Verdict `No-Go` or `Go-with-conditions` |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-001] accepted and merged | The package, `constants.py`, the test set-up and the Doxyfile are created there |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 1: window and three-segment snake as in the lectures | [BC-001], criterion 1 in Success Criteria |
| Objective 2: the assignment's structure and names | [BC-001], criterion 6 in Success Criteria |
| Objective 4: tests without a display | [BC-001], criterion 2 in Success Criteria |
| Design of the `Snake` class: no Design Class Diagram exists in this project and none is wanted for a learning project of this size. The class traces to the lecture "Create a Snake Class & Move to OOP" and to tasks 1 and 2 below. This is a recorded deviation from `QC-PY-001` criterion 10 | [RC-007] action item, S01 asked to start this milestone without asking for a diagram |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-11 — second of three gateways, inside the one-week plan of [PP-001] that ends 2026-10-15.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add the Snake class with create_snake | Create `src/snake_game/snake.py` with the class `Snake` (PascalCase) whose `__init__` sets an empty `segments` list and calls `create_snake`. `create_snake` makes one square turtle per entry of `STARTING_POSITIONS`, lifts the pen (`penup`) and sends it to its position. The segment factory is a constructor parameter whose default imports `turtle` lazily, so tests can pass a fake. Serves objectives 1 and 2 of the Business Case. | No | |
| 2 | Add the screen set-up and the main flow | Create `src/snake_game/main.py` with `configure_screen(screen)` (size 600 by 600, background black, title "My Snake Game") and `main()` that creates the screen, the snake, and ends with `screen.exitonclick()`. Add `src/snake_game/__main__.py` so `python -m snake_game` starts the game. | No | |
| 3 | Test the snake body without a display | Add `tests/test_snake.py` with a fake segment that records `shape`, `color`, `penup` and `goto`. Test: three segments are created, in the order of `STARTING_POSITIONS`, with the pen lifted before the first `goto`, in the shape and colour of the constants; and that importing `snake` does not import `turtle`. | No | |
| 4 | Test the screen set-up without a display | Add `tests/test_main.py` with a fake screen that records `setup`, `bgcolor` and `title`. Test that `configure_screen` sets the width, height, colour and title from the constants and nothing else. | No | |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-001]: ./mil-001-project-foundation.md
[RC-007]: ../sqa/reviews/rc-007-mil-001-code.md
[a2c997e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/020-snake-game/commit/a2c997e1413e425050df8c50a976ec839ebb4752
