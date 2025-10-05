@echo off
echo Pushing AI Fitness Health Analyzer to GitHub...
echo.

REM Check if git is installed
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Git is not installed or not in your PATH.
    echo Please install Git from https://git-scm.com/
    pause
    exit /b 1
)

REM Initialize git repository if not already done
if not exist .git (
    echo Initializing Git repository...
    git init
    echo.
)

REM Add all files to staging
echo Adding all files to Git...
git add .

REM Check if there are changes to commit
git diff --cached --quiet
if %errorlevel% neq 0 (
    echo Creating commit...
    git commit -m "Initial commit: AI Fitness Health Analyzer with React and Streamlit versions"
    echo.
) else (
    echo No changes to commit. Checking if remote exists...
)

REM Check if remote already exists
git remote get-url origin >nul 2>&1
if %errorlevel% neq 0 (
    echo Adding remote repository...
    git remote add origin https://github.com/Nitishkumarmaury/AI-Fitness-Health-Analyzers.git
    echo.
) else (
    echo Remote origin already exists.
)

REM Set main branch and push
echo Setting main branch and pushing to GitHub...
git branch -M main
git push -u origin main

if %errorlevel% equ 0 (
    echo.
    echo ✅ Successfully pushed to GitHub!
    echo 🔗 Repository URL: https://github.com/Nitishkumarmaury/AI-Fitness-Health-Analyzers
    echo.
) else (
    echo.
    echo ❌ Failed to push to GitHub. Please check your credentials and try again.
    echo.
)

pause
