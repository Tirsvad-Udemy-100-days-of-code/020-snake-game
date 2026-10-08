# Snake Game

The classic Snake game, built object-oriented with Python's `turtle` module. It is
the day-20 assignment of Udemy's *100 Days of Code: The Complete Python Pro
Bootcamp*: a snake of three square segments moves across a black 600 by 600
screen by itself and is steered with the arrow keys, but never turns straight
back onto itself. Food, score and game over belong to day 21 and are not part of
this repository.

The game has no runtime dependencies. The code keeps the names of the lectures
(`Snake`, `create_snake`, `move`, `up`, `down`, `left`, `right`, `segments`,
`head`, `game_is_on`) so that you can compare it with your own solution.

> **Status:** under construction. The project foundation (this README, the
> configuration, `constants.py` and the tests of the constants) is in place. The
> window and the snake are added in the next milestone and the movement and keys
> in the last one; see `docs/project-plan.md`.

## Requirements

- Python 3.13 or newer, with `tkinter` (the `turtle` module needs it).
- `git`, to clone the repository.
- Optional: [Doxygen](https://www.doxygen.nl/) to build the source documentation.
- No runtime dependencies. The development tools (`pytest`, `ruff`, `mypy`) are
  installed into the virtual environment by the `dev` extra.

## Set up

Clone the repository, then create a local virtual environment `.venv` in its
root, upgrade `pip` and install the project with its development tools. The
`.venv` folder is ignored by git.

```bash
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/020-snake-game.git
cd 020-snake-game
```

### Windows powershell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

If PowerShell refuses to run the activation script, allow scripts for this
window only with `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned`
and activate again. Python from python.org includes `tkinter`.

### Linux debian

Debian 13 or newer ships Python 3.13. On older releases install Python 3.13
separately.

```bash
sudo apt install python3 python3-venv python3-tk
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

### MacOS

```bash
brew install python@3.13 python-tk@3.13
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Run

With the virtual environment active:

```bash
python -m snake_game
```

This command works once the game is finished (see the status above). The arrow
keys steer the snake; click the window to close it.

## Run the tests

The tests need no display: they use fakes instead of real turtles.

```bash
pytest
```

The same checks that continuous integration runs:

```bash
python -m pytest
python -m ruff check src tests
python -m ruff format --check src tests
python -m mypy
```

## Continuous integration

`.gitea/workflows/ci.yml` runs on Gitea Actions on every push and on every pull
request. It sets up Python 3.13, upgrades `pip`, installs `.[dev]`, then runs
`pytest`, `ruff` (lint and format check) and `mypy`. It does not build the source
documentation: run `doxygen Doxyfile` yourself, as the next section shows. No
step opens a turtle window.

The workflow lives in `.gitea/workflows` and not in `.github/workflows`, so
GitHub does not run it and pushing to the GitHub mirror needs no workflow
permission.

## Build the source documentation

The source is documented with Doxygen comments and the `Doxyfile` in the root.
Install Doxygen (`winget install DimitriVanHeesch.Doxygen` on Windows,
`sudo apt install doxygen` on Debian, `brew install doxygen` on macOS), then:

```bash
doxygen Doxyfile
```

The HTML is written to `build/doxygen/index.html`. A warning fails the build.

## Project layout

```text
.
├── .gitea/workflows/ci.yml    continuous integration (Gitea Actions)
├── docs/                      business case, plan, milestones, reviews
├── src/snake_game/            the game
│   ├── __init__.py
│   └── constants.py           every constant of the game
├── tests/                     pytest tests
├── Doxyfile                   source documentation settings
├── LICENSE
├── pyproject.toml             project configuration
└── README.md
```

## License

GNU Affero General Public License v3.0 only. See [LICENSE](LICENSE).
