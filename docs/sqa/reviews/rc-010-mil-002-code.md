# RC-010: Review of the MIL-002 code

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-010 |
| CrossReference | [MIL-002], [QC-PY-001], [RC-009] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-08 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [d60ceba] |

---

## Artifact Under Review

- Instance reviewed: the Python code of [MIL-002]: `src/snake_game/snake.py`, `src/snake_game/main.py`, `src/snake_game/__main__.py`, `tests/fakes.py`, `tests/test_snake.py` and `tests/test_main.py`
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a (source code is a technical type)
- Language reviewer: none

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Package `snake_game`; modules `snake`, `main`, `__main__`; class `Snake`, protocols `Segment` and `ScreenLike` (PascalCase); functions `configure_screen`, `make_turtle_segment`, `create_snake`; no constants outside `constants.py`. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names are the lectures' own (`Snake`, `segments`, `create_snake`, `screen`) and state purpose. `x` and `y` are coordinates in a two-line scope; `new_segment` is the lecture's name. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check src tests` reports "All checks passed!" and `ruff format --check src tests` reports all 9 files formatted; the imports and two long lines in the tests were fixed by ruff itself; no suppression exists. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Every function, method and Protocol member is annotated, `-> None` included; the tests are annotated too. `mypy` strict reports no issues in 9 source files. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | N-A | No exception handling in this change. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | The only default argument is `segment_factory: ... | None = None`; no builtin is shadowed (`shape`, `color`, `title` are method names of the turtle API). |
| 7 | Files, locks and connections are managed with context managers | N-A | No file, lock or connection is opened; `subprocess.run` in the tests is called with `capture_output` and waits for the process. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Module, class, method and function docstrings in Doxygen style say what each does; `doxygen Doxyfile` exits 0 with no warnings. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No `print` and no logging; no secret in any file. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | No Design Class Diagram exists. The deviation is recorded in the Traceability section of [MIL-002] and in [RC-009]; the classes trace to the lecture "Create a Snake Class & Move to OOP" and to tasks 1 and 2. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 25 tests (12 new), each named for one behaviour, independent of order, no network and no window; the two import tests start a fresh interpreter on the local `src` folder. `pytest` exits 0. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy` strict reports no issues; `object` is used for return values that the snake ignores and `Any` is not used. A real `turtle.Turtle` and `turtle.Screen` are accepted where `Segment` and `ScreenLike` are expected. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Fail | Unchanged since [RC-007]: `dependencies = []` and the dev tools have lower bounds, not exact pins. Optional criterion; no new dependency was added. |

## Other Go/No-Go checks of MIL-002 run for this review

| # | Criterion of [MIL-002] | Result |
| --- | --- | --- |
| 1 | The window matches the lecture | Read back from a real `turtle` screen: 600 by 600, background `black`, title "My Snake Game". `exitonclick` is called after the snake is drawn (checked with the fake screen). **A real click and the look of the window were not checked by the assistant: S01 runs `python -m snake_game`** |
| 2 | The snake body is drawn | Read back from real turtles: 3 segments at (0, 0), (-20, 0), (-40, 0), shape `square`, colour `white`, pen up. **S01 confirms by eye that they touch and leave no trail** |
| 3 | `Snake` follows the lecture | `Snake`, `segments` (a list) and `create_snake` exist in `snake.py`; one segment per entry of `STARTING_POSITIONS`; `penup` is called before `goto`; no literal position, shape or colour in `snake.py` or `main.py` |
| 4 | The window code is testable | `configure_screen` takes the screen and `Snake` takes its segment factory as parameters; `turtle` is imported only in `make_turtle_segment` and `main`; two tests start a fresh interpreter and show that importing `snake_game.snake` and `snake_game.main` does not import `turtle` |
| 5 | Tests prove the body | 25 passed; the new tests cover number, shape, colour, order and positions of the segments, the pen, the default factory and the screen settings, using fakes only |
| 6 | `doxygen Doxyfile` builds | Exit 0, no warnings (after the Doxyfile was aligned with `018-turtle`, see Action Items) |

## Overall Verdict

Go — all Mandatory criteria pass or are not applicable, and the one Fail (criterion 13) is Optional and unchanged. The rows above were assessed on 2026-10-08 by the assistant that wrote the code, at S01's request in chat. This review is **not independent**; S01 is the approver and can overrule the verdict at the pull request. The two visual checks (criteria 1 and 2 of [MIL-002]) rest on S01's own run.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Run `python -m snake_game` and confirm the window, the three touching white squares and the close on a click (Go/No-Go criteria 1 and 2 of [MIL-002]) | S01 | 2026-10-11 |
| Note that the Doxyfile changed in this branch: `WARN_NO_PARAMDOC = NO` and `WARN_IF_INCOMPLETE_DOC = YES`, as in `018-turtle`, because with `YES` Doxygen asks for an `@return` on every `-> None` function. A half-documented function still fails the build | S01 | 2026-10-11 |
| Decide whether to pin the development tools exactly (criterion 13, carried over from [RC-007]) | S01 | 2026-10-13 |

---

[MIL-002]: ../../milestones/mil-002-screen-and-snake-body.md
[QC-PY-001]: ../../../framework/qc/qc-programming-python.md
[RC-007]: ./rc-007-mil-001-code.md
[RC-009]: ./rc-009-mil-002-rereview.md
[d60ceba]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/020-snake-game/commit/d60cebaeff4cbb5d54c080429b4a77661befce8f
