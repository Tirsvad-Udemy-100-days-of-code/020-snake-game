"""Tests of the main flow, with fakes instead of a real screen."""

import pytest

from fakes import FakeScreen, imports_turtle, install_fake_turtle
from snake_game import constants
from snake_game.main import configure_screen, main


def test_configure_screen_sets_size_background_and_title_and_nothing_else() -> None:
    screen = FakeScreen()

    configure_screen(screen)

    assert screen.calls == [
        ("setup", (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)),
        ("bgcolor", (constants.SCREEN_BACKGROUND_COLOR,)),
        ("title", (constants.SCREEN_TITLE,)),
    ]


def test_main_sets_up_one_screen_and_waits_for_a_click(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _, screens = install_fake_turtle(monkeypatch)

    main()

    assert len(screens) == 1
    names = [name for name, _ in screens[0].calls]
    assert names == ["setup", "bgcolor", "title", "exitonclick"]


def test_main_draws_the_snake_before_it_waits_for_a_click(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    turtles, _ = install_fake_turtle(monkeypatch)

    main()

    assert len(turtles) == len(constants.STARTING_POSITIONS)
    assert all(
        ("goto", position) in turtle.calls
        for turtle, position in zip(turtles, constants.STARTING_POSITIONS, strict=True)
    )


def test_importing_the_main_module_does_not_import_turtle() -> None:
    assert not imports_turtle("snake_game.main")
