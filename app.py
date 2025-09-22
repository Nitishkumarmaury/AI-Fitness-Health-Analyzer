import streamlit as st
import os
from PIL import Image
import io
import matplotlib.pyplot as plt
import pandas as pd
import time
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from image_processor import extract_fitness_data_from_image
from health_analyzer import analyze_health_metrics
from recommendations import generate_recommendations

# Set page configuration
st.set_page_config(
    page_title="AI Fitness Health Analyzer",
    page_icon="💪",
    layout="wide"
)

# Get API key from Streamlit secrets or environment variables
def get_api_key():
    try:
        # Try Streamlit secrets first (for cloud deployment)
        return st.secrets["GEMINI_API_KEY"]
    except (KeyError, FileNotFoundError):
        # Fall back to environment variable (for local development)
        return os.environ.get("GEMINI_API_KEY")

# Check if API key is available
api_key = get_api_key()
if not api_key:
    st.error("🔑 GEMINI_API_KEY is not set!")
    st.markdown("""
    ### How to add your API key:
    
    **For Streamlit Cloud:**
    1. Go to your app settings
    2. Navigate to "Secrets" tab
    3. Add: `GEMINI_API_KEY = "your_api_key_here"`
    
    **For local development:**
    1. Create `.streamlit/secrets.toml` file
    2. Add: `GEMINI_API_KEY = "your_api_key_here"`
    
    **Get your API key:** [Google AI Studio](https://makersuite.google.com/app/apikey)
    """)
    st.stop()

# Set the API key in environment for the modules
os.environ["GEMINI_API_KEY"] = api_key

# App title and description
st.title("AI Fitness Health Analyzer")
st.markdown("""
This application uses AI to analyze your fitness data from images and provide personalized health insights.
Simply upload a screenshot of your fitness tracker summary, and get detailed recommendations!
""")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Upload Image", "Dashboard", "History", "About"])

# Initialize session state for storing data
if 'fitness_data' not in st.session_state:
    st.session_state.fitness_data = None
if 'analysis_results' not in st.session_state:
    st.session_state.analysis_results = None
if 'recommendations' not in st.session_state:
    st.session_state.recommendations = None
if 'history' not in st.session_state:
    st.session_state.history = []

# Upload Image Page
if page == "Upload Image":
    st.header("Upload Fitness Data Image")
    
    uploaded_file = st.file_uploader("Choose an image of your fitness tracker summary", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        try:
            # Display the uploaded image
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            
            # Process button
            if st.button("Analyze Image"):
                with st.spinner("Processing image with AI..."):
                    # Check image dimensions and size
                    if max(image.size) < 200:
                        st.error("Image is too small. Please upload a larger image with clear text.")
                        st.stop()
                        
                    # Extract data using the Gemini AI
                    fitness_data = extract_fitness_data_from_image(image)
                    
                    if fitness_data:
                        st.session_state.fitness_data = fitness_data
                        
                        # Analyze the extracted data
                        analysis_results = analyze_health_metrics(fitness_data)
                        st.session_state.analysis_results = analysis_results
                        
                        # Generate recommendations
                        recommendations = generate_recommendations(analysis_results)
                        st.session_state.recommendations = recommendations
                        
                        # Add to history
                        st.session_state.history.append({
                            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                            "fitness_data": fitness_data,
                            "analysis_results": analysis_results,
                            "recommendations": recommendations
                        })
                        
                        st.success("Analysis complete! Navigate to the Dashboard to see your results.")
                    else:
                        st.error("Could not extract fitness data from the image. Please try another image with clearer fitness metrics.")
                        st.info("Tips: Use images that clearly show numbers for steps, calories, or other fitness metrics. Make sure the text is readable and not blurry.")
        except Exception as e:
            st.error(f"Error processing image: {str(e)}")
            st.info("Please try a different image format or check if the file is corrupted.")

# Dashboard Page
elif page == "Dashboard":
    st.header("Your Health Dashboard")
    
    if st.session_state.fitness_data and st.session_state.analysis_results and st.session_state.recommendations:
        # Create columns for layout
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Your Fitness Metrics")
            metrics = st.session_state.fitness_data
            for metric, value in metrics.items():
                st.metric(label=metric.title(), value=value)
        
        with col2:
            st.subheader("Health Analysis")
            analysis = st.session_state.analysis_results
            for category, level in analysis.items():
                if category != "raw_data":
                    st.info(f"{category.replace('_', ' ').title()}: {level}")
        
        # Recommendations section
        st.subheader("Personalized Recommendations")
        recommendations = st.session_state.recommendations
        
        tab1, tab2, tab3 = st.tabs(["Activity", "Nutrition", "Wellness"])
        
        with tab1:
            st.markdown(recommendations.get("activity", "No recommendations available"))
        
        with tab2:
            st.markdown(recommendations.get("nutrition", "No recommendations available"))
        
        with tab3:
            st.markdown(recommendations.get("wellness", "No recommendations available"))
        
        # Visualization section
        st.subheader("Data Visualization")
        
        # Create a simple bar chart of the metrics
        fig, ax = plt.subplots(figsize=(10, 6))
        metrics_to_plot = {k: v for k, v in metrics.items() if isinstance(v, (int, float))}
        ax.bar(metrics_to_plot.keys(), metrics_to_plot.values())
        ax.set_title("Your Fitness Metrics")
        ax.set_ylabel("Value")
        ax.set_xlabel("Metric")
        st.pyplot(fig)
        
    else:
        st.info("No data to display. Please upload and analyze an image first.")

# History Page
elif page == "History":
    st.header("Your Analysis History")
    
    if st.session_state.history:
        for i, entry in enumerate(reversed(st.session_state.history)):
            with st.expander(f"Analysis from {entry['date']}"):
                st.subheader("Fitness Data")
                for metric, value in entry["fitness_data"].items():
                    st.text(f"{metric.title()}: {value}")
                
                st.subheader("Analysis Results")
                for category, level in entry["analysis_results"].items():
                    if category != "raw_data":
                        st.text(f"{category.replace('_', ' ').title()}: {level}")
                
                st.subheader("Recommendations")
                for category, rec in entry["recommendations"].items():
                    st.text(f"{category.title()}: {rec[:100]}...")
    else:
        st.info("No history available. Start by analyzing a fitness image.")

# About Page
elif page == "About":
    st.header("About AI Fitness Health Analyzer")
    
    st.markdown("""
    ## How It Works
    
    The AI Fitness Health Analyzer uses Google's Gemini 1.5-flash AI model to:
    
    1. **Extract Data**: Convert fitness tracker screenshots into structured data
    2. **Analyze Metrics**: Interpret your activity levels based on scientific guidelines
    3. **Generate Insights**: Provide personalized recommendations for your health journey
    
    ## Privacy Notice
    
    Your uploaded images are processed securely and not stored permanently. We value your privacy and data security.
    
    ## Contact
    
    For questions or feedback, please contact support@aifitnesshealthanalyzer.com
    """)



# Footer
st.markdown("---")
st.markdown("© 2023 AI Fitness Health Analyzer | Powered by Google Gemini AI")
