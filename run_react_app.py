#!/usr/bin/env python3
import os
import sys
import subprocess
import webbrowser
import time
import threading
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def check_env():
    """Check if r    python setup_react.pyequired environment variables are set"""
    if not os.environ.get("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY is not set.")
        print("Please add it to your .env file or set it as an environment variable.")
        return False
    return True

def check_frontend_build():
    """Check if frontend build exists"""
    build_dir = os.path.join("frontend", "build")
    return os.path.exists(build_dir) and os.path.isdir(build_dir)

def build_frontend():
    """Build the React frontend"""
    print("Building React frontend...")
    frontend_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "frontend")
    
    if not os.path.exists(os.path.join(frontend_dir, "node_modules")):
        print("Installing frontend dependencies...")
        try:
            subprocess.run(["npm", "install"], cwd=frontend_dir, check=True)
        except subprocess.CalledProcessError:
            print("Error installing frontend dependencies.")
            return False
        except FileNotFoundError:
            print("Error: npm not found. Please install Node.js and npm.")
            return False
    
    try:
        subprocess.run(["npm", "run", "build"], cwd=frontend_dir, check=True)
        return True
    except subprocess.CalledProcessError:
        print("Error building frontend.")
        return False

def open_browser():
    """Open the browser after a delay"""
    time.sleep(2)  # Wait for the server to start
    webbrowser.open("http://localhost:5000")

def run_flask_server():
    """Run the Flask server"""
    from run import app
    app.run(host="0.0.0.0", port=5000)

def main():
    """Main function to run the application"""
    if not check_env():
        return 1
    
    if not check_frontend_build():
        print("Frontend build not found.")
        build = input("Would you like to build the frontend now? (y/n): ")
        if build.lower() == 'y':
            if not build_frontend():
                return 1
        else:
            print("Cannot run application without frontend build.")
            return 1
    
    print("Starting AI Fitness Health Analyzer...")
    print("The application will open in your browser shortly...")
    
    # Open browser in a separate thread
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    # Run Flask server
    run_flask_server()
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
