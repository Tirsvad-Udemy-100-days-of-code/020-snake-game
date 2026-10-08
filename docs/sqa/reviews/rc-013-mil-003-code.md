# RC-013: Review of the MIL-003 code

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-013 |
| CrossReference | [MIL-003], [QC-PY-001], [RC-011] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-08 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [0096f2f] |

---

## Artifact Under Review

- Instance reviewed: the Python code of [MIL-003]: `src/snake_game/snake.py`, `src/snake_game/main.py`, `tests/fakes.py`, `tests/test_snake.py` and `tests/test_main.py`
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a (source code is a technical type)
- Language reviewer: none

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Methods `move`, `up`, `down`, `left`, `right` and functions `bind_keys`, `play_frame` are `snake_case`; `Snake`, `Segment`, `ScreenLike` are `PascalCase`; no new constant outside `constants.py`. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names are the lectures' own (`move`, `head`, `up`, `down`, `left`, `right`, `game_is_on`, `segments`) and state purpose. `_direction_of_travel` says what it holds; `ahead` is the segment in front of the one being moved. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check src tests` reports "All checks passed!" and `ruff format --check src tests` reports all 9 files formatted; ruff's own fixes were applied; the one rule hit by a test helper (N818, exception names end in `Error`) was fixed by renaming, not suppressed. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Every function, method and Protocol member is annotated, `-> None` included; `mypy` strict reports no issues in 9 source files. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | `main` catches exactly `tkinter.TclError` and `turtle.Terminator`, around the animation loop only, and returns because the player closed the window; the reason is in the docstring. Anything else passes through, which `test_main_lets_other_errors_through` checks. The catch is deliberate and narrow, not a swallowed error. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No default arguments were added; no builtin is shadowed (`index`, `ahead`, `seconds`). |
| 7 | Files, locks and connections are managed with context managers | N-A | No file, lock or connection is opened by the new code. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Module, class, method and function docstrings in Doxygen style say what each does; `Snake` explains why a turn is compared with the last move; `doxygen Doxyfile` exits 0 with no warnings. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No `print` and no logging; no secret in any file. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | No Design Class Diagram exists. The deviation is recorded in the Traceability section of [MIL-002] and in [RC-009]; `move`, `head` and the direction methods trace to the lectures "Animating the Snake Segments on Screen" and "Controlling the Snake with Keypresses" and to tasks 1 to 5 of [MIL-003]. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 61 tests (36 new), each named for one behaviour, independent of order, no network and no window; `time.sleep` is replaced so that no test waits; the direction table covers every direction from every starting direction (16 cases). `pytest` exits 0. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy` strict reports no issues; `Any` is not used. A real `turtle.Turtle` and `turtle.Screen` are accepted where `Segment` and `ScreenLike` are expected. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Fail | Unchanged since [RC-007]: `dependencies = []` and the dev tools have lower bounds, not exact pins. Optional criterion; no dependency was added. |

## Other Go/No-Go checks of MIL-003 run for this review

The real game was run with a real `turtle` window. Arrow keys were injected as Tk key events into the window, positions were read back from the real turtles, and the window's close handler (`WM_DELETE_WINDOW`, `screen._destroy`) was called to close it.

| # | Criterion of [MIL-003] | Result |
| --- | --- | --- |
| 1 | The snake moves by itself | Pass for the movement: after about 0.4 s the head was at (80, 0), the body at (60, 0) and (40, 0), that is 20 pixels per move to the right, and no segment drew a line (pen up). **That it looks smooth and does not flicker is S01's check by eye** |
| 2 | Segments follow the head | Pass: after Up the segments were at (100, 80), (100, 60), (100, 40), a joined line; after Left they were at (0, 200), (20, 200), (40, 200), joined, with no gap |
| 3 | The arrow keys steer | Pass for Up, Down and Left in the real window (headings 90, 270 refused, 180); Right is checked by the tests and by the same code path |
| 4 | The snake never reverses | Pass: Down while moving up left the heading at 90 in the real window; the table of tests covers every direction from every starting direction, and two key presses within one move |
| 5 | The window closes cleanly | Pass: `main()` returned normally 0.14 s after the close handler ran, exit code 0, no traceback. The exception a real close raises is `_tkinter.TclError`; `turtle.Terminator` is handled too (tests for both) |
| 6 | Tests prove the behaviour | 61 passed |
| 7 | `doxygen Doxyfile` builds | Exit 0, no warnings |
| 8 | The README is finished | Run section gives `python -m snake_game`, the arrow keys and the day-21 note; Status says the day-20 game is finished. **A fresh clone was not made for this milestone**; the set-up commands are those verified in [RC-007] and did not change |
| 9 | The game matches the lecture | **Open: S01 compares the running game with the lecture video.** Known difference from the lecture's code: a turn is refused against the direction of the last move, not the current direction of the head (explained in `Snake` and in task 4 of [MIL-003]) |
| 10 | The code is reviewed | This record |

## Overall Verdict

Go — all Mandatory criteria pass or are not applicable, and the one Fail (criterion 13) is Optional and unchanged. The rows above were assessed on 2026-10-08 by the assistant that wrote the code, at S01's request in chat. This review is **not independent**; S01 is the approver and can overrule the verdict at the pull request. Criteria 1 (look), 8 (fresh clone) and 9 (video) of [MIL-003] rest on S01.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Run `python -m snake_game`, watch the snake move and turn, and confirm that it looks smooth, then compare it with the lecture video (Go/No-Go criteria 1 and 9 of [MIL-003]) | S01 | 2026-10-13 |
| Follow the README in a fresh clone on Windows PowerShell up to a green `pytest` (Go/No-Go criterion 8 of [MIL-003]) | S01 | 2026-10-13 |
| Decide whether to pin the development tools exactly (criterion 13, carried over from [RC-007]) | S01 | 2026-10-13 |

---

[MIL-003]: ../../milestones/mil-003-movement-and-keys.md
[MIL-002]: ../../milestones/mil-002-screen-and-snake-body.md
[QC-PY-001]: ../../../framework/qc/qc-programming-python.md
[RC-007]: ./rc-007-mil-001-code.md
[RC-009]: ./rc-009-mil-002-rereview.md
[RC-011]: ./rc-011-mil-003-rereview.md
[0096f2f]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/020-snake-game/commit/0096f2f31350100013cd93f3ed13cca9c5f5d4a2
