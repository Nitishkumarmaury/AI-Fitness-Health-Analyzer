#!/usr/bin/env python3
import os
import sys
import subprocess
import webbrowser
import time
import threading
from dotenv import load_dotenv

def check_environment():
    """Check if all necessary components are installed"""
    # Check Python
    print("Checking Python environment...")
    if not os.environ.get("GEMINI_API_KEY"):
        print("Warning: GEMINI_API_KEY is not set in environment variables.")
        print("Please set it in your .env file or as an environment variable.")
        return False
        
    # Check Node.js/npm if we need to build the frontend
    if not os.path.exists(os.path.join("frontend", "build")):
        print("Checking Node.js environment...")
        try:
            subprocess.run(["node", "--version"], check=True, capture_output=True)
            subprocess.run(["npm", "--version"], check=True, capture_output=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("Error: Node.js or npm not found.")
            print("Please install Node.js and npm to build the frontend.")
            return False
    
    return True

def build_frontend():
    """Build the React frontend application"""
    print("Building the React frontend...")
    frontend_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "frontend")
    
    # Check if node_modules exists
    if not os.path.exists(os.path.join(frontend_dir, "node_modules")):
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
    time.sleep(2)  # Wait for the server to start
    webbrowser.open("http://localhost:5000")

def main():
    """Main function to run the application"""
    print("Starting AI Fitness Health Analyzer...")
    
    # Load environment variables
    load_dotenv()
    
    # Check environment
    if not check_environment():
        return 1
    
    # Check if frontend is built
    build_dir = os.path.join("frontend", "build")
    if not os.path.exists(build_dir):
        print("Frontend build not found.")
        choice = input("Do you want to build the frontend now? (y/n): ")
        if choice.lower() == 'y':
            if not build_frontend():
                return 1
        else:
            print("Cannot run application without frontend build.")
            return 1
    
    # Open browser in a new thread
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    # Run the Flask application
    print("Starting Flask server...")
    print("The application will open in your browser shortly...")
    
    # Import and run the Flask app
    from run import app
    app.run(host="0.0.0.0", port=5000)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
