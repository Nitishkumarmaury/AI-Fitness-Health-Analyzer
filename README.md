# AI Fitness Health Analyzer

Advanced AI-powered fitness data analysis and health recommendations system.

## Features

- 📊 AI Vision-based fitness image analysis
- 🤖 Advanced health insights and recommendations
- 💡 Personalized meal and workout plans
- 📈 Progress tracking and visualization
- 🏥 Comprehensive health assessments

## Live Demo

🌐 **[Try the Live App](https://your-app-name.streamlit.app)**

## Local Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd ai-fitness-analyzer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up API key:
```bash
# Create .streamlit/secrets.toml and add your Gemini API key
echo 'GEMINI_API_KEY = "your-api-key-here"' > .streamlit/secrets.toml
```

4. Run the application:
```bash
streamlit run main.py
```

## Usage

1. Upload a fitness summary image
2. Click "Analyze Fitness Data"
3. View comprehensive health analysis
4. Get AI-powered recommendations

## Tech Stack

- **Frontend**: Streamlit
- **AI Vision**: Google Gemini 1.5 Flash
- **Image Processing**: OpenCV, Tesseract OCR
- **Data Analysis**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn

## Deployment

This app is deployed on Streamlit Cloud with automatic updates from GitHub.
