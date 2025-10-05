#!/bin/bash

echo "Installing AI Fitness Health Analyzer dependencies..."
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install Python 3.7 or higher."
    exit 1
fi

# Install Python dependencies
echo "Installing Python packages..."
pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "Failed to install required packages. Please check your internet connection and try again."
    exit 1
fi

# Check operating system for Tesseract instructions
echo
echo "IMPORTANT: Tesseract OCR is required for full functionality."
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    echo "For macOS, install Tesseract with: brew install tesseract"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    echo "For Ubuntu/Debian, install Tesseract with: sudo apt-get install tesseract-ocr"
    echo "For other Linux distributions, please check the appropriate package manager"
else
    # Windows or other
    echo "Please download and install from: https://github.com/UB-Mannheim/tesseract/wiki"
fi
echo

# Remind about Gemini API key
echo "IMPORTANT: You need a Google Gemini API key."
echo "Create a .env file with: GEMINI_API_KEY=your_api_key_here"
echo

echo "Setup completed! Run the application with:"
echo "- GUI mode: python3 run.py"
echo "- CLI mode: python3 run.py <image_path>"

# Make the script executable
chmod +x quick_setup.sh
