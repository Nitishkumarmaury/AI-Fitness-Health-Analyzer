@echo off
echo ===== AI Fitness Health Analyzer =====
echo.

rem Check for Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python not found. Please install Python.
    pause
    exit /b 1
)

rem Check for frontend build
if not exist frontend\build (
    echo Frontend build not found. Building now...
    
    if not exist frontend\node_modules (
        echo Installing frontend dependencies...
        cd frontend
        call npm install
        cd ..
    )
    
    echo Building frontend...
    cd frontend
    call npm run build
    cd ..
)

rem Check for .env file
if not exist .env (
    echo Creating .env file template...
    echo GEMINI_API_KEY=your_api_key_here > .env
    echo.
    echo IMPORTANT: Edit the .env file with your actual Gemini API key.
    echo.
)

rem Install Python dependencies if needed
echo Checking Python dependencies...
pip install -r requirements.txt >nul 2>&1

echo.
echo Starting the application...
echo Access the app at: http://localhost:5000
echo Press Ctrl+C to stop the server
echo.

python run.py
