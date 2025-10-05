# Running the AI Fitness Health Analyzer

This document provides instructions for running the AI Fitness Health Analyzer project using different interfaces.

## Prerequisites

Before running the application, make sure you have:

1. Installed all required dependencies
   ```bash
   pip install -r requirements.txt
   ```

2. Set up your Google Gemini API key in a `.env` file
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

3. Installed Tesseract OCR for image text extraction capabilities

## Option 1: Streamlit Web Interface

The Streamlit interface provides a user-friendly web application that you can access through your browser.

```bash
# Run the Streamlit application
streamlit run app.py
```

This will start a local web server and open the application in your default web browser. If it doesn't open automatically, you can access it at http://localhost:8501.

## Option 2: Python GUI Application

For a native desktop experience without requiring a web browser:

```bash
# Run the GUI application
python run.py
```

This will launch a desktop application with similar functionality to the Streamlit version.

## Option 3: Command Line Interface

For batch processing or server environments:

```bash
# Process a single image via command line
python run.py /path/to/your/fitness_image.jpg

# Optional: Save the results to a JSON file
python run.py /path/to/your/fitness_image.jpg --save results.json
```

## Troubleshooting

If you encounter any issues:

1. **API Key Problems**: Ensure your Gemini API key is correctly set in the `.env` file
2. **Image Processing Errors**: Try using clearer images with visible fitness metrics
3. **OCR Issues**: Verify Tesseract OCR is properly installed on your system
4. **Missing Dependencies**: Run `pip install -r requirements.txt` to ensure all packages are installed

## Sample Test Images

You can test the application with sample fitness tracker screenshots located in the `sample_images` directory (if available).
