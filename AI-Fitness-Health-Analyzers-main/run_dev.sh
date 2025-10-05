#!/bin/bash

# Colors for terminal output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}Starting AI Fitness Health Analyzer Development Environment${NC}"
echo

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python 3 is not installed or not in your PATH.${NC}"
    exit 1
fi

# Check if Node.js is available
if ! command -v node &> /dev/null; then
    echo -e "${RED}Error: Node.js is not installed or not in your PATH.${NC}"
    exit 1
fi

# Check if npm is available
if ! command -v npm &> /dev/null; then
    echo -e "${RED}Error: npm is not installed or not in your PATH.${NC}"
    exit 1
fi

# Check if .env file exists
if [ ! -f .env ]; then
    echo -e "${YELLOW}Warning: .env file not found. Creating template...${NC}"
    echo "GEMINI_API_KEY=your_api_key_here" > .env
    echo -e "${YELLOW}Please edit .env file with your actual API key!${NC}"
    echo
fi

# Start frontend and backend in separate terminals
echo -e "${GREEN}Starting frontend development server...${NC}"
cd frontend && npm start &
FRONTEND_PID=$!

echo -e "${GREEN}Starting backend API server...${NC}"
cd ..
python3 run.py &
BACKEND_PID=$!

# Function to handle script termination
function cleanup {
    echo -e "${YELLOW}Shutting down servers...${NC}"
    kill $FRONTEND_PID
    kill $BACKEND_PID
    echo -e "${GREEN}Done!${NC}"
    exit 0
}

# Set up trap to catch SIGINT (ctrl+c)
trap cleanup SIGINT

# Wait for user to press Ctrl+C
echo -e "${GREEN}Development environment is running!${NC}"
echo -e "${YELLOW}Frontend:${NC} http://localhost:3000"
echo -e "${YELLOW}Backend API:${NC} http://localhost:5000"
echo -e "${YELLOW}Press Ctrl+C to stop all servers${NC}"

# Keep script running
wait
