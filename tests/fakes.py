"""Fakes that stand in for turtles and the screen, so that no test opens a window."""

import os
import subprocess
import sys
import types
from pathlib import Path

import pytest

SRC = Path(__file__).resolve().parents[1] / "src"


class FakeSegment:
    """A segment that records what is done to it, in order."""

    def __init__(self) -> None:
        self.calls: list[tuple[str, tuple[object, ...]]] = []

    def shape(self, name: str, /) -> None:
        self.calls.append(("shape", (name,)))

    def color(self, color: str, /) -> None:
        self.calls.append(("color", (color,)))

    def penup(self) -> None:
        self.calls.append(("penup", ()))

    def goto(self, x: float, y: float, /) -> None:
        self.calls.append(("goto", (x, y)))

    def call_names(self) -> list[str]:
        """Return the names of the calls, in the order they were made."""
        return [name for name, _ in self.calls]


class FakeScreen:
    """A screen that records what is done to it, in order."""

    def __init__(self) -> None:
        self.calls: list[tuple[str, tuple[object, ...]]] = []

    def setup(self, width: float, height: float) -> None:
        self.calls.append(("setup", (width, height)))

    def bgcolor(self, color: str, /) -> None:
        self.calls.append(("bgcolor", (color,)))

    def title(self, titlestring: str, /) -> None:
        self.calls.append(("title", (titlestring,)))

    def exitonclick(self) -> None:
        self.calls.append(("exitonclick", ()))


def install_fake_turtle(
    monkeypatch: pytest.MonkeyPatch,
) -> tuple[list[FakeSegment], list[FakeScreen]]:
    """Replace the `turtle` module with a fake for one test.

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
        screen = FakeScreen()
        screens.append(screen)
        return screen

    module = types.ModuleType("turtle")
    module.__dict__["Turtle"] = make_segment
    module.__dict__["Screen"] = make_screen
    monkeypatch.setitem(sys.modules, "turtle", module)
    return segments, screens


def imports_turtle(module_name: str) -> bool:
    """Tell whether importing a module, in a fresh interpreter, imports `turtle`."""
    code = f"import sys, {module_name}; print('turtle' in sys.modules)"
    result = subprocess.run(
        [sys.executable, "-c", code],
        env={**os.environ, "PYTHONPATH": str(SRC)},
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    return result.stdout.strip() == "True"
