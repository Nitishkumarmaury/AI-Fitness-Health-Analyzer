#!/usr/bin/env python3
import os
import sys
import subprocess
import webbrowser
import time
from pathlib import Path

def check_streamlit():
    """Check if streamlit is installed"""
    try:
        import streamlit
        return True
    except ImportError:
        return False

def install_streamlit():
    """Install streamlit if not present"""
    print("Installing Streamlit...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "streamlit"], check=True)
        return True
    except subprocess.CalledProcessError:
        print("Failed to install Streamlit.")
        return False

def main():
    """Run the Streamlit version of the application"""
    print("=" * 60)
    print("  AI Fitness Health Analyzer - Streamlit Version")
    print("=" * 60)
    print()
    
    # Check for .env file
    if not os.path.exists('.env'):
        print("Warning: .env file not found.")
        print("Creating a template .env file. Please edit it with your actual API key.")
        with open('.env', 'w') as f:
            f.write("GEMINI_API_KEY=your_api_key_here\n")
        print("Please edit the .env file with your API key before continuing.")
        input("Press Enter when you've added your API key...")
    
    # Check if streamlit is installed
    if not check_streamlit():
        print("Streamlit not found. Installing...")
        if not install_streamlit():
            input("Press Enter to exit...")
            return 1
    
    # Check if app.py exists
    if not os.path.exists('app.py'):
        print("Error: app.py not found. Make sure you're in the correct directory.")
        input("Press Enter to exit...")
        return 1
    
    print("Starting Streamlit application...")
    print("The application will open in your browser shortly...")
    print("Press Ctrl+C to stop the server")
    print()
    
    try:
        # Run streamlit
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])
    except KeyboardInterrupt:
        print("\nShutting down server...")
    except Exception as e:
        print(f"Error running application: {e}")
        input("Press Enter to exit...")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
