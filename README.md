# ChankArts X & O

`ChankArts X & O` is a Windows-friendly Tic Tac Toe desktop game built with Python and Tkinter. It runs offline, uses no third-party dependencies, and is a good fit for a Windows VM such as Parallels Desktop on macOS.

## Features

- 3x3 local two-player Tic Tac Toe
- X always starts first
- Turn status messaging
- Win detection for rows, columns, and diagonals
- Draw detection
- Winning cell highlight
- Scoreboard for X wins, O wins, and draws
- `New Game` and `Reset Score` controls
- Dark modern UI with hover feedback

## Requirements

- Windows with Python 3 installed
- Tkinter available in the Python installation

Most standard Windows Python installers include Tkinter by default.

## Run

From the project folder, run:

```powershell
python main.py
```

If `python` is not on your PATH, use the full Python path or the Python Launcher:

```powershell
py main.py
```

You can also launch the game directly with:

```powershell
.\play-game.bat
```

## Files

- `main.py`
- `README.md`
- `play-game.bat`

## Notes

- The game is fully offline.
- No `requirements.txt` is needed because the app uses only the Python standard library.
