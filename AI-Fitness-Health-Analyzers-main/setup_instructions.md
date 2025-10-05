# AI Fitness Health Analyzer Setup Instructions

## Prerequisites
- Python 3.7 or higher
- pip (Python package installer)
- Git (optional, for cloning the repository)

## Installation Steps

### 1. Clone or Download the Repository (if applicable)
```bash
git clone [repository-url]
cd [repository-directory]
```

### 2. Install Python Dependencies
You can install all required Python packages using the provided script:

```bash
python install_dependencies.py
```

Or manually install them using pip:

```bash
pip install -r requirements.txt
```

### 3. Install Tesseract OCR
The OCR functionality requires Tesseract OCR to be installed on your system.

#### Windows
1. Download the Tesseract installer from [UB-Mannheim's GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
2. Run the installer and follow the instructions
3. Ensure the installation path is set to the default location (`C:\Program Files\Tesseract-OCR`)
4. The application will automatically detect the Tesseract installation

#### macOS
1. Install Homebrew if not already installed: [https://brew.sh/](https://brew.sh/)
2. Install Tesseract using Homebrew:
   ```bash
   brew install tesseract
   ```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
```

### 4. Set Up Environment Variables
Create a `.env` file in the root directory with your Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
```

Or set the environment variable directly:
- Windows:
  ```
  set GEMINI_API_KEY=your_api_key_here
  ```
- macOS/Linux:
  ```
  export GEMINI_API_KEY=your_api_key_here
  ```

### 5. Run the Application
```bash
streamlit run app.py
```

## Troubleshooting

### OCR Not Working
- Verify that Tesseract is properly installed
- For Windows, check if the path in `image_processor.py` matches your Tesseract installation path
- Try running a simple OCR test:
  ```python
  import pytesseract
  from PIL import Image
  print(pytesseract.image_to_string(Image.open('path_to_test_image.png')))
  ```

### API Key Issues
- Make sure your Gemini API key is valid
- Ensure the `.env` file is in the correct location or the environment variable is set properly

### Package Installation Failures
- Try installing packages one by one to identify problematic dependencies
- Update pip: `python -m pip install --upgrade pip`
- If opencv-python fails, try installing opencv-python-headless instead

## Additional Resources
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Tesseract Documentation](https://tesseract-ocr.github.io/)
- [Google Generative AI Python SDK](https://ai.google.dev/tutorials/python_quickstart)
