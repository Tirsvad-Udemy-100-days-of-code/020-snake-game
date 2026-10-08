# MIL-003: Movement and keys

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-08 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [a2c997e] |
| 2026-10-08 | Accepted | Jens Tirsvad Nielsen | S01 | Task 3 names the exceptions a real window close raises (`_tkinter.TclError` and `turtle.Terminator`); task 4 and criterion 4 compare with the direction of the last move so that two key presses within one move cannot reverse the snake; task 6 lists the extra tests | [c033c7b] |

---

## Purpose

This gate decides whether the day-20 game state is complete: the snake moves by itself, every segment follows the one before it, and the arrow keys steer it without a reversal. It covers the lectures "Animating the Snake Segments on Screen" and "Controlling the Snake with Keypresses", and it is the last gate before the repository is finished. The work is delivered on the branch `mil-003-movement-and-keys` and one pull request.

## Deliverable

`Snake.move`, `Snake.head`, `Snake.up`, `Snake.down`, `Snake.left` and `Snake.right` in `snake.py`; the animation loop and the key bindings in `main.py`; the tests for each; and a finished `README.md` whose Run section says how to start the game and which keys steer it. S01 compares the running game with the lecture video.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The snake moves by itself | A manual run shows the snake moving to the right at 20 pixels every 0.1 seconds without flicker and without a trail | It does not move, moves segment by segment, flickers, or leaves a trail |
| 2 | Segments follow the head | While turning, the segments follow the path of the head with no gap and no split; `move` sends each segment, from the tail to the second segment, to the position of the segment before it, then moves the head forward by `MOVE_DISTANCE` | A segment takes its own direction instead of the position before it |
| 3 | The arrow keys steer | Up, Down, Left and Right set the head to 90, 270, 180 and 0 degrees through `Snake.up`, `Snake.down`, `Snake.left` and `Snake.right`, with constants for the headings | A key does nothing, or a heading is a literal outside `constants.py` |
| 4 | The snake never reverses | While the snake moves down, Up is ignored; while it moves up, Down is ignored; the same for left and right; two key presses within one move (for example Up then Left while moving right) do not reverse it either | A reversal is accepted |
| 5 | The window closes cleanly | Closing the window ends the program with exit code 0 and no traceback | A traceback, or a non-zero exit code |
| 6 | Tests prove the behaviour | `pytest` exits 0; tests cover `move` (positions after one move and after a turn), all four directions from each starting direction (a table of cases), the refused reversals, the key bindings and one frame of the loop, using fakes only | A failing test, or one of those behaviours has no test |
| 7 | `doxygen Doxyfile` builds | 0 warnings | Any warning |
| 8 | The README is finished | The Run section gives the command `python -m snake_game`, names the arrow keys and says that food, score and game over are day 21; a fresh clone reaches a green `pytest` by following the README | A section is still a placeholder, or a command fails |
| 9 | The game matches the lecture | S01 compares the finished game with the lecture video and notes any difference in the pull request | An undocumented difference |
| 10 | The code is reviewed | `RC-*` against `QC-PY-001` has the verdict `Go` | Verdict `No-Go` or `Go-with-conditions` |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-002] accepted and merged | The `Snake` class, the segments and the main flow are created there |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 1: movement, keys and no reversal as in the lectures | [BC-001], criterion 1 in Success Criteria |
| Objective 2: the assignment's names (`move`, `up`, `down`, `left`, `right`, `head`, `game_is_on`) | [BC-001], criterion 6 in Success Criteria |
| Objective 4: tests without a display | [BC-001], criterion 2 in Success Criteria |
| Objective 5: README and Doxygen | [BC-001], criteria 3, 4 in Success Criteria |
| Objective 6: traceable steps | [BC-001], criterion 7 in Success Criteria |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-13 — last of three gateways, inside the one-week plan of [PP-001] that ends 2026-10-15.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add Snake.move with the following segments | Add `Snake.move` as in the lecture: loop over the segments from the last to the second with a reverse `range`, send each to the `xcor` and `ycor` of the segment before it, then move the head forward by `MOVE_DISTANCE`. This keeps the body joined while turning, however many segments there are. | No | |
| 2 | Add the animation loop | In `main`, turn off automatic drawing with `screen.tracer(0)`, then loop while `game_is_on`: `screen.update()`, wait `REFRESH_DELAY_SECONDS`, `snake.move()`. Put one pass of the loop body in a small function so a test can call it once with fakes. | No | |
| 3 | Close the window without a traceback | Closing the window during the animation loop raises `_tkinter.TclError` ("invalid command name") from `screen.update()`, as found by closing a real turtle window in a loop; `turtle.Terminator` is the exception that `turtle` raises in other calls once its window is gone. Catch exactly these two around the loop in `main` so the program ends with exit code 0, and keep `screen.exitonclick()` after the loop for the day-21 game over. Risk named in the Business Case. | No | |
| 4 | Add Snake.head and the direction methods | Add the `head` attribute (the first segment) and `up`, `down`, `left`, `right`. Each turns the head to its direction with the constants `UP`, `DOWN`, `LEFT`, `RIGHT` unless the snake last moved the opposite way, so the snake cannot reverse onto itself. The test is against the direction of the last move and not against the current direction of the head: the lecture's test lets two key presses within one move (Up then Left while moving right) reverse the snake. | No | |
| 5 | Bind the arrow keys | In `main`, call `screen.listen()` and bind the keys `Up`, `Down`, `Left` and `Right` with `screen.onkey` to the four `Snake` methods. Put the bindings in a function that takes the screen and the snake, so a test can check them with a fake screen. | No | |
| 6 | Test movement and steering without a display | Extend `tests/test_snake.py` and `tests/test_main.py` with fakes that remember `goto`, `forward`, `setheading`, `heading`, `xcor`, `ycor`: the positions after one move and after a turn, a table of every direction from every starting direction including the refused reversals, two key presses within one move, the key bindings, one frame of the loop, and the clean exit when the window is closed. | No | |
| 7 | Finish the README and the documentation | Complete the Run section of `README.md` (`python -m snake_game`, the arrow keys, the day-21 note), re-check the Project layout section, and confirm that `doxygen Doxyfile` ends with 0 warnings. | No | |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-002]: ./mil-002-screen-and-snake-body.md
[a2c997e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/020-snake-game/commit/a2c997e1413e425050df8c50a976ec839ebb4752
[c033c7b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/020-snake-game/commit/c033c7b660f8b9dcabf13d7556ef6c4e21b7d3a4
