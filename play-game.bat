@echo off
setlocal

set "GAME_DIR=%~dp0"
set "PYTHONW=%LocalAppData%\Programs\Python\Python313\pythonw.exe"
set "PYTHON=%LocalAppData%\Programs\Python\Python313\python.exe"

if exist "%PYTHONW%" (
    start "" "%PYTHONW%" "%GAME_DIR%main.py"
    exit /b 0
)

if exist "%PYTHON%" (
    start "" "%PYTHON%" "%GAME_DIR%main.py"
    exit /b 0
)

where py >nul 2>nul
if %errorlevel%==0 (
    start "" py "%GAME_DIR%main.py"
    exit /b 0
)

where python >nul 2>nul
if %errorlevel%==0 (
    start "" python "%GAME_DIR%main.py"
    exit /b 0
)

echo Python was not found. Please install Python 3 for Windows and try again.
pause
