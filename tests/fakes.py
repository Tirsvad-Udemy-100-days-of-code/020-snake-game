"""Fakes that stand in for turtles and the screen, so that no test opens a window."""

import math
import os
import subprocess
import sys
import types
from collections.abc import Callable
from pathlib import Path

import pytest

from snake_game.snake import Snake

SRC = Path(__file__).resolve().parents[1] / "src"


class FakeTerminatorError(Exception):
    """Stands in for `turtle.Terminator`."""


class FakeTclError(Exception):
    """Stands in for `tkinter.TclError`."""


class FakeSegment:
    """A segment that records what is done to it, in order, and keeps its state."""

    def __init__(self) -> None:
        self.calls: list[tuple[str, tuple[object, ...]]] = []
        self.x = 0.0
        self.y = 0.0
        self.angle = 0.0

    def shape(self, name: str, /) -> None:
        self.calls.append(("shape", (name,)))

    def color(self, color: str, /) -> None:
        self.calls.append(("color", (color,)))

    def penup(self) -> None:
        self.calls.append(("penup", ()))

    def goto(self, x: float, y: float, /) -> None:
        self.calls.append(("goto", (x, y)))
        self.x, self.y = x, y

    def xcor(self) -> float:
        return self.x

    def ycor(self) -> float:
        return self.y

    def forward(self, distance: float, /) -> None:
        self.calls.append(("forward", (distance,)))
        radians = math.radians(self.angle)
        self.x += round(distance * math.cos(radians), 10)
        self.y += round(distance * math.sin(radians), 10)

    def heading(self) -> float:
        return self.angle

    def setheading(self, to_angle: float, /) -> None:
        self.calls.append(("setheading", (to_angle,)))
        self.angle = float(to_angle) % 360

    def call_names(self) -> list[str]:
        """Return the names of the calls, in the order they were made."""
        return [name for name, _ in self.calls]

    def position(self) -> tuple[float, float]:
        """Return where the segment is now."""
        return (self.x, self.y)


class FakeScreen:
    """A screen that records what is done to it, in order.

    After `frames_before_close` updates it behaves like a closed window: the next
    `update` raises `closing_error`.
    """

    def __init__(
        self,
        frames_before_close: int = 0,
        closing_error: type[Exception] = FakeTerminatorError,
    ) -> None:
        self.calls: list[tuple[str, tuple[object, ...]]] = []
        self.bindings: dict[str, Callable[[], object]] = {}
        self._updates_left = frames_before_close
        self._closing_error = closing_error

    def setup(self, width: float, height: float) -> None:
        self.calls.append(("setup", (width, height)))

    def bgcolor(self, color: str, /) -> None:
        self.calls.append(("bgcolor", (color,)))

    def title(self, titlestring: str, /) -> None:
        self.calls.append(("title", (titlestring,)))

    def tracer(self, n: int, /) -> None:
        self.calls.append(("tracer", (n,)))

    def listen(self) -> None:
        self.calls.append(("listen", ()))

    def onkey(self, fun: Callable[[], object], key: str) -> None:
        self.calls.append(("onkey", (key,)))
        self.bindings[key] = fun

    def update(self) -> None:
        self.calls.append(("update", ()))
        if self._updates_left == 0:
            raise self._closing_error
        self._updates_left -= 1

    def exitonclick(self) -> None:
        self.calls.append(("exitonclick", ()))

    def call_names(self) -> list[str]:
        """Return the names of the calls, in the order they were made."""
        return [name for name, _ in self.calls]


def make_snake() -> tuple[Snake, list[FakeSegment]]:
    """Make a snake whose segments are fakes, and return the fakes too."""
    created: list[FakeSegment] = []

    def factory() -> FakeSegment:
        segment = FakeSegment()
        created.append(segment)
        return segment

    return Snake(segment_factory=factory), created


def install_fake_turtle(
    monkeypatch: pytest.MonkeyPatch,
    *,
    frames_before_close: int = 0,
    closing_error: type[Exception] = FakeTerminatorError,
) -> tuple[list[FakeSegment], list[FakeScreen]]:
    """Replace the `turtle` and `tkinter` modules with fakes for one test.

    The fake screen acts like a window that the player closes after
    `frames_before_close` updates, by raising `closing_error` from `update`.
    Returns the lists that collect every segment and every screen the code under
    test creates.
    """
    segments: list[FakeSegment] = []
    screens: list[FakeScreen] = []

    def make_segment() -> FakeSegment:
        segment = FakeSegment()
        segments.append(segment)
        return segment

    def make_screen() -> FakeScreen:
        screen = FakeScreen(frames_before_close, closing_error)
        screens.append(screen)
        return screen

    turtle_module = types.ModuleType("turtle")
    turtle_module.__dict__["Turtle"] = make_segment
    turtle_module.__dict__["Screen"] = make_screen
    turtle_module.__dict__["Terminator"] = FakeTerminatorError
    tkinter_module = types.ModuleType("tkinter")
    tkinter_module.__dict__["TclError"] = FakeTclError
    monkeypatch.setitem(sys.modules, "turtle", turtle_module)
    monkeypatch.setitem(sys.modules, "tkinter", tkinter_module)
    return segments, screens


def imports_turtle_or_tkinter(module_name: str) -> bool:
    """Tell whether importing a module in a fresh interpreter loads a display module."""
    code = (
        f"import sys, {module_name}; "
        "print('turtle' in sys.modules or 'tkinter' in sys.modules)"
    )
    result = subprocess.run(
        [sys.executable, "-c", code],
        env={**os.environ, "PYTHONPATH": str(SRC)},
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    return result.stdout.strip() == "True"
