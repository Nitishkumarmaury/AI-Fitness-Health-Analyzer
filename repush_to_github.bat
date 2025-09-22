@echo off
echo ===== AI Fitness Health Analyzer - Re-Push to GitHub =====
echo.

REM Check if git is installed
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Git is not installed or not in your PATH.
    echo Please install Git from https://git-scm.com/
    pause
    exit /b 1
)

REM Check if we're in a git repository
if not exist .git (
    echo Error: Not a git repository.
    echo Please run push_to_github.bat first to initialize the repository.
    pause
    exit /b 1
)

echo Current repository status:
git status --porcelain

echo.
echo Adding all changes to git...
git add .

echo.
echo Checking for changes to commit...
git diff --cached --quiet
if %errorlevel% neq 0 (
    echo Creating commit with latest changes...
    set /p commit_message="Enter commit message (or press Enter for default): "
    
    if "%commit_message%"=="" (
        set commit_message=🚀 Update: Complete AI Fitness Health Analyzer with all components and fixes
    )
    
    git commit -m "%commit_message%"
    echo.
) else (
    echo No changes detected to commit.
    echo.
)

echo Current branch:
git branch --show-current

echo.
echo Force pushing to GitHub (this will overwrite remote)...
git push --force-with-lease origin main

if %errorlevel% equ 0 (
    echo.
    echo ✅ Successfully re-pushed to GitHub!
    echo.
    echo 🌐 Repository: https://github.com/Nitishkumarmaury/AI-Fitness-Health-Analyzers
    echo.
    echo 📝 Recent commits:
    git log --oneline -5
    echo.
    echo 🎉 Next Steps - Deploy for FREE:
    echo.
    echo 1. 🎯 Streamlit Cloud:
    echo    - Go to https://share.streamlit.io
    echo    - Connect your updated GitHub repo
    echo    - Set main file: app.py
    echo    - Add secret: GEMINI_API_KEY
    echo.
    echo 2. 🚂 Railway:
    echo    - Go to https://railway.app
    echo    - Redeploy from updated GitHub repo
    echo    - Environment variables will be preserved
    echo.
    echo 3. ⚡ Vercel:
    echo    - Go to https://vercel.com
    echo    - Auto-deploy will trigger from GitHub
    echo.
) else (
    echo.
    echo ❌ Failed to push to GitHub.
    echo.
    echo Possible solutions:
    echo 1. Check your internet connection
    echo 2. Verify your GitHub credentials
    echo 3. Try regular push: git push origin main
    echo 4. If conflicts exist, try: git pull origin main
    echo.
    echo Trying regular push...
    git push origin main
    
    if %errorlevel% equ 0 (
        echo ✅ Regular push successful!
    else (
        echo ❌ Regular push also failed. Manual intervention needed.
        echo.
        echo Manual commands to try:
        echo git pull origin main
        echo git push origin main
    )
)

echo.
echo 🌟 Repository updated! Opening GitHub...
pause >nul
start https://github.com/Nitishkumarmaury/AI-Fitness-Health-Analyzers

pause
