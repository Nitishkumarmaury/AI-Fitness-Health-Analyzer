@echo off
echo ===== AI Fitness Health Analyzer - Quick Deploy =====
echo.

echo Choose deployment option:
echo 1. Streamlit Cloud (Easiest)
echo 2. Railway (Full Stack)
echo 3. Push to GitHub only
echo 4. Local Test
echo.

set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" (
    echo Preparing for Streamlit deployment...
    python deploy_streamlit.py
) else if "%choice%"=="2" (
    echo Preparing for Railway deployment...
    python deploy_railway.py
) else if "%choice%"=="3" (
    echo Pushing to GitHub...
    call push_to_github.bat
) else if "%choice%"=="4" (
    echo Starting local test...
    python run_streamlit.py
) else (
    echo Invalid choice.
)

pause
