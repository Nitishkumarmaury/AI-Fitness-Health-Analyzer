@echo off
echo ===== AI Fitness Health Analyzer - Updated Re-Push to GitHub =====
echo.

REM Adding all changes
git add .

REM Create commit with latest changes
git commit -m "🚀 Fix Streamlit Cloud deployment - Updated secrets handling and main app"

REM Force push the updates
git push --force-with-lease origin main

if %errorlevel% equ 0 (
    echo.
    echo ✅ Successfully updated GitHub repository!
    echo.
    echo 🌐 Repository: https://github.com/Nitishkumarmaury/AI-Fitness-Health-Analyzers
    echo.
    echo 📋 Next Steps for Streamlit Cloud:
    echo 1. Go to your app dashboard: https://share.streamlit.io
    echo 2. Your app should restart automatically with the updates
    echo 3. Add your API key in app settings → Secrets:
    echo    GEMINI_API_KEY = "your_actual_api_key_here"
    echo.
    echo ⚡ Your app URL: https://ai-fitness-health-analyzers.streamlit.app
    echo.
) else (
    echo ❌ Failed to push updates
)

pause
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
