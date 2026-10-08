# RC-022: Review of the MIL-005 code

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-022 |
| CrossReference | [MIL-005], [QC-PY-001], [RC-020] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-08 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: the Python code of [MIL-005]: `src/snake_game/snake.py`, `src/snake_game/scoreboard.py`, `src/snake_game/main.py`, `src/snake_game/constants.py`, `tests/fakes.py`, `tests/test_snake.py`, `tests/test_scoreboard.py`, `tests/test_main.py` and `tests/test_constants.py`
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a (source code is a technical type)
- Language reviewer: none

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Methods `hits_wall`, `hits_tail`, `game_over` and function `end_game_if_over` are `snake_case`; the three new constants are `UPPER_SNAKE`. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose and follow the dictionary verbs: the head passes the wall (`hits_wall`), touches the tail (`hits_tail`), the game is over (`game_over`, `end_game_if_over`). |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check src tests` reports "All checks passed!" and `ruff format --check src tests` reports all 13 files formatted; ruff's own fixes were applied; no suppression exists. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Every function, method and Protocol member is annotated, `-> None` and `-> bool` included; `mypy` strict reports no issues in 13 source files. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | N-A | No new exception handling; the catch of `TclError` and `Terminator` in `main` is unchanged, and now also covers the final `screen.update()` and `exitonclick()`. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No default arguments were added; no builtin is shadowed. |
| 7 | Files, locks and connections are managed with context managers | N-A | No file, lock or connection is opened by the new code. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Docstrings in Doxygen style say what each method does, including that `game_over` leaves the score and that the screen must be updated after it; `doxygen Doxyfile` exits 0 with no warnings. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No `print` and no logging; neither token value of `.env` appears in any file. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | No Design Class Diagram exists. The deviation is recorded in the Traceability section of [MIL-005] (as in [MIL-002]); `hits_wall`, `hits_tail` and `game_over` trace to the day-21 outline and to tasks 2 to 4 of [MIL-005]. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 128 tests (37 new, 91 before), each named for one behaviour, independent of order and of the network; no test opens a window. The boundaries are tested on both sides: the wall at 280 and at 281 on all four sides, the tail at 9, 10 and 11 pixels, a snake of five segments that turns into its tail and a snake of four that cannot. The suite passes with the files in reverse order and with each file alone. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy` strict reports no issues; `Any` is not used in the code, and in the tests only in the two helpers described in [RC-021]. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Fail | Unchanged since [RC-007]: `dependencies = []` and the dev tools have lower bounds, not exact pins. Optional criterion; no dependency was added. |

## The assumed values, as confirmed

The assistant ended its last message before this milestone with "tell me if any should change before I begin" (wall at 280, tail touched closer than 10 pixels, `GAME OVER` centred). S01 answered "Yes, start MIL-005" in chat on 2026-10-08. That is taken as confirmation without changes; **S01 should say so explicitly, or list a change, in the pull request**. The assistant did not compare the values with the lecture video. The final values:

| Value | Final | Constant |
| --- | --- | --- |
| Wall | the head is outside when its x or y is beyond 280 | `WALL_LIMIT` (from [MIL-004]) |
| Distance at which the head touches the tail | less than 10 pixels from any segment behind the head | `TAIL_COLLISION_DISTANCE` |
| Text at game over | `GAME OVER` | `GAME_OVER_TEXT` |
| Place, alignment and font of that text | (0, 0), centred, the font of the scoreboard | `GAME_OVER_POSITION`, `SCOREBOARD_ALIGNMENT`, `SCOREBOARD_FONT` |

## Other Go/No-Go checks of MIL-005 run for this review

The real game was run with a real `turtle` window. The head and a body segment were moved by script to stage each case, the window state was read back from the real turtles and the canvas, and a click was sent to the canvas (or the close handler of the window was called). All scenarios were run with a 20-second limit.

| # | Criterion of [MIL-005] | Result |
| --- | --- | --- |
| 1 | The assumed values are confirmed | Taken as confirmed, see above. **The video comparison, and an explicit statement, are S01's** |
| 2 | The wall ends the game | Pass: in the real window the head passed the wall to the right and stopped at (300, 0). The other three sides and the inside of the wall are covered by the tests. **Playing into each wall by hand is S01's check** |
| 3 | The tail ends the game | Pass: in the real window a body segment was put on the next place of the head and the game ended with the head at (80, 0); the tests cover turning into a tail of five segments, the touch distance on both sides, and that growing does not cause a touch. **Turning into the tail with the arrow keys is S01's check** |
| 4 | GAME OVER is shown | Pass: the canvas held exactly `GAME OVER` and `Score: 0`, and the head stayed at the same place at two probes 0.4 seconds apart. The centre is checked by the tests. **The look is S01's check** |
| 5 | A click closes the window | Pass: a click sent to the canvas ended `main()` within 0.02 seconds, exit code 0, no traceback |
| 6 | Closing the window still ends quietly | Pass: closing the window while it waits for the click ended `main()` normally, exit code 0; the tests cover both exceptions during play and after game over. Closing during play was checked in [RC-013] |
| 7 | Constants are in one place | Pass: a search for 280, 10, `GAME OVER`, `center` and `Arial` found none outside `constants.py` |
| 8 | Earlier behaviour is unchanged | Pass: the 91 tests of [MIL-001] to [MIL-004] still pass |
| 9 | Tests prove the behaviour | Pass: 128 passed; importing `snake_game.main` loads neither `turtle` nor `tkinter` |
| 10 | `doxygen Doxyfile` builds | Pass: exit 0, no warnings |
| 11 | The README is finished | Pass for the content: it describes moving, food, score, game over and closing, and no sentence says that anything is missing. **A fresh clone was not made for this milestone**; the set-up commands did not change since [RC-007] |
| 12 | The game matches the lecture | **Open: S01 compares the finished game with the lecture video** |
| 13 | The code is reviewed | This record |

A note on the real runs: a first attempt hung because the test script sent its click to the Frame that `getcanvas()` returns and not to the inner canvas that `exitonclick` binds; that was a fault of the script, not of the game. A few early returns in those first attempts were not explained and did not occur in the corrected runs.

## Overall Verdict

Go — all Mandatory criteria pass or are not applicable, and the one Fail (criterion 13) is Optional and unchanged. The rows above were assessed on 2026-10-08 by the assistant that wrote the code, at S01's request in chat. This review is **not independent**; S01 is the approver and can overrule the verdict at the pull request. The explicit confirmation of the values, the look of the end of the game, playing into the wall and the tail by hand, a fresh-clone run and the comparison with the video rest on S01.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Run `python -m snake_game`, play into the wall and into your own tail, check that GAME OVER appears and that a click closes the window; compare with the lecture video and state in the pull request which values stay (Go/No-Go criteria 1 to 5 and 12 of [MIL-005]) | S01 | 2026-10-19 |
| Follow the README in a fresh clone on Windows PowerShell up to a green `pytest` (Go/No-Go criterion 11 of [MIL-005]) | S01 | 2026-10-19 |
| Decide whether to pin the development tools exactly (criterion 13, carried over from [RC-007]) | S01 | 2026-10-19 |

---

[MIL-005]: ../../milestones/mil-005-game-over.md
[MIL-001]: ../../milestones/mil-001-project-foundation.md
[MIL-002]: ../../milestones/mil-002-screen-and-snake-body.md
[MIL-004]: ../../milestones/mil-004-food-and-score.md
[QC-PY-001]: ../../../framework/qc/qc-programming-python.md
[RC-007]: ./rc-007-mil-001-code.md
[RC-013]: ./rc-013-mil-003-code.md
[RC-020]: ./rc-020-mil-005-title.md
[RC-021]: ./rc-021-mil-004-code.md
