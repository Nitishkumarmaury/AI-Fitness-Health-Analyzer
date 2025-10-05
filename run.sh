#!/bin/bash

echo "Starting AI Fitness Health Analyzer..."
echo

# Check Python installation
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 not found. Please install Python 3.7 or higher."
    exit 1
fi

# Check for .env file
if [ ! -f .env ]; then
    echo "Warning: .env file not found."
    echo "Creating a template .env file. Please edit it with your actual API key."
    echo "GEMINI_API_KEY=your_api_key_here" > .env
    echo
fi

# Check if frontend build exists
if [ ! -d frontend/build ]; then
    echo "Frontend build not found. Building now..."
    
    # Check if Node.js is installed
    if ! command -v node &> /dev/null; then
        echo "Error: Node.js not found. Please install Node.js and npm."
        exit 1
    fi
    
    # Build frontend
    cd frontend
    
    echo "Installing dependencies..."
    npm install
    
    echo "Building frontend..."
    npm run build
    
    if [ $? -ne 0 ]; then
        echo "Error building frontend. Please check errors above."
        exit 1
    fi
    
    cd ..
fi

# Start the server
echo "Starting server..."
python3 run.py

# Make this script executable
chmod +x run.sh
