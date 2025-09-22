#!/usr/bin/env python3
import os
import sys
import subprocess
import webbrowser
import json

def check_railway_cli():
    """Check if Railway CLI is installed"""
    try:
        result = subprocess.run(["railway", "--version"], capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False

def install_railway_cli():
    """Install Railway CLI"""
    print("Railway CLI not found. Please install it manually:")
    print("npm install -g @railway/cli")
    print("or")
    print("curl -fsSL https://railway.app/install.sh | sh")
    return False

def deploy_to_railway():
    """Deploy the application to Railway"""
    print("🚂 Deploying to Railway...")
    
    # Check if Railway CLI is installed
    if not check_railway_cli():
        if not install_railway_cli():
            return False
    
    try:
        # Login to Railway
        print("Logging in to Railway...")
        subprocess.run(["railway", "login"], check=True)
        
        # Initialize project
        print("Initializing Railway project...")
        subprocess.run(["railway", "init"], check=True)
        
        # Add environment variables
        api_key = input("Enter your GEMINI_API_KEY: ")
        if api_key:
            subprocess.run(["railway", "variables", "set", f"GEMINI_API_KEY={api_key}"], check=True)
        
        # Deploy
        print("Deploying application...")
        result = subprocess.run(["railway", "up"], check=True, capture_output=True, text=True)
        
        # Get the deployment URL
        url_result = subprocess.run(["railway", "domain"], capture_output=True, text=True)
        if url_result.returncode == 0:
            print(f"✅ Deployment successful!")
            print(f"🌐 Your app is live at: {url_result.stdout.strip()}")
            
            # Open in browser
            if input("Open in browser? (y/n): ").lower() == 'y':
                webbrowser.open(url_result.stdout.strip())
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Deployment failed: {e}")
        return False

def main():
    """Main deployment function"""
    print("=" * 60)
    print("  AI Fitness Health Analyzer - Railway Deployment")
    print("=" * 60)
    print()
    
    # Check if we're in a git repository
    if not os.path.exists('.git'):
        print("❌ Not a git repository. Please run 'git init' first.")
        return 1
    
    # Check if changes are committed
    result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    if result.stdout.strip():
        print("⚠️  You have uncommitted changes. Please commit them first:")
        print("git add .")
        print("git commit -m 'Deploy to Railway'")
        return 1
    
    # Deploy
    if deploy_to_railway():
        print("🎉 Deployment completed successfully!")
        return 0
    else:
        print("❌ Deployment failed. Please check the errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
