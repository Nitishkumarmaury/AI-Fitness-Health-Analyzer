import subprocess
import sys
import os
import platform

def install_dependencies():
    """Install all required dependencies for the AI Fitness Health Analyzer"""
    
    print("Installing required Python packages...")
    
    # List of required packages
    requirements = [
        "Pillow==10.0.0",
        "matplotlib==3.7.2",
        "pandas==2.0.3",
        "google-generativeai==0.3.1",
        "python-dotenv==1.0.0",
        "opencv-python==4.8.0.74",
        "pytesseract==0.3.10",
        "numpy==1.24.3"
    ]
    
    # Optional development packages
    dev_requirements = [
        "pytest==7.4.0",
        "black==23.7.0",
        "flake8==6.1.0"
    ]
    
    # Install required packages
    for package in requirements:
        print(f"Installing {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
    # Ask if user wants to install development packages
    install_dev = input("\nDo you want to install development packages (pytest, black, flake8)? (y/n): ")
    if install_dev.lower() == 'y':
        for package in dev_requirements:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
    print("\nAll Python packages installed successfully!")
    
    # Provide instructions for Tesseract OCR installation
    print("\n--- Tesseract OCR Installation Instructions ---")
    system = platform.system()
    if system == "Windows":
        print("For Windows:")
        print("1. Download Tesseract installer from: https://github.com/UB-Mannheim/tesseract/wiki")
        print("2. Run the installer and follow the instructions")
        print("3. Ensure the install location is the default (C:\\Program Files\\Tesseract-OCR) or update the path in image_processor.py")
    elif system == "Darwin":  # macOS
        print("For macOS:")
        print("1. Install Homebrew if not already installed: https://brew.sh/")
        print("2. Run: brew install tesseract")
    elif system == "Linux":
        print("For Linux (Ubuntu/Debian):")
        print("1. Run: sudo apt-get install tesseract-ocr")
        print("For other Linux distributions, please check the appropriate package manager")
    
    print("\nSetup completed!")
    print("\nRun the application with:")
    print("- GUI mode: python run.py")
    print("- CLI mode: python run.py <image_path>")

if __name__ == "__main__":
    install_dependencies()
