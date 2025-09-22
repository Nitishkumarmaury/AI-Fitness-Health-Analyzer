#!/usr/bin/env python3
import os
import sys
import webbrowser

def create_streamlit_config():
    """Create Streamlit configuration files"""
    
    # Create .streamlit directory
    streamlit_dir = ".streamlit"
    if not os.path.exists(streamlit_dir):
        os.makedirs(streamlit_dir)
    
    # Create config.toml
    config_content = """
[theme]
primaryColor = "#1976d2"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f0f0"
textColor = "#262730"

[server]
headless = true
port = 8501
enableCORS = false
enableXsrfProtection = false
"""
    
    with open(os.path.join(streamlit_dir, "config.toml"), "w") as f:
        f.write(config_content)
    
    # Create secrets.toml template
    secrets_content = """
# Add your secrets here
# GEMINI_API_KEY = "your_api_key_here"
"""
    
    with open(os.path.join(streamlit_dir, "secrets.toml"), "w") as f:
        f.write(secrets_content)
    
    print("✅ Streamlit configuration files created")

def create_requirements_streamlit():
    """Create requirements.txt for Streamlit deployment"""
    streamlit_requirements = """
streamlit==1.28.0
Pillow==10.0.0
matplotlib==3.7.2
pandas==2.0.3
google-generativeai==0.3.1
python-dotenv==1.0.0
opencv-python-headless==4.8.0.74
pytesseract==0.3.10
numpy==1.24.3
"""
    
    with open("requirements_streamlit.txt", "w") as f:
        f.write(streamlit_requirements)
    
    print("✅ Streamlit requirements.txt created")

def main():
    """Main function for Streamlit deployment"""
    print("=" * 60)
    print("  AI Fitness Health Analyzer - Streamlit Cloud Deployment")
    print("=" * 60)
    print()
    
    # Create Streamlit config
    create_streamlit_config()
    create_requirements_streamlit()
    
    print("📋 Deployment Instructions:")
    print("1. Push your code to GitHub (use push_to_github.bat)")
    print("2. Go to https://share.streamlit.io")
    print("3. Connect your GitHub account")
    print("4. Select your repository")
    print("5. Set main file path: app.py")
    print("6. Add your GEMINI_API_KEY in the secrets section")
    print()
    print("🔑 In Streamlit secrets, add:")
    print('GEMINI_API_KEY = "your_actual_api_key_here"')
    print()
    
    if input("Open Streamlit Cloud in browser? (y/n): ").lower() == 'y':
        webbrowser.open("https://share.streamlit.io")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
