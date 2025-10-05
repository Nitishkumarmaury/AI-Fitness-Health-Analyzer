import streamlit as st
import os
from PIL import Image
import io
import matplotlib.pyplot as plt
import pandas as pd
import time
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file (for local development)
load_dotenv()

# Import custom modules with error handling
try:
    from image_processor import extract_fitness_data_from_image
    from health_analyzer import analyze_health_metrics
    from recommendations import generate_recommendations
except ImportError as e:
    st.error(f"Error importing modules: {e}")
    st.stop()

# Set page configuration
st.set_page_config(
    page_title="AI Fitness Health Analyzer",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Get API key from Streamlit secrets or environment variables
def get_api_key():
    try:
        # Try Streamlit secrets first (for cloud deployment)
        return st.secrets["GEMINI_API_KEY"]
    except (KeyError, FileNotFoundError, AttributeError):
        # Fall back to environment variable (for local development)
        return os.environ.get("GEMINI_API_KEY")

# Check if API key is available
api_key = get_api_key()
if not api_key:
    st.error("🔑 GEMINI_API_KEY is not set!")
    st.markdown("""
    ### 🔧 How to add your API key:
    
    **For Streamlit Cloud:**
    1. Go to your app dashboard: [share.streamlit.io](https://share.streamlit.io)
    2. Click on your app settings (⚙️)
    3. Navigate to "Secrets" tab
    4. Add this exact text:
    ```
    GEMINI_API_KEY = "your_actual_api_key_here"
    ```
    
    **For local development:**
    1. Create `.streamlit/secrets.toml` file in your project
    2. Add: `GEMINI_API_KEY = "your_api_key_here"`
    
    **📋 Get your API key:** 
    - Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
    - Click "Create API key" 
    - Copy the key and paste it in secrets
    
    **⚡ Quick fix for Streamlit Cloud:**
    1. Copy your API key
    2. Go to app settings → Secrets
    3. Paste: `GEMINI_API_KEY = "YOUR_KEY_HERE"`
    4. Save and restart the app
    """)
    st.stop()

# Set the API key in environment for the modules
os.environ["GEMINI_API_KEY"] = api_key

# App title and description
st.title("🏃‍♂️ AI Fitness Health Analyzer")
st.markdown("""
Welcome! Upload a screenshot of your fitness tracker and get **personalized health insights** powered by AI.

📊 **What we analyze:** Steps, calories, distance, activity levels, and more  
🤖 **Powered by:** Google Gemini 1.5-flash AI  
🎯 **Get:** Custom recommendations for fitness, nutrition, and wellness  
""")

# Sidebar for navigation
st.sidebar.title("📱 Navigation")
page = st.sidebar.radio("Choose a section:", 
    ["📸 Upload Image", "📊 Dashboard", "📈 History", "ℹ️ About"],
    index=0
)

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
if page == "📸 Upload Image":
    st.header("📸 Upload Fitness Data Image")
    
    # Add helpful tips
    with st.expander("💡 Tips for best results"):
        st.markdown("""
        **✅ Good images:**
        - Clear screenshots from fitness apps (Apple Health, Google Fit, Fitbit, etc.)
        - Images showing steps, calories, distance, or activity summaries
        - Good lighting and readable text
        
        **❌ Avoid:**
        - Blurry or dark images
        - Images without clear fitness numbers
        - Very small screenshots
        """)
    
    uploaded_file = st.file_uploader(
        "Choose an image of your fitness tracker summary", 
        type=["jpg", "jpeg", "png"],
        help="Upload a clear screenshot showing your fitness metrics"
    )
    
    if uploaded_file is not None:
        try:
            # Display the uploaded image
            image = Image.open(uploaded_file)
            
            col1, col2 = st.columns([2, 1])
            with col1:
                st.image(image, caption="📱 Your uploaded image", use_column_width=True)
            
            with col2:
                st.info(f"""
                **Image Info:**
                - Size: {image.size[0]} x {image.size[1]} pixels
                - Format: {image.format}
                - File size: {len(uploaded_file.getvalue()) / 1024:.1f} KB
                """)
            
            # Process button
            if st.button("🚀 Analyze Image", type="primary", use_container_width=True):
                with st.spinner("🤖 Processing image with AI... This may take a moment..."):
                    # Check image dimensions and size
                    if max(image.size) < 200:
                        st.error("📏 Image is too small. Please upload a larger image with clear text.")
                        st.stop()
                    
                    # Create a progress bar
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    
                    try:
                        # Step 1: Extract data
                        status_text.text("🔍 Extracting fitness data from image...")
                        progress_bar.progress(25)
                        
                        fitness_data = extract_fitness_data_from_image(image)
                        
                        if not fitness_data:
                            st.error("❌ Could not extract fitness data from the image. Please try another image with clearer fitness metrics.")
                            st.info("💡 **Tips:** Use images that clearly show numbers for steps, calories, or other fitness metrics. Make sure the text is readable and not blurry.")
                            st.stop()
                        
                        # Step 2: Analyze data
                        status_text.text("📊 Analyzing your health metrics...")
                        progress_bar.progress(50)
                        
                        analysis_results = analyze_health_metrics(fitness_data)
                        
                        # Step 3: Generate recommendations
                        status_text.text("💡 Generating personalized recommendations...")
                        progress_bar.progress(75)
                        
                        recommendations = generate_recommendations(analysis_results)
                        
                        # Step 4: Save results
                        status_text.text("💾 Saving your results...")
                        progress_bar.progress(100)
                        
                        # Store in session state
                        st.session_state.fitness_data = fitness_data
                        st.session_state.analysis_results = analysis_results
                        st.session_state.recommendations = recommendations
                        
                        # Add to history
                        st.session_state.history.append({
                            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                            "fitness_data": fitness_data,
                            "analysis_results": analysis_results,
                            "recommendations": recommendations
                        })
                        
                        # Clear progress
                        progress_bar.empty()
                        status_text.empty()
                        
                        # Show success
                        st.success("🎉 Analysis complete! Check out your results below and navigate to Dashboard for detailed insights.")
                        
                        # Show quick preview
                        st.subheader("🔍 Quick Preview")
                        col1, col2, col3 = st.columns(3)
                        
                        with col1:
                            steps = fitness_data.get('steps', 'N/A')
                            st.metric("👣 Steps", steps)
                        
                        with col2:
                            calories = fitness_data.get('calories') or fitness_data.get('total_calories', 'N/A')
                            st.metric("🔥 Calories", calories)
                        
                        with col3:
                            fitness_score = analysis_results.get('fitness_score', 'N/A')
                            st.metric("⭐ Fitness Score", f"{fitness_score}/100" if fitness_score != 'N/A' else 'N/A')
                        
                        # Navigation buttons
                        col1, col2 = st.columns(2)
                        with col1:
                            if st.button("📊 View Full Dashboard", type="primary"):
                                st.experimental_set_query_params(page="dashboard")
                        with col2:
                            if st.button("📈 View History"):
                                st.experimental_set_query_params(page="history")
                        
                    except Exception as e:
                        st.error(f"❌ Error during analysis: {str(e)}")
                        st.info("Please try a different image or contact support if the issue persists.")
                        
        except Exception as e:
            st.error(f"❌ Error processing image: {str(e)}")
            st.info("Please try a different image format or check if the file is corrupted.")

# Dashboard Page
elif page == "📊 Dashboard":
    st.header("📊 Your Health Dashboard")
    
    if st.session_state.fitness_data and st.session_state.analysis_results and st.session_state.recommendations:
        # Display date of analysis
        if st.session_state.history:
            latest_date = st.session_state.history[-1]["date"]
            st.caption(f"📅 Latest analysis: {latest_date}")
        
        # Key metrics in columns
        st.subheader("📈 Key Metrics")
        metrics = st.session_state.fitness_data
        
        # Create columns for metrics
        metric_cols = st.columns(len(metrics))
        for i, (metric, value) in enumerate(metrics.items()):
            with metric_cols[i % len(metric_cols)]:
                # Add appropriate emoji for each metric
                emoji_map = {
                    'steps': '👣',
                    'calories': '🔥',
                    'total_calories': '🔥',
                    'distance': '📏',
                    'active_minutes': '⏱️',
                    'stairs': '🪜'
                }
                emoji = emoji_map.get(metric, '📊')
                st.metric(f"{emoji} {metric.replace('_', ' ').title()}", value)
        
        # Create two columns for analysis and visualization
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("🎯 Health Analysis")
            analysis = st.session_state.analysis_results
            
            # Show overall fitness prominently
            if 'overall_fitness' in analysis:
                st.info(f"🏆 **Overall Fitness Level:** {analysis['overall_fitness']}")
            
            for category, level in analysis.items():
                if category not in ["raw_data", "overall_fitness", "insights"]:
                    st.write(f"**{category.replace('_', ' ').title()}:** {level}")
            
            # Show insights if available
            if 'insights' in analysis and analysis['insights']:
                st.subheader("💡 Health Insights")
                for insight in analysis['insights']:
                    st.write(f"• {insight}")
        
        with col2:
            st.subheader("📊 Data Visualization")
            
            # Create a simple bar chart of the metrics
            metrics_to_plot = {k: v for k, v in metrics.items() if isinstance(v, (int, float))}
            
            if metrics_to_plot:
                fig, ax = plt.subplots(figsize=(10, 6))
                bars = ax.bar(metrics_to_plot.keys(), metrics_to_plot.values())
                ax.set_title("Your Fitness Metrics")
                ax.set_ylabel("Value")
                ax.set_xlabel("Metric")
                
                # Add value labels on bars
                for bar in bars:
                    height = bar.get_height()
                    ax.text(bar.get_x() + bar.get_width()/2., height,
                           f'{height}', ha='center', va='bottom')
                
                plt.xticks(rotation=45, ha='right')
                plt.tight_layout()
                st.pyplot(fig)
            else:
                st.info("No numeric data available for visualization")
        
        # Recommendations section
        st.subheader("🎯 Personalized Recommendations")
        recommendations = st.session_state.recommendations
        
        tab1, tab2, tab3 = st.tabs(["🏃 Activity", "🥗 Nutrition", "🧘 Wellness"])
        
        with tab1:
            st.markdown(recommendations.get("activity", "No activity recommendations available"))
        
        with tab2:
            st.markdown(recommendations.get("nutrition", "No nutrition recommendations available"))
        
        with tab3:
            st.markdown(recommendations.get("wellness", "No wellness recommendations available"))
        
    else:
        st.info("📸 No data to display. Please upload and analyze an image first!")
        if st.button("📱 Upload Image Now", type="primary"):
            st.experimental_set_query_params(page="upload")

# History Page
elif page == "📈 History":
    st.header("📈 Your Analysis History")
    
    if st.session_state.history:
        st.write(f"📊 Total analyses: **{len(st.session_state.history)}**")
        
        for i, entry in enumerate(reversed(st.session_state.history)):
            with st.expander(f"📅 Analysis from {entry['date']}", expanded=(i==0)):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write("**🔢 Fitness Data:**")
                    for metric, value in entry["fitness_data"].items():
                        st.write(f"• {metric.replace('_', ' ').title()}: {value}")
                
                with col2:
                    st.write("**🎯 Analysis Results:**")
                    for category, level in entry["analysis_results"].items():
                        if category not in ["raw_data", "insights"]:
                            st.write(f"• {category.replace('_', ' ').title()}: {level}")
                
                # Show a preview of recommendations
                st.write("**💡 Recommendations Preview:**")
                for category, rec in entry["recommendations"].items():
                    preview = rec[:100] + "..." if len(rec) > 100 else rec
                    st.write(f"**{category.title()}:** {preview}")
    else:
        st.info("📊 No history available yet. Start by analyzing a fitness image!")
        if st.button("📸 Upload Your First Image", type="primary"):
            st.experimental_set_query_params(page="upload")

# About Page
elif page == "ℹ️ About":
    st.header("ℹ️ About AI Fitness Health Analyzer")
    
    st.markdown("""
    ## 🚀 How It Works
    
    The AI Fitness Health Analyzer uses **Google's Gemini 1.5-flash AI model** to:
    
    1. **🔍 Extract Data**: Convert fitness tracker screenshots into structured data
    2. **📊 Analyze Metrics**: Interpret your activity levels based on scientific guidelines  
    3. **💡 Generate Insights**: Provide personalized recommendations for your health journey
    
    ## 🔒 Privacy Notice
    
    Your uploaded images are processed securely and **not stored permanently**. We value your privacy and data security.
    
    ## 🛠️ Technical Stack
    
    - **🤖 AI Model**: Google Gemini 1.5-flash
    - **🖼️ Image Processing**: OpenCV, Tesseract OCR
    - **🌐 Frontend**: Streamlit
    - **🐍 Backend**: Python, Flask
    
    ## 📞 Support
    
    For questions or feedback, please contact: **support@aifitnesshealthanalyzer.com**
    
    ## 🌟 Features
    
    ✅ **Smart Image Analysis** - Extracts data from any fitness app screenshot  
    ✅ **Personalized Insights** - AI-powered health recommendations  
    ✅ **Progress Tracking** - View your fitness journey over time  
    ✅ **Privacy First** - Your data stays secure and private  
    ✅ **Mobile Friendly** - Works on any device  
    """)
    
    # Add some stats if available
    if st.session_state.history:
        st.subheader("📊 Your Stats")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("📸 Images Analyzed", len(st.session_state.history))
        
        with col2:
            # Calculate average steps if available
            steps_data = [entry["fitness_data"].get("steps", 0) for entry in st.session_state.history if entry["fitness_data"].get("steps")]
            avg_steps = sum(steps_data) / len(steps_data) if steps_data else 0
            st.metric("👣 Avg Daily Steps", f"{avg_steps:,.0f}")
        
        with col3:
            st.metric("📅 Days Tracked", len(st.session_state.history))

# Footer
st.markdown("---")
st.markdown("© 2024 AI Fitness Health Analyzer | Powered by Google Gemini AI | 🚀 **[View on GitHub](https://github.com/Nitishkumarmaury/AI-Fitness-Health-Analyzers)**")
