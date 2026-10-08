# MIL-001: Project foundation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-08 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [a2c997e] |
| 2026-10-08 | Accepted | Jens Tirsvad Nielsen | S01 | Moved the CI workflow from `.github/workflows` to `.gitea/workflows` (task 6, deliverable, criterion 8) so that the push mirror to GitHub is not blocked | [a2c997e] |

---

## Purpose

This gate decides whether the repository is ready to hold the game: a fresh clone can be set up from the README, the tests and the documentation build run, and every constant of the game lives in one module. The work is delivered on the branch `mil-001-project-foundation` and one pull request.

## Deliverable

The repository files that carry no game logic yet: `pyproject.toml`, the Python `.gitignore`, the package `src/snake_game/` with `constants.py`, `tests/test_constants.py`, `README.md` following the Product Owner's template, `Doxyfile`, and the continuous integration workflow `.gitea/workflows/ci.yml`. The repository description and topics on the git host are already set (2026-10-08).

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | In a fresh clone, `python -m venv .venv`, `python -m pip install --upgrade pip` and `python -m pip install -e ".[dev]"` succeed in Windows PowerShell | All three commands exit 0 | Any command fails |
| 2 | `pytest` runs | Exit code 0, at least one test of `constants.py`, no window opened | Failing test, or no test of `constants.py` |
| 3 | `pyproject.toml` states the Python version and the dependencies | `requires-python = ">=3.13"`, `dependencies = []`, a `dev` extra with pytest | Any of the three is missing or different |
| 4 | The `.gitignore` protects local files | `git check-ignore .venv .env __pycache__` lists all three | One of them is not ignored |
| 5 | `constants.py` holds the lectures' values | Screen width, height, colour and title; segment shape and colour; the three starting positions; the move distance; the four directions; the refresh delay are constants with Doxygen comments, and no other module defines them | A value of the list is a literal in another module |
| 6 | `doxygen Doxyfile` builds the source documentation | Ends with 0 warnings and writes HTML for `src/` | Any warning, or no output |
| 7 | The README follows the Product Owner's template | Every heading of the template in the given order, with commands for Windows PowerShell, Linux Debian and macOS | A heading is missing, out of order, or a section has no commands |
| 8 | The continuous integration (CI) workflow exists | `.gitea/workflows/ci.yml` installs `.[dev]` and runs `pytest` on Python 3.13, and nothing under `.github/workflows` exists | No workflow, or it does not run the tests, or a file exists under `.github/workflows` |
| 9 | The repository page is complete | Description is non-empty and there are at least 5 topics on the git host | Description empty or fewer than 5 topics |
| 10 | The code is reviewed | `RC-*` against `QC-PY-001` has the verdict `Go` | Verdict `No-Go` or `Go-with-conditions` |
| 11 | No secret is in the change | `.env` is not tracked and no token appears in any changed file | A token is found in the diff |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [PP-001] accepted | The plan schedules this gateway; the plan-first gate needs it before any code |
| This milestone accepted with a `Go` review | The plan-first gate allows no file under `src/` or `tests/` before that |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 3: reproducible environment, no runtime dependencies | [BC-001], criteria 3, 5 in Success Criteria |
| Objective 4: tests without a display | [BC-001], criterion 2 in Success Criteria |
| Objective 5: Doxygen and README | [BC-001], criteria 3, 4 in Success Criteria |
| Objective 7: repository page | [BC-001], criterion 8 in Success Criteria |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-09 — first of three gateways, inside the one-week plan of [PP-001] that ends 2026-10-15.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add pyproject.toml | Create `pyproject.toml` for the `snake-game` project with `requires-python = ">=3.13"`, an empty `dependencies` list, an optional `dev` extra with pytest, ruff and mypy, the `src` layout for the package `snake_game`, and the pytest settings (`testpaths = ["tests"]`). Serves objective 3 of the Business Case: a reproducible environment without runtime dependencies. | No | |
| 2 | Add the Python .gitignore | Add a `.gitignore` for Python: bytecode, `.venv/`, build and packaging output, pytest, ruff, mypy and Doxygen output. Also ignore `.env`, so the personal tokens can never be committed or become part of the project. | No | |
| 3 | Create the package skeleton with constants.py | Create `src/snake_game/__init__.py` and `src/snake_game/constants.py` with the values of the four lectures as `UPPER_SNAKE` constants with Doxygen comments: screen 600 by 600, background `black`, title "My Snake Game", segment shape `square` and colour `white`, the starting positions (0, 0), (-20, 0), (-40, 0), the move distance 20, the directions UP 90, DOWN 270, LEFT 180, RIGHT 0, and the refresh delay 0.1 seconds. Add `tests/test_constants.py` that checks them (three distinct positions 20 pixels apart on one row, four distinct directions, positions inside the screen). | No | |
| 4 | Add the README | Write `README.md` with the Product Owner's template (Requirements, Set up for Windows PowerShell, Linux Debian and macOS, Run, Run the tests, Continuous integration, Build the source documentation, Project layout, License). Document creating a local `.venv`, `python -m pip install --upgrade pip` and `python -m pip install -e ".[dev]"`; name `python3-tk` and Debian 13 for Linux. The Run section is completed in MIL-003. Serves S02 and S03. | No | |
| 5 | Add the Doxyfile | Add a `Doxyfile` that reads `src/`, writes to `build/doxygen`, extracts documentation for Python (Doxygen comment style, `OPTIMIZE_OUTPUT_JAVA`) and treats warnings as failures, and document the command `doxygen Doxyfile` in the README. | No | |
| 6 | Add the continuous integration workflow | Add `.gitea/workflows/ci.yml` (run by Gitea Actions): check out, set up Python 3.13, `python -m pip install --upgrade pip`, `python -m pip install -e ".[dev]"`, run `pytest`, `ruff` and `mypy`. The tests need no display. The file lives in `.gitea/workflows`, not `.github/workflows`, because GitHub refuses a push that touches `.github/workflows` from a token without the workflow scope, which would block the push mirror to GitHub. | No | |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[a2c997e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/020-snake-game/commit/a2c997e1413e425050df8c50a976ec839ebb4752
