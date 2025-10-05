@echo off
echo ===== Python Version Check =====
echo.

python --version
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH
    echo Please install Python 3.7 or higher
    pause
    exit /b 1
)

echo.
echo Detailed version information:
python check_python_version.py

echo.
echo Python location:
where python

echo.
echo Pip version:
python -m pip --version

pause
