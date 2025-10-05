@echo off
echo ===== AI Fitness Health Analyzer - GitHub Push =====
echo.

REM Check if git is installed
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Git is not installed or not in your PATH.
    echo Please install Git from https://git-scm.com/
    pause
    exit /b 1
)

REM Check if we're in the right directory
if not exist "requirements.txt" (
    echo Error: Not in the project root directory.
    echo Please run this script from the project root.
    pause
    exit /b 1
)

REM Initialize git repository if not already done
if not exist .git (
    echo Initializing Git repository...
    git init
    echo.
)

REM Create or update .gitignore
echo Creating .gitignore file...
(
echo # Python
echo __pycache__/
echo *.py[cod]
echo *$py.class
echo *.so
echo .Python
echo build/
echo develop-eggs/
echo dist/
echo downloads/
echo eggs/
echo .eggs/
echo lib/
echo lib64/
echo parts/
echo sdist/
echo var/
echo wheels/
echo *.egg-info/
echo .installed.cfg
echo *.egg
echo MANIFEST
echo.
echo # Virtual environments
echo venv/
echo env/
echo ENV/
echo env.bak/
echo venv.bak/
echo.
echo # Environment variables
echo .env
echo .env.local
echo .env.development.local
echo .env.test.local
echo .env.production.local
echo.
echo # Database
echo *.db
echo *.sqlite
echo *.sqlite3
echo fitness_analyzer.db
echo.
echo # Logs
echo *.log
echo app.log
echo.
echo # Node modules
echo node_modules/
echo npm-debug.log*
echo yarn-debug.log*
echo yarn-error.log*
echo.
echo # React build
echo /frontend/build/
echo /frontend/.pnp
echo /frontend/.pnp.js
echo.
echo # Testing
echo /frontend/coverage/
echo.
echo # Production
echo /build
echo.
echo # Misc
echo .DS_Store
echo .DS_Store?
echo ._*
echo .Spotlight-V100
echo .Trashes
echo ehthumbs.db
echo Thumbs.db
echo.
echo # Temporary uploads
echo temp_uploads/
echo.
echo # IDE
echo .vscode/
echo .idea/
echo *.swp
echo *.swo
echo *~
) > .gitignore

REM Add all files to staging
echo Adding files to Git...
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
    echo.
    echo Please enter your GitHub repository URL:
    echo Example: https://github.com/yourusername/your-repo-name.git
    set /p repo_url="Repository URL: "
    
    if "%repo_url%"=="" (
        echo Error: No repository URL provided.
        pause
        exit /b 1
    )
    
    echo Adding remote repository...
    git remote add origin %repo_url%
    echo.
) else (
    echo Remote origin already exists.
)

REM Set main branch and push
echo Pushing to GitHub...
git branch -M main
git push -u origin main

if %errorlevel% equ 0 (
    echo.
    echo ✅ Successfully pushed to GitHub!
    echo.
    echo Your project is now available on GitHub.
    echo You can view it in your browser or clone it to other machines.
    echo.
    echo Next steps:
    echo 1. Go to your GitHub repository
    echo 2. Add a description and topics
    echo 3. Consider adding a license
    echo 4. Share your project!
    echo.
) else (
    echo.
    echo ❌ Failed to push to GitHub.
    echo.
    echo Possible issues:
    echo 1. Check your internet connection
    echo 2. Verify your GitHub credentials
    echo 3. Make sure the repository exists on GitHub
    echo 4. Check if you have push permissions
    echo.
    echo Try running: git push -u origin main
    echo.
)

pause
