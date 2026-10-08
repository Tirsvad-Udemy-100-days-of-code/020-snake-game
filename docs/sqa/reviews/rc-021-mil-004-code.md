# RC-021: Review of the MIL-004 code

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-021 |
| CrossReference | [MIL-004], [QC-PY-001], [RC-018] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-08 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: the Python code of [MIL-004]: `src/snake_game/food.py`, `src/snake_game/scoreboard.py`, `src/snake_game/snake.py`, `src/snake_game/main.py`, `src/snake_game/constants.py`, `tests/fakes.py`, `tests/test_food.py`, `tests/test_scoreboard.py`, `tests/test_snake.py`, `tests/test_main.py` and `tests/test_constants.py`
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a (source code is a technical type)
- Language reviewer: none

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Classes `Food`, `Scoreboard`, `FoodLike`, `ScoreboardLike` are `PascalCase`; functions and methods `add_segment`, `extend`, `refresh`, `random_coordinate`, `update_scoreboard`, `increase_score`, `eat_food_if_close` are `snake_case`; the eleven new constants are `UPPER_SNAKE`. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names are the lectures' own (`Food`, `Scoreboard`, `refresh`, `extend`, `increase_score`) or state their purpose (`eat_food_if_close`, `random_coordinate`); no abbreviations. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check src tests` reports "All checks passed!" and `ruff format --check src tests` reports all 13 files formatted; ruff's own fixes were applied; no suppression exists. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Every function, method and Protocol member is annotated, `-> None` included; `mypy` strict reports no issues in 13 source files. A real `Turtle` is accepted as a `Segment` (`position` and `distance` were added), and a real `Food` and `Scoreboard` as `FoodLike` and `ScoreboardLike`. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | N-A | No new exception handling; the catch of `TclError` and `Terminator` in `main` is unchanged from [MIL-003]. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable default argument (the one default in the tests is a tuple); no builtin is shadowed. |
| 7 | Files, locks and connections are managed with context managers | N-A | No file, lock or connection is opened by the new code. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Module, class, method and function docstrings in Doxygen style; the modules `food` and `scoreboard` explain why they need `turtle` at import time; `doxygen Doxyfile` exits 0 with no warnings. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No `print` and no logging; neither token value of `.env` appears in any file. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | No Design Class Diagram exists. The deviation is recorded in the Traceability section of [MIL-004] (as in [MIL-002]); `Food`, `Scoreboard` and `Snake.extend` trace to the day-21 outline and to tasks 2 to 5 of [MIL-004]. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 91 tests (30 new, 61 before), each named for one behaviour, independent of order and of the network; no test opens a window. The tests that import `food` and `scoreboard` install a fake `turtle` module first and remove the imported modules afterwards: the suite passes with the files in reverse order, with each file alone, and with `test_main.py` run twice in one session. The random places come from `random.randint`, which the tests replace. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy` strict reports no issues. `Any` is used only as the return type of `make_food` and `make_scoreboard` in the tests, with the reason in their docstrings: the result is a real `Food` or `Scoreboard` on a fake base class and has the attributes of both. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Fail | Unchanged since [RC-007]: `dependencies = []` and the dev tools have lower bounds, not exact pins. Optional criterion; no dependency was added. |

## The assumed values, as confirmed

S01 confirmed the assumed values of the table in the Deliverable section of [MIL-004] in chat on 2026-10-08 ("Yes, confirm the values and start MIL-004"), without changing any. The assistant did not compare them with the lecture video. The pull request must list them (Go/No-Go criterion 1):

| Value | Final | Constant |
| --- | --- | --- |
| Shape, size, colour and speed of the food | circle, 0.5 by 0.5, blue, fastest | `FOOD_SHAPE`, `FOOD_SIZE`, `FOOD_COLOR`, `FOOD_SPEED` |
| Wall, also the range of the random place of the food | 280 on every side | `WALL_LIMIT` |
| Distance at which the food is eaten | less than 15 pixels | `FOOD_COLLISION_DISTANCE` |
| Growth and points | one segment and 1 point per food | none |
| Text, colour, place and alignment of the scoreboard | `Score: ` and the score, white, (0, 270), centred | `SCORE_LABEL`, `SCOREBOARD_COLOR`, `SCOREBOARD_POSITION`, `SCOREBOARD_ALIGNMENT` |
| Font of the scoreboard | Arial, 24, normal | `SCOREBOARD_FONT` |

The decisions of the open issues of [PP-001] that the plan proposed were taken as agreed by the same message and are built as proposed: `Food` and `Scoreboard` inherit from `Turtle` and the tests install a fake `turtle` module; the food is placed at random without looking at the snake.

## Other Go/No-Go checks of MIL-004 run for this review

The real game was run with a real `turtle` window, the real `Food` and the real `Scoreboard`. The food was moved into the path of the head, the window state was read back from the real turtles and the canvas, and the window's close handler was called to close it.

| # | Criterion of [MIL-004] | Result |
| --- | --- | --- |
| 1 | The assumed values are confirmed | Confirmed by S01 in chat, see above. **The comparison with the video is S01's** |
| 2 | Food is shown | Pass, read back: shape `circle`, colour `blue`, size (0.5, 0.5), pen up, at (176, -98) (inside the walls); a new place (46, -103) after it was eaten. **That it looks like a small blue dot is S01's check by eye** |
| 3 | The snake eats | Pass: the food was placed two moves ahead of the head; afterwards there were 6 turtles instead of 5 (one segment more), the canvas showed `Score: 1`, and the food was at a new place |
| 4 | Growth keeps the body joined | Pass in the tests (all gaps equal the move distance after a turn, an extend and a move). **No gap by eye is S01's check** |
| 5 | The scoreboard shows the score | Pass: the canvas held one text item, `Score: 0` at the start and `Score: 1` after eating, so the old text was gone. White, centred at (0, 270) and the font are checked by the tests. **The look is S01's check** |
| 6 | The classes inherit | Pass: the real `Food` and `Scoreboard` are instances of the real `turtle.Turtle`; the tests show `issubclass` and that the base class is initialised first |
| 7 | Constants are in one place | Pass: a search for numbers, colour names and shape names found no value of the table outside `constants.py` |
| 8 | Day-20 behaviour is unchanged | Pass: the 61 tests of phase 1 still pass. Two tests of `test_main.py` were adapted because `main` now also creates the food and the scoreboard (the number of turtles, and an autouse fixture that keeps the food far from the snake) |
| 9 | Tests prove the behaviour | Pass: 91 passed; importing `snake_game.main` loads neither `turtle` nor `tkinter` |
| 10 | `doxygen Doxyfile` builds | Pass: exit 0, no warnings |
| 11 | The code is reviewed | This record |

## Overall Verdict

Go — all Mandatory criteria pass or are not applicable, and the one Fail (criterion 13) is Optional and unchanged. The rows above were assessed on 2026-10-08 by the assistant that wrote the code, at S01's request in chat. This review is **not independent**; S01 is the approver and can overrule the verdict at the pull request. The look of the food and the scoreboard, the joined body and the comparison with the video rest on S01.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Run `python -m snake_game` and check by eye the food, the growth, the scoreboard and that the body stays joined; compare with the lecture video and list the final values in the pull request (Go/No-Go criteria 1 to 5 of [MIL-004]) | S01 | 2026-10-17 |
| Decide whether to pin the development tools exactly (criterion 13, carried over from [RC-007]) | S01 | 2026-10-17 |

---

[MIL-004]: ../../milestones/mil-004-food-and-score.md
[QC-PY-001]: ../../../framework/qc/qc-programming-python.md
[PP-001]: ../../project-plan.md
[RC-007]: ./rc-007-mil-001-code.md
[RC-018]: ./rc-018-mil-004.md
