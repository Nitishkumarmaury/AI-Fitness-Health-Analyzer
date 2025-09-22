#!/usr/bin/env python3
import sys
import platform
import subprocess

def check_python_version():
    """Check and display Python version information"""
    print("=" * 50)
    print("  Python Version Information")
    print("=" * 50)
    
    # Current Python version
    print(f"Python Version: {sys.version}")
    print(f"Python Version Info: {sys.version_info}")
    print(f"Python Executable: {sys.executable}")
    print(f"Platform: {platform.platform()}")
    print()
    
    # Check if version meets requirements
    if sys.version_info >= (3, 7):
        print("✅ Python version is compatible with this project!")
    else:
        print("❌ Python version is too old. Please upgrade to Python 3.7 or higher.")
    
    print()
    print("Project Requirements:")
    print("- Minimum: Python 3.7")
    print("- Recommended: Python 3.8+")
    print("- Deployment: Python 3.11.0")
    
    # Check pip version
    try:
        import pip
        print(f"\nPip Version: {pip.__version__}")
    except ImportError:
        print("\nPip: Not available")

if __name__ == "__main__":
    check_python_version()
