# RC-007: Review of the MIL-001 code

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-007 |
| CrossReference | [MIL-001], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-08 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: the Python code of [MIL-001]: `src/snake_game/__init__.py`, `src/snake_game/constants.py` and `tests/test_constants.py`
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a (source code is a technical type)
- Language reviewer: none

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Package `snake_game`, modules `constants`, tests `test_constants.py`; constants are `UPPER_SNAKE`; test functions are `snake_case`. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names are the lectures' own (`STARTING_POSITIONS`, `MOVE_DISTANCE`, `UP`, `DOWN`, `LEFT`, `RIGHT`) and state purpose; no abbreviations. `x` and `y` in comprehensions are coordinates in a tiny scope. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check .` reports "All checks passed!" and `ruff format --check .` reports all files formatted (rule set E, F, W, I, N, UP, B, SIM in `pyproject.toml`); no `noqa` or other suppression exists. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Every test function is annotated `-> None`; every constant is annotated `Final[...]`. There are no other functions. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | N-A | No exception handling in this change. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No default arguments; no builtin is shadowed. |
| 7 | Files, locks and connections are managed with context managers | N-A | No files, locks or connections in this change. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Module docstring in `__init__.py` and `constants.py`; every constant has a Doxygen `##` comment; `doxygen Doxyfile` ends with exit code 0 (warnings fail the build). |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | N-A | No logging or `print` in this change; no secret or personal data in any file (the two token values of `.env` were searched for in all 140 non-ignored files: none found). |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No class or operation in this change; the module holds constants only. Note for MIL-002: the `Snake` class will trace to no Design Class Diagram because none exists in this project (open issue in [PP-001]); that deviation must be recorded before the review of MIL-002. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 13 tests in `tests/test_constants.py`, each named for one behaviour (for example `test_starting_positions_are_one_move_distance_apart`), independent of order, with no network and no window; `pytest` exits 0. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy` (strict, from `pyproject.toml`) reports "Success: no issues found in 3 source files"; `Any` is not used. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Fail | `dependencies = []` and the `dev` extra (pytest, ruff, mypy) is used by CI, so nothing is unused; but the dev tools have lower bounds (`>=`), not exact pins. Optional criterion; accepted for a learning project with no runtime dependencies. |

## Other Go/No-Go checks of MIL-001 run for this review

| # | Criterion of [MIL-001] | Result |
| --- | --- | --- |
| 1 | Fresh `.venv`, `python -m pip install --upgrade pip`, `python -m pip install -e ".[dev]"` in Windows PowerShell | All three exit 0 (pip 26.2.1, snake-game 0.1.0 installed) |
| 2 | `pytest` | 13 passed, exit 0, no window opened |
| 3 | `pyproject.toml` | `requires-python = ">=3.13"`, `dependencies = []`, `dev` extra with pytest |
| 4 | `.gitignore` | `git check-ignore .venv .env __pycache__ build` lists all four |
| 5 | Constants only in `constants.py` | No other module exists yet |
| 6 | `doxygen Doxyfile` | Exit 0, `build/doxygen/index.html` written, constants documented |
| 7 | README follows the template | Headings in the order of the template: Requirements, Set up (Windows powershell, Linux debian, MacOS), Run, Run the tests, Continuous integration, Build the source documentation, Project layout, License |
| 8 | CI workflow | `.gitea/workflows/ci.yml` installs `.[dev]` and runs pytest, ruff and mypy on Python 3.13; nothing exists under `.github/workflows`. **Not executed**: no run was available; the same commands were run locally |
| 9 | Repository page | Description and 12 topics set on the Gitea repository on 2026-10-08 |
| 11 | No secret in the change | No token value of `.env` found in any non-ignored file; `.env` is ignored by `.git/info/exclude` and by `.gitignore` |

## Overall Verdict

Go — all Mandatory criteria pass or are not applicable, and the one Fail (criterion 13) is Optional. The rows above were assessed on 2026-10-08 by the assistant that wrote the code, at S01's request in chat. This review is **not independent**; S01 is the approver and can overrule the verdict at the pull request. Criterion 8 of [MIL-001] was checked by running the commands locally, not by a CI run.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Decide before the review of MIL-002 whether a Design Class Diagram is wanted for `Snake`, or record in [MIL-002] that the class traces to the lecture instead (criterion 10) | S01 | 2026-10-11 |
| Run the CI workflow once a runner is available and note the result in the pull request | S01 | 2026-10-09 |
| Decide whether to pin the development tools exactly (criterion 13) | S01 | 2026-10-13 |

---

[MIL-001]: ../../milestones/mil-001-project-foundation.md
[MIL-002]: ../../milestones/mil-002-screen-and-snake-body.md
[PP-001]: ../../project-plan.md
[QC-PY-001]: ../../../framework/qc/qc-programming-python.md
