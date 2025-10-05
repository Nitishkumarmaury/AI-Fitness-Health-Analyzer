#!/usr/bin/env python3
import os
import sys
import subprocess
import webbrowser
import time
import platform
from pathlib import Path

def check_environment():
    """Check if all necessary components are installed"""
    print("Checking environment...")
    
    # Check Python
    if sys.version_info < (3, 7):
        print("Error: Python 3.7 or higher is required.")
        return False
    
    # Check for .env file
    if not os.path.exists('.env'):
        print("Warning: .env file not found.")
        print("Creating a template .env file. Please edit it with your actual API key.")
        with open('.env', 'w') as f:
            f.write("GEMINI_API_KEY=your_api_key_here\n")
    
    # Check if frontend build exists
    frontend_build = Path('frontend/build')
    if not frontend_build.exists():
        # Check Node.js/npm
        try:
            subprocess.run(["node", "--version"], check=True, capture_output=True)
            subprocess.run(["npm", "--version"], check=True, capture_output=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("Error: Node.js or npm not found.")
            print("Please install Node.js and npm to build the frontend.")
            return False
    
    return True

def build_frontend():
    """Build the React frontend"""
    print("Building the React frontend...")
    
    frontend_dir = Path('frontend')
    if not frontend_dir.exists():
        print(f"Error: Frontend directory not found at {frontend_dir}")
        return False
    
    # Install dependencies if node_modules doesn't exist
    if not (frontend_dir / 'node_modules').exists():
        print("Installing frontend dependencies...")
        try:
            subprocess.run(["npm", "install"], cwd=frontend_dir, check=True)
        except subprocess.CalledProcessError:
            print("Failed to install frontend dependencies.")
            return False
    
    # Build the frontend
    try:
        subprocess.run(["npm", "run", "build"], cwd=frontend_dir, check=True)
        return True
    except subprocess.CalledProcessError:
        print("Failed to build the frontend.")
        return False

def open_browser():
    """Open browser after a short delay"""
    print("Opening browser...")
    time.sleep(2)  # Wait for the server to start
    webbrowser.open("http://localhost:5000")

def main():
    """Main function to run the application"""
    print("=" * 60)
    print("  AI Fitness Health Analyzer - Quick Start")
    print("=" * 60)
    print()
    
    # Check environment
    if not check_environment():
        input("Press Enter to exit...")
        return 1
    
    # Check if frontend is built
    if not os.path.exists('frontend/build'):
        print("Frontend build not found.")
        choice = input("Do you want to build the frontend now? (y/n): ")
        if choice.lower() == 'y':
            if not build_frontend():
                input("Press Enter to exit...")
                return 1
        else:
            print("Cannot run application without frontend build.")
            input("Press Enter to exit...")
            return 1
    
    # Open browser in a new thread
    if platform.system() != "Linux":  # Skip on Linux which might be headless
        try:
            from threading import Thread
            browser_thread = Thread(target=open_browser)
            browser_thread.daemon = True
            browser_thread.start()
        except Exception as e:
            print(f"Note: Could not open browser automatically: {e}")
    
    # Start the server
    print("\nStarting the application...")
    print("Access the app at: http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    print()
    
    try:
        subprocess.run([sys.executable, "run.py"])
    except KeyboardInterrupt:
        print("\nShutting down server...")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
