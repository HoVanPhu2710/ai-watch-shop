@echo off
chcp 65001 >nul

echo ==== Multi-Server Launcher: Rasa + AI Recommendation ====
echo.

REM -- 1. Start Rasa Action Server (window 1)
echo [1/4] Starting Rasa Action Server on port 5055...
start "Rasa Action Server" cmd /k "cd /d %~dp0chatbot2 && call start_actions.bat"
TIMEOUT /T 2 >nul

REM -- 2. Start Rasa Server (window 2)
echo [2/4] Starting Rasa Core Server on port 5005...
start "Rasa Server" cmd /k "cd /d %~dp0chatbot2 && call start_server.bat"
TIMEOUT /T 2 >nul

REM -- 3. Start AI Recommendation Server (window 3)
echo [3/4] Starting AI Python server (Flask) on port 5001...
start "AI Server" cmd /k "cd /d %~dp0ai-recommend && call setup_and_start.bat"
TIMEOUT /T 2 >nul

REM -- 4. Start Scheduler (window 4)
echo [4/4] Starting Scheduler for auto training/generation...
start "Scheduler" cmd /k "cd /d %~dp0ai-recommend && call start_scheduler.bat"
echo All servers started in new windows.
echo. & pause
exit /b
