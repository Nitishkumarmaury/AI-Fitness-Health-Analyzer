#!/bin/bash

echo "Setting up AI Fitness Health Analyzer..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed. Please install Python 3.7 or higher."
    exit 1
fi

# Check if Node.js and npm are installed
if ! command -v node &> /dev/null || ! command -v npm &> /dev/null; then
    echo "Error: Node.js or npm is not installed. Please install both."
    exit 1
fi

# Create virtual environment
echo "Creating Python virtual environment..."
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Check for .env file and create if needed
if [ ! -f .env ]; then
    echo "Creating .env file template..."
    echo "GEMINI_API_KEY=your_api_key_here" > .env
    echo "Please edit the .env file with your actual API key."
fi

# Initialize the database
echo "Initializing database..."
python -c "from run import init_db; init_db()"

# Set up the frontend
echo "Setting up React frontend..."
cd frontend

# Install dependencies
echo "Installing npm dependencies..."
npm install

# Build the frontend
echo "Building the frontend..."
npm run build

cd ..

echo "Setup complete!"
echo "To run the application:"
echo "1. Activate the virtual environment: source venv/bin/activate"
echo "2. Run the server: python run.py"
echo "3. Access the app at: http://localhost:5000"
echo "Building frontend..."
npm run build
if [ $? -ne 0 ]; then
    echo "Failed to build frontend."
    exit 1
fi

cd ..

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

echo "Setup completed! Start the application with: python run.py"
