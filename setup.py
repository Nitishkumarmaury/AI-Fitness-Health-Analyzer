import os
import subprocess
import sys
import platform

def main():
    """Set up the AI Fitness Health Analyzer project"""
    
    print("Setting up AI Fitness Health Analyzer...")
    
    # Install Python dependencies
    print("\nInstalling Python dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError:
        print("Failed to install Python dependencies")
        return 1
    
    # Set up frontend
    frontend_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "frontend")
    
    if not os.path.exists(frontend_dir):
        print("Error: Frontend directory not found")
        return 1
    
    print("\nInstalling frontend dependencies...")
    try:
        # Check if npm is available
        npm_cmd = "npm"
        try:
            subprocess.run([npm_cmd, "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("Error: npm not found. Please install Node.js and npm.")
            return 1
            
        # Install frontend dependencies
        subprocess.check_call([npm_cmd, "install"], cwd=frontend_dir)
        
        # Build frontend
        print("\nBuilding frontend...")
        subprocess.check_call([npm_cmd, "run", "build"], cwd=frontend_dir)
        
    except subprocess.CalledProcessError as e:
        print(f"Failed to set up frontend: {e}")
        return 1
    
    print("\nSetup completed successfully!")
    print("\nYou can now run the application with: python run.py")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
