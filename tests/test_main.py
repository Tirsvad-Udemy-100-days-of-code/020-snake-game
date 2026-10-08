"""Tests of the main flow, with fakes instead of a real screen."""

import pytest

from fakes import (
    FakeScreen,
    FakeTclError,
    FakeTerminatorError,
    imports_turtle_or_tkinter,
    install_fake_turtle,
    make_snake,
)
from snake_game import constants
from snake_game.main import bind_keys, configure_screen, main, play_frame

ARROW_KEYS = ("Up", "Down", "Left", "Right")


@pytest.fixture
def sleeps(monkeypatch: pytest.MonkeyPatch) -> list[float]:
    """Replace `time.sleep` for one test and collect the waits requested."""
    waited: list[float] = []
    monkeypatch.setattr("time.sleep", waited.append)
    return waited


def test_configure_screen_sets_size_background_and_title_and_nothing_else() -> None:
    screen = FakeScreen()

    configure_screen(screen)

    assert screen.calls == [
        ("setup", (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)),
        ("bgcolor", (constants.SCREEN_BACKGROUND_COLOR,)),
        ("title", (constants.SCREEN_TITLE,)),
    ]


def test_bind_keys_listens_and_binds_the_four_arrow_keys_to_the_snake() -> None:
    screen = FakeScreen()
    snake, _ = make_snake()

    bind_keys(screen, snake)

    assert screen.call_names() == ["listen", "onkey", "onkey", "onkey", "onkey"]
    assert screen.bindings == {
        "Up": snake.up,
        "Down": snake.down,
        "Left": snake.left,
        "Right": snake.right,
    }


@pytest.mark.parametrize(
    ("key", "degrees"),
    [("Up", constants.UP), ("Down", constants.DOWN), ("Right", constants.RIGHT)],
)
def test_pressing_a_bound_key_turns_the_head(key: str, degrees: int) -> None:
    screen = FakeScreen()
    snake, _ = make_snake()
    bind_keys(screen, snake)

    screen.bindings[key]()

    assert snake.head.heading() == degrees


def test_play_frame_updates_the_screen_then_waits_then_moves(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    screen = FakeScreen(frames_before_close=1)
    snake, created = make_snake()
    seen: list[tuple[float, list[str], list[str]]] = []

    def record_sleep(seconds: float) -> None:
        seen.append((seconds, screen.call_names(), created[0].call_names()))

    monkeypatch.setattr("time.sleep", record_sleep)

    play_frame(screen, snake)

    assert len(seen) == 1
    seconds, screen_calls_at_sleep, head_calls_at_sleep = seen[0]
    assert seconds == constants.REFRESH_DELAY_SECONDS
    assert screen_calls_at_sleep == ["update"]
    assert "forward" not in head_calls_at_sleep
    assert "forward" in created[0].call_names()


def test_main_sets_up_the_screen_turns_off_drawing_and_binds_the_keys(
    monkeypatch: pytest.MonkeyPatch, sleeps: list[float]
) -> None:
    _, screens = install_fake_turtle(monkeypatch)

    main()

    assert len(screens) == 1
    assert screens[0].call_names()[:9] == [
        "setup",
        "bgcolor",
        "title",
        "tracer",
        "listen",
        "onkey",
        "onkey",
        "onkey",
        "onkey",
    ]
    assert ("tracer", (0,)) in screens[0].calls
    assert sorted(screens[0].bindings) == sorted(ARROW_KEYS)


def test_main_draws_the_snake_before_the_first_frame(
    monkeypatch: pytest.MonkeyPatch, sleeps: list[float]
) -> None:
    turtles, _ = install_fake_turtle(monkeypatch)

    main()

    assert len(turtles) == len(constants.STARTING_POSITIONS)
    assert all(
        ("goto", position) in turtle.calls
        for turtle, position in zip(turtles, constants.STARTING_POSITIONS, strict=True)
    )


@pytest.mark.parametrize("closing_error", [FakeTerminatorError, FakeTclError])
def test_main_ends_quietly_when_the_window_is_closed(
    monkeypatch: pytest.MonkeyPatch,
    sleeps: list[float],
    closing_error: type[Exception],
) -> None:
    turtles, screens = install_fake_turtle(
        monkeypatch, frames_before_close=3, closing_error=closing_error
    )

    main()

    assert screens[0].call_names().count("update") == 3 + 1
    assert turtles[0].call_names().count("forward") == 3
    assert sleeps == [constants.REFRESH_DELAY_SECONDS] * 3
    assert "exitonclick" not in screens[0].call_names()


def test_main_lets_other_errors_through(
    monkeypatch: pytest.MonkeyPatch, sleeps: list[float]
) -> None:
    install_fake_turtle(monkeypatch, closing_error=KeyError)

    with pytest.raises(KeyError):
        main()


def test_importing_the_main_module_does_not_import_turtle_or_tkinter() -> None:
    assert not imports_turtle_or_tkinter("snake_game.main")
