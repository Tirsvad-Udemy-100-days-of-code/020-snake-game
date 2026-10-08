# Business Case: Snake Game

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-08 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [a2c997e] |
| 2026-10-08 | Accepted | Jens Tirsvad Nielsen | S01 | Risk table names the exceptions that closing the window really raises (`_tkinter.TclError` or `turtle.Terminator`) | [c033c7b] |

---

## Executive Summary

Snake Game is the day-20 assignment of Udemy's *100 Days of Code: The Complete
Python Pro Bootcamp*: the first half of the classic Snake game, built in an
object-oriented way with Python's `turtle` module. Four lectures lead from an
empty window to a three-segment snake that moves by itself and is steered with
the arrow keys. The course leaves the result as loose code in the lecture
videos. This project turns it into a small, finished repository: a `Snake`
class that follows the lectures, tests that run without a display, source
documentation, and a README that lets another course participant create a
virtual environment and run everything. It has no runtime dependencies and is
planned in three milestones, each delivered by one branch and one pull request.
The second half of the game (food, score and game over, day 21) is not part of
this project.

## Methodological and Standards Foundation

- **Process:** the Software Quality Assurance (SQA) and Quality Criteria (QC)
  framework mounted at `framework/`: Business Case, Stakeholder Analysis,
  Project Plan, milestones, tasks synced as issues, then code, each step
  reviewed before the next. Analysis follows Larman, *Applying UML and
  Patterns*.
- **Quality model:** ISO/IEC 25010:2023; every QC criterion is tagged with a
  characteristic of it.
- **Code:** Python Enhancement Proposals (PEP) 8, 257 and 484, reviewed against `QC-PY-001`; comments
  in Doxygen style; tests with pytest.
- **Domain terms:** the lectures' own terms and names are used and recorded in
  the Domain Dictionary [DICT-001] (screen, snake, segment, head, body, move,
  direction, reversal, and the names `create_snake`, `up`, `down`, `left`,
  `right`, `game_is_on`).

## Problem Statement

- The course shows the code only inside lecture videos, and the lectures change
  the same code four times (loose script, list of segments, `Snake` class,
  key bindings). Nobody can run or compare the finished day-20 state without
  retyping it.
- A loose script cannot be run by someone else without guessing the Python
  version, the environment and the way to start it.
- A turtle program opens a window, so it is normally not tested, and mistakes
  in the rules of the move (a segment that does not follow, a snake that
  reverses onto itself) are found only by watching.
- A repository without description, topics or README is hard to find and hard
  to judge for the people who browse for ideas.

## Business Opportunity

A single finished, reproducible repository shows the whole path from lecture
to documented, tested code. It can be compared with the solutions of other
participants, shared, and reused as the starting point for day 21, which adds
food, score and game over to the same `Snake` class.

## Objectives

| # | Objective |
| --- | --- |
| 1 | Deliver a runnable game state that follows the four lectures: a 600 by 600 black window titled "My Snake Game"; a snake of three square segments at (0, 0), (-20, 0) and (-40, 0); a move of 20 pixels every 0.1 seconds with manual screen updates; arrow keys that turn the head; and no reversal onto the snake |
| 2 | Keep the assignment's structure and names: a `Snake` class in its own module with `create_snake`, `move`, `up`, `down`, `left`, `right`, a `segments` list and a `head`, directions and the move distance as constants, and a main flow that uses `screen`, `snake` and `game_is_on` |
| 3 | Provide a reproducible environment: Python 3.13 or newer, a local `.venv`, a `pyproject.toml`, and zero runtime dependencies |
| 4 | Prove the behaviour with pytest tests that need no display |
| 5 | Document the project: Doxygen comments in the source with a `Doxyfile`, and a README with set-up instructions for Windows PowerShell, Linux Debian and macOS |
| 6 | Keep every step traceable: one branch and one pull request per milestone, each pull request closing the issues it completes |
| 7 | Publish the repository with a description and topics |

## Scope

### In Scope

- The four lectures of day 20: screen set-up and snake body, animating the
  segments, the `Snake` class, controlling the snake with the arrow keys.
- Constants in `constants.py`; source in `src/`, tests in `tests/`, documents in
  `docs/`.
- `pyproject.toml`, Python `.gitignore`, `Doxyfile`, `README.md` following the
  Product Owner's template, a continuous integration (CI) workflow.
- Repository description and topics on the git host.

### Out of Scope

- Day 21 of the course: food, detecting a collision with food, the scoreboard,
  growing the snake, and the game-over rules (wall and tail collision). The
  `Snake` class is built so that day 21 can extend it, but none of that is
  delivered here.
- Anything the lectures do not cover: sound, a menu, high-score storage,
  levels, configurable speed or window size.
- Packaging for or publishing to the Python Package Index (PyPI).
- A mirror of the repository on GitHub (the repository lives on the Tirsvad git
  host; see Open Issues of [PP-001]).
- Runtime dependencies of any kind.
- Using or testing the tokens in `.env`; the file is for personal use only and
  is never imported by the project.

## Expected Benefits

### Tangible Benefits

- A finished day-20 game state that runs with one command after the README
  steps.
- A test suite that can run in continuous integration without a display.
- Generated source documentation.
- A repository page with description, topics and README.

### Intangible Benefits

- Practice with the `turtle` coordinate system, lists of objects, constants and
  classes, which is the aim of the lectures.
- A base for day 21 and a pattern for the following days of the course.
- Confidence from a step-by-step, reviewed delivery.

## Strategic Alignment

The project supports the participant's goal of finishing the bootcamp with
repositories that other people can read, run and learn from, and it exercises
the framework's rule that planning, review and code stay in step.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | The game state follows the lectures | Window 600 by 600, black, titled "My Snake Game"; 3 segments at (0, 0), (-20, 0), (-40, 0); every move takes each segment 20 pixels and each segment takes the place of the one before it; the head turns to 90, 270, 180 and 0 degrees for up, down, left and right; a reversal is ignored | Manual run by S01 against the Go/No-Go list of [MIL-003], plus the matching tests |
| 2 | Tests are green and need no display | 100% of tests pass; 0 tests open a window; at least one test per public function and method of the logic modules | `pytest` exit code 0 locally and in CI |
| 3 | The set-up steps work | A fresh clone reaches a green `pytest` by following the README alone, on Windows PowerShell (by S01) and on Linux (by CI) | One run per operating system, recorded in the pull request |
| 4 | Source documentation builds | `doxygen Doxyfile` ends with 0 warnings | Doxygen output |
| 5 | No runtime dependencies | 0 entries in `[project].dependencies` | `pyproject.toml` |
| 6 | Names follow the assignment | 100% of the names listed in objective 2 exist with that spelling | Review of `src/` against objective 2 |
| 7 | Steps are traceable | 3 of 3 milestones merged by pull request, each description with one `Closes #N` line per completed issue | Pull request list and issue states |
| 8 | The repository page is complete | Non-empty description and at least 5 topics | Git host |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| `tkinter` is missing from the Python installation (typical on Debian) | The game cannot start | README lists `python3-tk` for Debian; the `snake` module does not import `turtle` at module level, so tests do not need it |
| Debian 12 ships Python 3.11, below the required 3.13 | Linux set-up fails | README states Debian 13 or newer, or a separately installed Python 3.13 |
| A turtle window cannot be opened in continuous integration | The tests cannot cover the game | `Snake` receives its segment factory as a parameter, so tests pass fakes; only `main` opens a window |
| The git host has no Actions runner | The continuous integration workflow is never executed | Provide the workflow file and run the same commands locally; recorded as an open issue of [PP-001] |
| Closing the window during the animation loop ends in a traceback (`_tkinter.TclError` or `turtle.Terminator`) | The game looks broken when it is quit | [MIL-003] requires a clean exit when the window is closed |
| Author and reviewer are the same person (S01) | A defect can pass review unnoticed | Review against the QC checklists, record each review as an `RC-*`, and let the pull request be the second look |
| The lectures are available only as the summaries in the request | The game differs from the video | S01 compares the finished game with the video at the [MIL-003] Go/No-Go |
| Tokens in `.env` leak into the repository | Credentials exposed | `.env` is in `.gitignore`, is never imported, and is not part of any task |

## Assumptions

- Python 3.13 or newer with `tkinter` is available on the machines that run
  the game.
- S01 is the only person who reviews and accepts artifacts.
- The git host is the Tirsvad Gitea instance, and its issues and milestones
  are used for tracking.
- The four lecture summaries in the request are the only specification of the
  game; the video is the tie-breaker when a detail is missing.

## Constraints

- Python 3.13 or newer, in a virtual environment (`venv`).
- pytest for tests; `constants.py` for constants; `pyproject.toml` for
  project configuration; a Python `.gitignore`; Doxygen comments in the source
  and a `Doxyfile`.
- Folder structure `src/`, `tests/`, `docs/`.
- No runtime dependencies unless needed.
- Effort budget of about one week; the plan ends on 2026-10-15 (proposed, see
  [PP-001]).
- Nothing is committed, pushed or merged without the Product Owner's request;
  changes are reviewed in the working tree first.
- The plan gate holds: no file under `src/` or `tests/` before an accepted,
  reviewed milestone that lists the task.

## Cost–Benefit Assessment

The assessment is qualitative on purpose: this is an unpaid learning project
with one participant, so money does not measure either side.

| Costs | Benefits |
| --- | --- |
| About one week of S01's spare time, including reviews | A finished and shareable repository (objectives 1 to 7) |
| Review effort for the planning documents, which is large compared with the size of the game | A traceable, repeatable way of working that day 21 and later days can reuse |
| Doxygen and pytest as development tools (not runtime) | Source documentation and automatic checks |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Wants a correct, tested and documented solution of the assignment: objectives 1 to 7 |
| S02 | Needs readable, runnable code with the assignment's names and README instructions (objectives 1, 2, 3 and 5) |
| S03 | Needs a clear repository page and nothing to install (objectives 3, 5 and 7) |

## Recommendation

Proceed — the scope is small and fully specified by the four lectures, the cost
is a week of the Product Owner's time, and the result is a reusable,
documented repository and a base for day 21.

---

[SA-001]: ./stakeholder-analysis.md
[DICT-001]: ./dictionary.md
[PP-001]: ./project-plan.md
[MIL-003]: ./milestones/mil-003-movement-and-keys.md
[a2c997e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/020-snake-game/commit/a2c997e1413e425050df8c50a976ec839ebb4752
[c033c7b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/020-snake-game/commit/c033c7b660f8b9dcabf13d7556ef6c4e21b7d3a4
