@echo off
echo ===== Git Commands for AI Fitness Health Analyzer =====
echo.

echo Choose an option:
echo 1. Quick push (add, commit, push)
echo 2. Force push (overwrite remote)
echo 3. Check status
echo 4. View commit history
echo 5. Pull latest changes
echo 6. Reset to last commit (DANGER)
echo.

set /p choice="Enter your choice (1-6): "

if "%choice%"=="1" (
    echo Quick push...
    git add .
    set /p msg="Commit message: "
    if "%msg%"=="" set msg="Update project files"
    git commit -m "%msg%"
    git push origin main
) else if "%choice%"=="2" (
    echo Force push - this will overwrite remote repository!
    set /p confirm="Are you sure? Type 'yes' to continue: "
    if "%confirm%"=="yes" (
        git add .
        git commit -m "Force update: Complete project rebuild"
        git push --force origin main
        echo ✅ Force push complete!
    ) else (
        echo Cancelled.
    )
) else if "%choice%"=="3" (
    echo Repository status:
    git status
    echo.
    echo Recent commits:
    git log --oneline -5
) else if "%choice%"=="4" (
    echo Recent commit history:
    git log --oneline -10
) else if "%choice%"=="5" (
    echo Pulling latest changes...
    git pull origin main
) else if "%choice%"=="6" (
    echo DANGER: This will reset to last commit and lose changes!
    set /p confirm="Type 'RESET' to confirm: "
    if "%confirm%"=="RESET" (
        git reset --hard HEAD
        git clean -fd
        echo ✅ Reset complete!
    ) else (
        echo Cancelled.
    )
) else (
    echo Invalid choice.
)

echo.
pause
