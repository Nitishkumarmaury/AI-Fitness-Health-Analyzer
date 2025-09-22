#!/usr/bin/env python3
import os
import sys
import subprocess
import streamlit as st

def main():
    """Run the Streamlit version of the application"""
    
    # For Streamlit Cloud, we don't need to check for .env files
    # since secrets are handled through Streamlit's secrets management
    
    # Check if running on Streamlit Cloud
    if "STREAMLIT_SHARING" in os.environ or "streamlit.app" in os.environ.get("HOSTNAME", ""):
        print("Running on Streamlit Cloud - using Streamlit secrets")
    else:
        # Local development - check for .env file
        if not os.path.exists('.env'):
            print("Warning: .env file not found.")
            print("For local development, create a .env file with:")
            print("GEMINI_API_KEY=your_api_key_here")
            print()
            print("For Streamlit Cloud, add your API key in the app secrets.")
    
    # Check if streamlit is installed
    try:
        import streamlit
        print("Streamlit is available")
    except ImportError:
        print("Installing Streamlit...")
        subprocess.run([sys.executable, "-m", "pip", "install", "streamlit"], check=True)
    
    # Run the app directly (for Streamlit Cloud this will execute app.py)
    if __name__ == "__main__":
        # This will be called by Streamlit Cloud
        exec(open('app.py').read())

if __name__ == "__main__":
    main()
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
