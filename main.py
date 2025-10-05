#!/usr/bin/env python3
"""
Main entry point for the AI Fitness Health Analyzer application.
This file provides a unified interface to run different versions of the app.
"""

import sys
import os

def main():
    """Main entry point with options for different interfaces"""
    print("AI Fitness Health Analyzer")
    print("=" * 40)
    print("Choose an interface:")
    print("1. Streamlit Web App (Recommended)")
    print("2. React Web App")
    print("3. Command Line Interface")
    print("4. Desktop GUI")
    
    choice = input("\nEnter your choice (1-4): ").strip()
    
    if choice == "1":
        os.system("python run_streamlit.py")
    elif choice == "2":
        os.system("python run_react_app.py")
    elif choice == "3":
        if len(sys.argv) > 1:
            os.system(f"python cli.py {' '.join(sys.argv[1:])}")
        else:
            print("Please provide an image path for CLI mode")
            print("Usage: python main.py <image_path>")
    elif choice == "4":
        os.system("python gui.py")
    else:
        print("Invalid choice. Please run the script again.")

if __name__ == "__main__":
    main()
