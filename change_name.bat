@echo off
setlocal

:: Check for properties.json
set "jsonPath=boiii_players\properties.json"
if not exist "%jsonPath%" (
    echo [ERROR] File not found: %jsonPath%
    pause
    exit /b
)

:: Prompt for new username
set /p newName=Enter new player name: 

:: Overwrite the file with new JSON content
> "%jsonPath%" echo {^"playerName^":^"%newName%^"}

echo Player name updated successfully to: %newName%
pause
