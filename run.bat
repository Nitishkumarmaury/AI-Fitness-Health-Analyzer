@echo off
echo Starting AI Fitness Health Analyzer...
echo.

:: Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in your PATH.
    echo Please install Python 3.7 or higher.
    pause
    exit /b 1
)

:: Check if .env file exists
if not exist .env (
    echo Warning: .env file not found.
    echo Creating a template .env file. Please edit it with your API key.
    echo GEMINI_API_KEY=your_api_key_here > .env
    echo.
)

:: Check if frontend build exists
if not exist frontend\build (
    echo Frontend build not found. Building now...
    cd frontend
    
    echo Installing dependencies...
    call npm install
    
    echo Building frontend...
    call npm run build
    
    cd ..
)

:: Start the server
echo Starting server...
python run.py

pause
