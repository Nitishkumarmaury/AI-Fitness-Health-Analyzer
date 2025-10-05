#!/usr/bin/env python3
import webbrowser
import os

def main():
    """Open Streamlit Cloud deployment page with pre-filled information"""
    
    print("🚀 Deploying to Streamlit Cloud")
    print("=" * 50)
    
    # Your repository information
    github_user = "Nitishkumarmaury"
    repo_name = "AI-Fitness-Health-Analyzers"
    main_file = "app.py"
    
    print(f"📁 Repository: {github_user}/{repo_name}")
    print(f"📄 Main file: {main_file}")
    print()
    
    print("🔑 IMPORTANT: Add this to your Streamlit Cloud secrets:")
    print("=" * 50)
    print("GEMINI_API_KEY = \"your_actual_api_key_here\"")
    print("=" * 50)
    print()
    
    print("📋 Deployment Steps:")
    print("1. ✅ Your code is already on GitHub")
    print("2. 🌐 Opening Streamlit Cloud...")
    print("3. 🔗 Connect your GitHub repository")
    print("4. 📝 Set main file: app.py")
    print("5. 🔐 Add secrets (see above)")
    print("6. 🚀 Deploy!")
    print()
    
    # Construct Streamlit Cloud URL
    streamlit_url = "https://share.streamlit.io"
    
    print(f"Opening: {streamlit_url}")
    webbrowser.open(streamlit_url)
    
    print()
    print("🎉 After deployment, your app will be available at:")
    print(f"https://{repo_name.lower()}.streamlit.app")
    
    input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
