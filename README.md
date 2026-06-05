# ChankArts X & O

`ChankArts X & O` is a polished offline Tic Tac Toe desktop game for Windows, built with Python and Tkinter. It is designed to be lightweight, easy to run, and friendly to a normal Windows setup, including a Windows 11 VM running inside Parallels Desktop on macOS.

This is a fun little `ChankArts` game made for Windows PC players who want something simple, clean, and instantly playable without needing a browser, internet connection, or a heavy install process.

## Overview

This project is a clean two-player local `X` and `O` game with a dark modern interface, live score tracking, clear turn messaging, and proper end-game handling.

The app focuses on:

- simple setup
- no third-party dependencies
- offline play
- a better-than-default Tkinter presentation

## From ChankArts

`ChankArts X & O` is meant to feel like a small creative desktop release rather than just a coding exercise. The idea behind it is simple:

- make a classic game feel neat and presentable on Windows
- keep the experience fast and lightweight
- make something easy to share, open, and enjoy on a PC

It is a compact project, but it still tries to carry a little personality in the visuals, the naming, and the overall presentation.

## Features

- 3x3 Tic Tac Toe board
- local two-player mode
- `X` always starts first
- live status text for turns, wins, and draws
- win detection for rows, columns, and diagonals
- draw detection when the board fills with no winner
- winning line highlight
- move lock after game over
- `New Game` button for resetting the board
- `Reset Score` button for clearing the scoreboard
- scoreboard for:
  - `X Wins`
  - `O Wins`
  - `Draws`
- dark theme with hover feedback on empty cells
- centered desktop window layout

## Tech Stack

- Python 3
- Tkinter from the Python standard library

No external packages are required.

## Requirements

- Windows 10 or Windows 11
- Python 3 installed
- Tkinter available in the Python installation

Most standard Python installers for Windows include Tkinter by default.

## Project Files

- `main.py`  
  The game itself, including UI and game-state logic.

- `play-game.bat`  
  A convenience launcher for Windows.

- `README.md`  
  Project documentation and usage notes.

## How To Run

### Option 1: Run with Python

From the project folder:

```powershell
python main.py
```

If `python` is not available on your PATH, try:

```powershell
py main.py
```

### Option 2: Run with the Windows launcher

Double-click:

```powershell
play-game.bat
```

Or from PowerShell:

```powershell
.\play-game.bat
```

## How To Play

1. Player `X` starts first.
2. Players take turns placing `X` and `O`.
3. The first player to complete a row, column, or diagonal wins.
4. If all cells are filled and nobody wins, the match is a draw.
5. Use `New Game` to start the next round while keeping the scores.
6. Use `Reset Score` to clear the board and all scoreboard values.

## Controls

- Left click an empty square to place your mark
- `New Game` resets only the current round
- `Reset Score` resets both the round and the scoreboard

## Visual Design Notes

The interface uses a dark theme with:

- bold red styling for `X`
- bright blue styling for `O`
- highlighted winner cells
- hover feedback on empty board squares
- centered layout sized for a normal desktop window

The goal was to keep the app feeling cleaner and more intentional than stock Tkinter defaults.

## Why This Project

This game was built as a small Windows-friendly `ChankArts` release that shows how even a simple classic game can be packaged with a bit more care. Instead of leaving it as a plain classroom-style Tic Tac Toe program, the project adds:

- a stronger visual identity
- a proper desktop window feel
- score tracking across rounds
- quick launch behavior for Windows users

The result is still simple, but it feels more like a real desktop mini-game.

## Testing

The game logic was checked for:

- horizontal win detection
- vertical win detection
- diagonal win detection
- draw detection
- score updates
- board reset behavior
- score reset behavior
- prevention of extra moves after game over

## Offline Use

This project runs fully offline. It does not use:

- web APIs
- paid services
- cloud services
- external game engines

## Troubleshooting

### `python` is not recognized

Install Python 3 for Windows and enable the option to add Python to `PATH` during installation.

### Tkinter does not open

Use a normal Windows Python installation from `python.org`. Standard installers usually include the required Tkinter components.

### Double-clicking the launcher does nothing

Open PowerShell in the project folder and run:

```powershell
python main.py
```

This usually reveals whether Python is missing or installed in a different location.

## Notes

- The app uses only the Python standard library.
- No `requirements.txt` is needed.
- The project is a good starter example for small Windows desktop games built without heavy frameworks.
- It is also a small fun game release from `ChankArts`, made with Windows PC playability in mind.
