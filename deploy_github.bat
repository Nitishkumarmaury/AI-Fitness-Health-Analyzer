@echo off
echo ===== AI Fitness Health Analyzer - GitHub Deployment =====
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
    git branch -M main
    echo.
)

REM Create or update .gitignore
echo Creating comprehensive .gitignore file...
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
echo.
echo # OS generated files
echo Desktop.ini
echo $RECYCLE.BIN/
echo.
echo # Deployment
echo .vercel
echo .netlify
) > .gitignore

REM Create README with deployment info
echo Creating updated README.md...
(
echo # AI Fitness Health Analyzer
echo.
echo ^> Transform your fitness data into personalized health insights using AI
echo.
echo ## 🚀 Live Demo
echo.
echo - **Streamlit Cloud**: [View Live Demo]^(https://ai-fitness-analyzer.streamlit.app^)
echo - **Railway**: [View Live Demo]^(https://ai-fitness-analyzer.up.railway.app^)
echo.
echo ## ✨ Features
echo.
echo - 📸 Upload fitness tracker screenshots
echo - 🤖 AI-powered data extraction using Google Gemini
echo - 📊 Personalized health insights and recommendations
echo - 📈 Progress tracking and history
echo - 📱 Responsive design for all devices
echo.
echo ## 🎯 Quick Start
echo.
echo ### Option 1: Streamlit Version ^(Recommended^)
echo ```bash
echo python run_streamlit.py
echo ```
echo.
echo ### Option 2: Full React App
echo ```bash
echo run.bat    # Windows
echo ./run.sh   # Linux/Mac
echo ```
echo.
echo ## 🛠️ Technologies
echo.
echo - **Frontend**: React, Material-UI, Streamlit
echo - **Backend**: Flask, Python
echo - **AI**: Google Gemini 1.5-flash
echo - **Database**: SQLite
echo - **Deployment**: Railway, Streamlit Cloud, Vercel
echo.
echo ## 📋 Requirements
echo.
echo - Python 3.7+
echo - Google Gemini API Key
echo - Node.js ^(for React version^)
echo - Tesseract OCR
echo.
echo ## ⚙️ Setup
echo.
echo 1. Clone the repository
echo 2. Create `.env` file with your `GEMINI_API_KEY`
echo 3. Install dependencies: `pip install -r requirements.txt`
echo 4. Run the application
echo.
echo ## 🚀 Deploy
echo.
echo ### Streamlit Cloud
echo 1. Push to GitHub
echo 2. Connect at [share.streamlit.io]^(https://share.streamlit.io^)
echo 3. Add secrets: `GEMINI_API_KEY = "your_key"`
echo.
echo ### Railway
echo 1. Connect GitHub repo at [railway.app]^(https://railway.app^)
echo 2. Add environment variable: `GEMINI_API_KEY`
echo.
echo ## 📱 Screenshots
echo.
echo ^[Add screenshots of your application here^]
echo.
echo ## 🤝 Contributing
echo.
echo Contributions are welcome! Please feel free to submit a Pull Request.
echo.
echo ## 📄 License
echo.
echo This project is licensed under the MIT License.
) > README.md

REM Add all files to staging
echo Adding files to Git...
git add .

REM Check if there are changes to commit
git diff --cached --quiet
if %errorlevel% neq 0 (
    echo Creating commit...
    git commit -m "🚀 Deploy: AI Fitness Health Analyzer with React and Streamlit versions

    Features:
    - AI-powered fitness data extraction
    - Personalized health recommendations  
    - React frontend with Material-UI
    - Streamlit alternative interface
    - SQLite database for history
    - Ready for cloud deployment"
    echo.
) else (
    echo No changes to commit. Repository is up to date.
)

REM Check if remote already exists
git remote get-url origin >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo Setting up GitHub remote...
    git remote add origin https://github.com/Nitishkumarmaury/AI-Fitness-Health-Analyzers.git
    echo.
) else (
    echo Remote origin already exists.
)

REM Push to GitHub
echo Pushing to GitHub...
git push -u origin main

if %errorlevel% equ 0 (
    echo.
    echo ✅ Successfully deployed to GitHub!
    echo.
    echo 🌐 Repository: https://github.com/Nitishkumarmaury/AI-Fitness-Health-Analyzers
    echo.
    echo 🚀 Next steps - Deploy for FREE:
    echo.
    echo 1. Streamlit Cloud ^(Easiest^):
    echo    - Go to https://share.streamlit.io
    echo    - Connect your GitHub repo
    echo    - Set main file: app.py
    echo    - Add secret: GEMINI_API_KEY
    echo.
    echo 2. Railway ^(Full Stack^):
    echo    - Go to https://railway.app
    echo    - Connect GitHub repo
    echo    - Add env var: GEMINI_API_KEY
    echo.
    echo 3. Vercel ^(Serverless^):
    echo    - Go to https://vercel.com
    echo    - Import project from GitHub
    echo    - Add env var: GEMINI_API_KEY
    echo.
) else (
    echo.
    echo ❌ Failed to push to GitHub.
    echo.
    echo Possible solutions:
    echo 1. Check your internet connection
    echo 2. Verify your GitHub credentials
    echo 3. Make sure the repository exists
    echo 4. Try: git push --set-upstream origin main
    echo.
)

echo.
echo Press any key to open GitHub repository...
pause >nul
start https://github.com/Nitishkumarmaury/AI-Fitness-Health-Analyzers

pause
