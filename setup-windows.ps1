# Windows setup script for AI Fitness Analyzer

Write-Host "🚀 Setting up AI Fitness Analyzer on Windows..." -ForegroundColor Green

# Step 1: Install Python dependencies
Write-Host "📦 Installing Python dependencies..." -ForegroundColor Yellow
pip install streamlit google-generativeai opencv-python-headless pytesseract Pillow numpy pandas scikit-learn matplotlib seaborn python-dotenv

# Step 2: Install Tesseract OCR for Windows
Write-Host "🔍 Installing Tesseract OCR..." -ForegroundColor Yellow
Write-Host "Please download and install Tesseract from:" -ForegroundColor Cyan
Write-Host "https://github.com/UB-Mannheim/tesseract/wiki" -ForegroundColor Cyan
Write-Host "Choose the latest installer for Windows" -ForegroundColor Cyan

# Step 3: Install Docker Desktop
Write-Host "🐳 Docker Desktop installation..." -ForegroundColor Yellow
if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
    Write-Host "Docker not found. Please install Docker Desktop:" -ForegroundColor Red
    Write-Host "https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe" -ForegroundColor Cyan
} else {
    Write-Host "✅ Docker is already installed!" -ForegroundColor Green
}

# Step 4: Install AWS CLI
Write-Host "☁️ AWS CLI installation..." -ForegroundColor Yellow
if (-not (Get-Command aws -ErrorAction SilentlyContinue)) {
    Write-Host "AWS CLI not found. Downloading installer..." -ForegroundColor Yellow
    $awsCliUrl = "https://awscli.amazonaws.com/AWSCLIV2.msi"
    $installerPath = "$env:TEMP\AWSCLIV2.msi"
    
    Invoke-WebRequest -Uri $awsCliUrl -OutFile $installerPath
    Write-Host "Please run the installer: $installerPath" -ForegroundColor Cyan
} else {
    Write-Host "✅ AWS CLI is already installed!" -ForegroundColor Green
}

Write-Host "✅ Setup completed!" -ForegroundColor Green
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Install Docker Desktop if not done" -ForegroundColor White
Write-Host "2. Install Tesseract OCR if not done" -ForegroundColor White
Write-Host "3. Run: .\deploy-windows.ps1" -ForegroundColor White
