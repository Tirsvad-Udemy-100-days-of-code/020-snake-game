# MIL-005: Game over

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-08 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [710784f] |
| 2026-10-08 | Accepted | Jens Tirsvad Nielsen | S01 | Task 7 has its own title, because the sync matches issues by title and the old title was also the title of task 7 of MIL-003 | [710784f] |

---

## Purpose

This gate decides whether the game is complete: it ends when the head passes the wall or touches the tail, shows GAME OVER, and closes on a click. It covers the day-21 step "implementing game over conditions" (the wall and the tail) and it is the last gate of phase 2 (day 21) of [PP-001]. The work is delivered on the branch `mil-005-game-over` and one pull request.

## Deliverable

`Snake.hits_wall` and `Snake.hits_tail` in `snake.py`, `Scoreboard.game_over` in `scoreboard.py`, the end of the game and the wait for a click in `main.py`, the game-over constants in `constants.py`, the tests for each, and a finished `README.md` that describes the whole game. S01 compares the running game with the lecture video.

The lecture does the two checks inline in the loop. The plan puts them in methods of `Snake` so that tests can call them; that is the only change of structure, and the methods are named for the dictionary terms ([DICT-001]).

The numbers below are **assumptions** (see [MIL-004]); S01 confirms or replaces each against the video before task 1 is started (Go/No-Go criterion 1).

| Value | Assumed | Constant |
| --- | --- | --- |
| Wall | the head is outside when its x or y is beyond 280 on any side | `WALL_LIMIT` (from [MIL-004]) |
| Distance at which the head touches the tail | less than 10 pixels from any segment behind the head | `TAIL_COLLISION_DISTANCE` |
| Text at game over | `GAME OVER` | `GAME_OVER_TEXT` |
| Place, alignment and font of that text | the centre (0, 0), centred, the font of the scoreboard | `GAME_OVER_POSITION` |

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The assumed values are confirmed | S01 confirmed or replaced every value of the table in the Deliverable section against the video, and the pull request lists the final values | A value is unconfirmed or missing from the pull request |
| 2 | The wall ends the game | A manual run shows the game ending when the head passes the wall on each of the four sides; a test covers each side and the inside of the wall | The game goes on beyond the wall, or ends inside it |
| 3 | The tail ends the game | Turning the head into the body ends the game; normal movement, including the moves right after eating, does not | The game does not end, or ends without a touch |
| 4 | GAME OVER is shown | The text appears at the centre; the score stays visible; the snake no longer moves | No text, wrong place, or the snake moves on |
| 5 | A click closes the window | After game over a click closes the window and the program ends with exit code 0 | The window stays, or a traceback appears |
| 6 | Closing the window still ends quietly | Closing the window during play, and after game over, ends the program with exit code 0 and no traceback | A traceback |
| 7 | Constants are in one place | Every value of the table is a constant with a Doxygen comment, and no other module defines it | A value is a literal in another module |
| 8 | Earlier behaviour is unchanged | The tests of [MIL-001] to [MIL-004] still pass | A regression |
| 9 | Tests prove the behaviour | `pytest` exits 0 with no display; tests cover `hits_wall` on each side and just inside, `hits_tail` (touching, not touching, no tail), `game_over`, the end of the loop and the wait for a click, using fakes only | A failing test, or one of those behaviours has no test |
| 10 | `doxygen Doxyfile` builds | 0 warnings | Any warning |
| 11 | The README is finished | It describes the whole game (moving, food, score, game over, closing); it no longer says that food, score or game over are missing; a fresh clone reaches a green `pytest` by following it | A placeholder or an out-of-date sentence, or a command fails |
| 12 | The game matches the lecture | S01 compares the finished game with the lecture video and notes any difference in the pull request | An undocumented difference |
| 13 | The code is reviewed | `RC-*` against `QC-PY-001` has the verdict `Go` | Verdict `No-Go` or `Go-with-conditions` |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-004] accepted and merged | `Food`, `Scoreboard`, `WALL_LIMIT` and the eating check exist there |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 9: game over on the wall or the tail, GAME OVER, click to close | [BC-001], criterion 10 in Success Criteria |
| Objective 2: the assignment's names (`game_over`) | [BC-001], criterion 6 in Success Criteria |
| Objective 4: tests without a display | [BC-001], criterion 2 in Success Criteria |
| Objective 5: README and Doxygen | [BC-001], criteria 3, 4 in Success Criteria |
| Objective 6: traceable steps | [BC-001], criterion 7 in Success Criteria |
| Design of `hits_wall`, `hits_tail` and `game_over`: no Design Class Diagram exists; they trace to the day-21 outline and to tasks 2 to 4 below, a recorded deviation from `QC-PY-001` criterion 10 as in [MIL-002] | [PP-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-19 — last of the two gateways of phase 2 (day 21), inside the plan of [PP-001] that ends 2026-10-21.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add the game-over constants | Add `TAIL_COLLISION_DISTANCE`, `GAME_OVER_TEXT` and `GAME_OVER_POSITION` to `constants.py` with Doxygen comments, and extend `tests/test_constants.py` (the game-over place is inside the wall, the touch distance is smaller than the move distance). Start only after S01 confirmed the values. | No | |
| 2 | Detect the head passing the wall | Add `Snake.hits_wall`, which tells whether the x or the y of the head is beyond `WALL_LIMIT` on any side. The limit is the one that keeps the food inside the walls ([MIL-004]). | No | |
| 3 | Detect the head touching the tail | Add `Snake.hits_tail`, which loops over the segments behind the head with a slice (`segments[1:]`) and tells whether the head is closer than `TAIL_COLLISION_DISTANCE` to any of them. A snake that has only a head has no tail to touch. | No | |
| 4 | Show GAME OVER | Add `Scoreboard.game_over`, which goes to the game-over place and writes `GAME_OVER_TEXT` centred with the font of the scoreboard. The text is drawn at once: automatic drawing is off, so the screen is updated after it. | No | |
| 5 | End the game and wait for a click | In `main`, after each move, set `game_is_on` to false and call `scoreboard.game_over()` when the snake hits the wall or the tail; after the loop `screen.exitonclick()` waits for a click, which is now reached. Closing the window during play or while waiting still ends quietly ([MIL-003]). Put the check in a small function so that a test can call it. | No | |
| 6 | Test game over without a display | Test `hits_wall` on each of the four sides and just inside, `hits_tail` (touching, not touching, no tail, right after eating), `game_over` (text, place, alignment), the end of the loop after a hit, the wait for a click, and the quiet exit for a window closed after game over, using the fakes of [MIL-004]. | No | |
| 7 | Finish the README for the whole game | Rewrite the Status and Run sections of `README.md` for the whole game (moving, food, score, game over, closing), remove the sentences that say that food, score and game over are missing, update the Project layout, and confirm that `doxygen Doxyfile` ends with 0 warnings. | No | |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[DICT-001]: ../dictionary.md
[MIL-001]: ./mil-001-project-foundation.md
[MIL-002]: ./mil-002-screen-and-snake-body.md
[MIL-003]: ./mil-003-movement-and-keys.md
[MIL-004]: ./mil-004-food-and-score.md
[710784f]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/020-snake-game/commit/710784f2243e7ecf8cec23cbdd9cc58c96cdff96
