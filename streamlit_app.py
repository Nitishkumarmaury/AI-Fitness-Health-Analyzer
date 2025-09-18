import osimport osimport os

import streamlit as st

import pandas as pdimport streamlit as stimport streamlit as st

import matplotlib.pyplot as plt

import seaborn as snsimport pandas as pdimport pandas as pd

import google.generativeai as genai

from PIL import Image as PILImageimport matplotlib.pyplot as pltimport matplotlib.pyplot as plt

import numpy as np

import cv2import seaborn as snsimport seaborn as sns

from dotenv import load_dotenv

import google.generativeai as genaiimport google.generativeai as genai

# Load environment variables

load_dotenv()from PIL import Image as PILImagefrom PIL import Image as PILImage



# Configure pageimport numpy as npimport numpy as np

st.set_page_config(

    page_title="AI Fitness Health Analyzer",import cv2import cv2

    page_icon="🏃‍♂️",

    layout="wide"from dotenv import load_dotenv

)

# Load environment variables

# Configure Gemini API

GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]# Load environment variablesfrom dotenv import load_dotenv

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')load_dotenv()load_dotenv()



def main():        try:

    st.title("🏃‍♂️ AI Fitness Health Analyzer")

    st.markdown("""# Configure page            if package == 'opencv-python':

    Upload your fitness summary image and get AI-powered health insights and recommendations.

    """)st.set_page_config(                __import__('cv2')



    uploaded_file = st.file_uploader("Choose a fitness summary image", type=['jpg', 'jpeg', 'png'])    page_title="AI Fitness Health Analyzer",            elif package == 'Pillow':

    

    if uploaded_file is not None:    page_icon="🏃‍♂️",                __import__('PIL')

        # Display uploaded image

        image = PILImage.open(uploaded_file)    layout="wide"            elif package == 'scikit-learn':

        st.image(image, caption='Uploaded Image', use_column_width=True)

        )                __import__('sklearn')

        if st.button('Analyze Image'):

            with st.spinner('Analyzing your fitness data...'):            elif package == 'python-dotenv':

                try:

                    # Convert image for Gemini# Configure Gemini API                __import__('dotenv')

                    response = model.generate_content([

                        "Analyze this fitness summary image and extract the following metrics:\n"GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]            elif package == 'replicate':

                        "- Steps count\n"

                        "- Calories burned\n"genai.configure(api_key=GEMINI_API_KEY)                __import__('replicate')

                        "- Distance covered\n"

                        "- Activity duration\n"model = genai.GenerativeModel('gemini-1.5-flash')            else:

                        "Provide the data in a structured format.",

                        image                __import__(package)

                    ])

                    def main():        except ImportError:

                    # Display results

                    st.subheader("📊 Analysis Results")    st.title("🏃‍♂️ AI Fitness Health Analyzer")            missing_packages.append(package)

                    st.write(response.text)

                        st.markdown("""    

                    # Generate health insights

                    st.subheader("💡 Health Insights")    Upload your fitness summary image and get AI-powered health insights and recommendations.    if missing_packages:

                    insights_response = model.generate_content([

                        "Based on this fitness data, provide 3-4 specific health insights and recommendations."    """)        print(f"Missing packages: {', '.join(missing_packages)}")

                        "Format them as bullet points.",

                        response.text        print("Installing missing packages automatically...")

                    ])

                    st.write(insights_response.text)    uploaded_file = st.file_uploader("Choose a fitness summary image", type=['jpg', 'jpeg', 'png'])        for package in missing_packages:

                    

                except Exception as e:                print(f"Installing {package}...")

                    st.error(f"An error occurred during analysis: {str(e)}")

    if uploaded_file is not None:            try:

if __name__ == "__main__":

    main()        # Display uploaded image                install_package(package)

        image = PILImage.open(uploaded_file)                print(f"✅ {package} installed successfully!")

        st.image(image, caption='Uploaded Image', use_column_width=True)            except Exception as e:

                        print(f"❌ Failed to install {package}: {e}")

        if st.button('Analyze Image'):        

            with st.spinner('Analyzing your fitness data...'):        # Special handling for replicate

                try:        if 'replicate' in missing_packages:

                    # Convert image for Gemini            print("\n🔄 Installing Replicate API client...")

                    response = model.generate_content([            try:

                        "Analyze this fitness summary image and extract the following metrics:\n"                subprocess.check_call([sys.executable, "-m", "pip", "install", "replicate", "--upgrade"])

                        "- Steps count\n"                print("✅ Replicate installed successfully!")

                        "- Calories burned\n"            except Exception as e:

                        "- Distance covered\n"                print(f"❌ Replicate installation failed: {e}")

                        "- Activity duration\n"                print("💡 Try manually: pip install replicate")

                        "Provide the data in a structured format.",        

                        image        print("\nInstallation complete! Please restart with: streamlit run main.py")

                    ])        return False

                        return True

                    # Display results

                    st.subheader("📊 Analysis Results")def load_gemini_credentials():

                    st.write(response.text)    """Load Google Gemini API key from environment variable"""

                        api_key = os.getenv('GEMINI_API_KEY')

                    # Generate health insights    if not api_key:

                    st.subheader("💡 Health Insights")        raise ValueError("GEMINI_API_KEY environment variable is not set")

                    insights_response = model.generate_content([    return api_key

                        "Based on this fitness data, provide 3-4 specific health insights and recommendations."

                        "Format them as bullet points.",try:

                        response.text    import streamlit as st

                    ])    import pandas as pd

                    st.write(insights_response.text)    import matplotlib.pyplot as plt

                        import seaborn as sns

                except Exception as e:    from image_processor import ImageProcessor

                    st.error(f"An error occurred during analysis: {str(e)}")    from health_analyzer import HealthAnalyzer

    

if __name__ == "__main__":    # Load Google Gemini API key early

    main()    GEMINI_API_KEY = load_gemini_credentials()
    
    # Google Gemini setup instead of Replicate
    try:
        import google.generativeai as genai
        import json
        import base64
        import os
        from PIL import Image as PILImage
        
        # Configure Gemini API
        genai.configure(api_key=GEMINI_API_KEY)
        gemini_model = genai.GenerativeModel('gemini-1.5-flash')
        
        GEMINI_AVAILABLE = True
        print("✅ Google Gemini API client created successfully")
        
    except ImportError:
        GEMINI_AVAILABLE = False
        print("❌ Google AI package not installed - installing now...")
        try:
            install_package('google-generativeai')
            print("✅ google-generativeai installed successfully! Please restart the application.")
        except Exception as e:
            print(f"❌ Failed to install google-generativeai: {e}")
    except Exception as e:
        GEMINI_AVAILABLE = False
        print(f"❌ Gemini initialization failed: {e}")
        
    import json
    
    # If we get here, core imports succeeded
    IMPORTS_SUCCESSFUL = True
except ImportError as e:
    IMPORTS_SUCCESSFUL = False
    GEMINI_API_KEY = "NOT_AVAILABLE"  # Add fallback value
    GEMINI_AVAILABLE = False
    if 'streamlit' in globals():
        st.error(f"Missing module: {e}")
        st.error("Please create the missing files or check the installation.")

def test_replicate_api():
    """Test Replicate API"""
    if not REPLICATE_AVAILABLE:
        return False, "Replicate not available"
    
    try:
        # Test with a simple text generation
        output = replicate.run(
            "meta/llama-2-7b-chat:13c3cdee13ee059ab779f0291d29054dab00a47dad8261375654de5540165fb0",
            input={"prompt": "Say 'Replicate API working!'", "max_tokens": 10}
        )
        result = "".join(output) if isinstance(output, list) else str(output)
        return True, f"Replicate API working! {result[:50]}..."
        
    except Exception as e:
        print(f"Replicate test failed: {e}")
        return False, str(e)

def test_gemini_api():
    """Test Google Gemini API"""
    if not GEMINI_AVAILABLE:
        return False, "Gemini not available"
    
    try:
        response = gemini_model.generate_content("Say 'Google Gemini API working!'")
        return True, f"Gemini API working! {response.text[:50]}..."
        
    except Exception as e:
        print(f"Gemini test failed: {e}")
        return False, str(e)

def analyze_image_with_replicate_ocr(image_path):
    """Analyze image using Replicate OCR models"""
    if not REPLICATE_AVAILABLE:
        return "Replicate not available"
    
    try:
        # Read and encode image
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
            image_base64 = base64.b64encode(image_data).decode('utf-8')
            image_url = f"data:image/jpeg;base64,{image_base64}"
        
        results = {}
        
        # 1. Use OCR model to extract text
        try:
            ocr_output = replicate.run(
                "abiruyt/text-extract-ocr:a524caeaa23495bc9edc2f3b3b91b308d3643a0e", 
                input={"image": image_url}
            )
            
            extracted_text = str(ocr_output) if ocr_output else ""
            results['text'] = [extracted_text] if extracted_text else []
            
        except Exception as e:
            results['text'] = [f"OCR error: {e}"]
        
        # 2. Try alternative OCR model if first fails
        if not results.get('text') or "error" in str(results['text']).lower():
            try:
                # Try PaddleOCR model
                ocr_output2 = replicate.run(
                    "cjwbw/paddleocr:f40f9ad5dc7ad18b8ce28b4b31ac27a9c6b72d3a0ed7e29d3b0e8b6ac2b30678",
                    input={"image": image_url}
                )
                
                if ocr_output2:
                    results['text'] = [str(ocr_output2)]
                    
            except Exception as e:
                if not results.get('text'):
                    results['text'] = [f"Alternative OCR error: {e}"]
        
        # 3. Extract fitness data from detected text
        fitness_metrics = extract_fitness_from_text(results.get('text', []))
        results['fitness_data'] = fitness_metrics
        
        return results
        
    except Exception as e:
        return f"Replicate OCR Analysis Error: {e}"

def analyze_image_with_gemini(image_path):
    """Analyze image using Google Gemini Vision with enhanced fitness data extraction"""
    if not GEMINI_AVAILABLE:
        return "Gemini not available"
    
    try:
        # Load and process image
        image = PILImage.open(image_path)
        
        results = {}
        
        # Extract text from image using Gemini Vision with specific fitness focus
        try:
            prompt = """Analyze this fitness summary image and extract ALL visible text and numerical data exactly as shown. 
            Focus specifically on these fitness metrics:
            - Steps (look for numbers like 4,889 or 4889)
            - Calories (Total Calories Burned, Move calories, etc.)
            - Distance (in km)
            - Stairs Climbed or Floors
            - Move Goal and Move Progress
            - Date information
            
            Return the extracted text EXACTLY as it appears in the image, preserving formatting, numbers, and punctuation.
            Include both the labels and the numerical values."""
            
            response = gemini_model.generate_content([prompt, image])
            extracted_text = response.text if response.text else ""
            results['text'] = [extracted_text] if extracted_text else []
            
            # Also try a second extraction with structured format
            if extracted_text:
                structured_prompt = f"""Based on this extracted text: "{extracted_text}"
                
                Extract the specific fitness values and format them as:
                Steps: [number]
                Total Calories Burned: [number] kcal
                Distance: [number] km
                Stairs Climbed: [number]
                Move Goal: [number] kcal
                Move Progress: [number]/[goal] kcal
                Date: [date if available]
                
                Only include the lines where you found actual values."""
                
                structured_response = gemini_model.generate_content(structured_prompt)
                if structured_response.text:
                    results['text'].append(structured_response.text)
            
        except Exception as e:
            results['text'] = [f"Gemini OCR error: {e}"]
        
        # Extract fitness data from detected text
        fitness_metrics = extract_fitness_from_text(results.get('text', []))
        
        # If no data extracted, try direct value extraction with Gemini
        if not fitness_metrics or (not fitness_metrics.get('steps') and not fitness_metrics.get('stairs')):
            try:
                direct_prompt = """Look at this fitness image and extract these specific numbers:
                1. Steps count (usually a 4-digit number like 4889)
                2. Stairs climbed count (usually a small number like 3)
                3. Total calories burned (usually a 4-digit number with 'kcal')
                4. Distance in km (decimal number like 3.41)
                5. Move goal and progress (format like 92/120 kcal)
                
                Reply in this exact format:
                STEPS: [number]
                STAIRS: [number]
                CALORIES: [number]
                DISTANCE: [number]
                MOVE: [current]/[goal]"""
                
                direct_response = gemini_model.generate_content([direct_prompt, image])
                if direct_response.text:
                    # Parse direct response
                    direct_data = parse_direct_gemini_response(direct_response.text)
                    if direct_data:
                        fitness_metrics.update(direct_data)
                        results['text'].append(f"Direct extraction: {direct_response.text}")
            
            except Exception as e:
                print(f"Direct extraction failed: {e}")
        
        results['fitness_data'] = fitness_metrics
        
        # Debug: Print what Gemini extracted
        print(f"DEBUG: Gemini extracted text: {results.get('text', [])}")
        print(f"DEBUG: Parsed fitness data: {fitness_metrics}")
        
        return results
        
    except Exception as e:
        return f"Gemini Analysis Error: {e}"

def parse_direct_gemini_response(response_text):
    """Parse direct Gemini response for fitness data"""
    import re
    
    fitness_data = {}
    text_lower = response_text.lower()
    
    # Extract steps
    steps_match = re.search(r'steps:\s*(\d{1,5})', text_lower)
    if steps_match:
        steps_value = int(steps_match.group(1))
        if 100 <= steps_value <= 50000:
            fitness_data['steps'] = steps_value
    
    # Extract stairs
    stairs_match = re.search(r'stairs:\s*(\d{1,3})', text_lower)
    if stairs_match:
        stairs_value = int(stairs_match.group(1))
        if 1 <= stairs_value <= 500:
            fitness_data['stairs'] = stairs_value
    
    # Extract calories
    calories_match = re.search(r'calories:\s*(\d{1,5})', text_lower)
    if calories_match:
        cal_value = int(calories_match.group(1))
        if 100 <= cal_value <= 5000:
            fitness_data['total_calories'] = cal_value
    
    # Extract distance
    distance_match = re.search(r'distance:\s*(\d+\.?\d*)', text_lower)
    if distance_match:
        dist_value = float(distance_match.group(1))
        if 0.01 <= dist_value <= 100:
            fitness_data['distance'] = dist_value
    
    # Extract move goal/progress
    move_match = re.search(r'move:\s*(\d+)/(\d+)', text_lower)
    if move_match:
        fitness_data['move_progress'] = int(move_match.group(1))
        fitness_data['move_goal'] = int(move_match.group(2))
    
    return fitness_data

def extract_fitness_from_text(text_lines):
    """Extract fitness metrics from detected text with improved patterns"""
    import re
    
    fitness_data = {}
    
    # Combine all text lines into one string for better pattern matching
    full_text = " ".join(text_lines).lower() if text_lines else ""
    
    # Debug: Print the text being analyzed
    print(f"DEBUG: Analyzing text: {full_text[:300]}...")
    
    # Enhanced steps extraction patterns - more specific for "**Steps:** 4,889" format
    steps_patterns = [
        r'\*?\*?steps\*?\*?[:\s]*(\d{1,3}),(\d{3})',  # "**Steps:** 4,889" with comma
        r'\*?\*?steps\*?\*?[:\s]*(\d{1,5})',  # "**Steps:** 4889" without comma
        r'steps[:\s]*(\d{1,3}),(\d{3})',  # "steps: 4,889"
        r'steps[:\s]*(\d{1,5})',  # "steps: 4889"
        r'(\d{1,5})\s*steps?',  # "4889 steps"
        r'(\d{4,5})(?=\s|$|[^\d])',  # 4-5 digit numbers (likely steps) standalone
        r'(\d{3,4})(?=\s*(?:steps|distance|km|cal|kcal))',  # 3-4 digits before fitness keywords
    ]
    
    for pattern in steps_patterns:
        steps_match = re.search(pattern, full_text)
        if steps_match:
            if len(steps_match.groups()) == 2 and steps_match.group(2):  # Format with comma like "4,889"
                steps_value = int(steps_match.group(1) + steps_match.group(2))
            else:
                steps_value = int(steps_match.group(1))
            
            # Relaxed validation for step count (500-50000)
            if 500 <= steps_value <= 50000:
                fitness_data['steps'] = steps_value
                print(f"DEBUG: Found steps: {steps_value}")
                break

    # Enhanced move goal and progress extraction - specific for "30/120 kcal" format
    move_patterns = [
        r'move[:\s]*(\d+)[/\\](\d+)\s*kcal',  # "move: 30/120 kcal"
        r'(\d+)[/\\](\d+)\s*kcal',  # "30/120 kcal"
        r'current move calories[:\s]*(\d+)\s*kcal.*?move goal[:\s]*(\d+)\s*kcal',  # separate current and goal
        r'move goal[:\s]*(\d+)\s*kcal',  # "move goal: 120 kcal"
        r'move progress[:\s]*(\d+)[/\\](\d+)\s*kcal',  # "move progress: 92/120 kcal"
        r'current move[:\s]*(\d+)',  # "current move: 30"
    ]
    
    for pattern in move_patterns:
        move_match = re.search(pattern, full_text)
        if move_match:
            if len(move_match.groups()) == 2:  # Format like "30/120"
                fitness_data['move_progress'] = int(move_match.group(1))
                fitness_data['move_goal'] = int(move_match.group(2))
                print(f"DEBUG: Found move progress/goal: {move_match.group(1)}/{move_match.group(2)}")
            else:
                fitness_data['move_goal'] = int(move_match.group(1))
                print(f"DEBUG: Found move goal: {move_match.group(1)}")
            break
    
    # Enhanced total calories extraction - prioritize "Total Calories Burned"
    total_cal_patterns = [
        r'total calories burned[:\s]*(\d{1,5})\s*kcal',  # "Total Calories Burned: 1,621 kcal"
        r'total calories burned[:\s]*(\d{1,3}),(\d{3})\s*kcal',  # "Total Calories Burned: 1,621 kcal" with comma
        r'total calories burned[:\s]*(\d{1,5})',  # "Total Calories Burned: 1621"
        r'total calories burned[:\s]*(\d{1,3}),(\d{3})',  # "Total Calories Burned: 1,621" with comma
        r'calories burned[:\s]*(\d{1,5})\s*kcal',  # "Calories Burned: 1621 kcal"
        r'calories burned[:\s]*(\d{1,3}),(\d{3})\s*kcal',  # "Calories Burned: 1,621 kcal"
        r'total calories[:\s]*(\d{1,5})\s*kcal',
        r'total calories[:\s]*(\d{1,3}),(\d{3})\s*kcal',
        r'burned[:\s]*(\d{1,5})\s*kcal',
        r'burned[:\s]*(\d{1,3}),(\d{3})\s*kcal',
        r'(\d{1,5})\s*kcal(?=.*total|.*burned)',  # numbers with kcal near total/burned
        r'(\d{1,3}),(\d{3})\s*kcal(?=.*total|.*burned)',  # with comma
        r'total[:\s]*(\d{1,5})',
        r'total[:\s]*(\d{1,3}),(\d{3})',
    ]
    
    for pattern in total_cal_patterns:
        cal_match = re.search(pattern, full_text)
        if cal_match:
            if len(cal_match.groups()) == 2:  # Format with comma like "1,621"
                cal_value = int(cal_match.group(1) + cal_match.group(2))
            else:
                cal_value = int(cal_match.group(1))
            
            # Validate reasonable total calorie count (100-5000)
            if 100 <= cal_value <= 5000:
                fitness_data['total_calories'] = cal_value
                print(f"DEBUG: Found total calories: {cal_value}")
                break
    
    # Enhanced distance extraction patterns
    dist_patterns = [
        r'distance[:\s]*(\d+\.?\d*)\s*km',
        r'(\d+\.\d+)\s*km',  # Prioritize decimal numbers with km
        r'(\d+\.?\d*)\s*kilometers?',
        r'distance[:\s]*(\d+\.?\d*)',
        r'(\d+\.\d+)(?=\s*km|\s*k\s|$)'  # Decimal numbers followed by km
    ]
    
    for pattern in dist_patterns:
        dist_match = re.search(pattern, full_text)
        if dist_match:
            dist_value = float(dist_match.group(1))
            # Validate reasonable distance (0.01-100 km) - lowered minimum
            if 0.01 <= dist_value <= 100:
                fitness_data['distance'] = dist_value
                print(f"DEBUG: Found distance: {dist_value}")
                break
    
    # Enhanced stairs/floors extraction patterns - specific for "**Stairs Climbed:** 3"
    stairs_patterns = [
        r'\*?\*?stairs climbed\*?\*?[:\s]*(\d+)',  # "**Stairs Climbed:** 3"
        r'stairs climbed[:\s]*(\d+)',  # "Stairs Climbed: 3"
        r'climbed[:\s]*(\d+)',  # "Climbed: 3"
        r'\*?\*?stairs\*?\*?[:\s]*(\d+)',  # "**Stairs:** 3"
        r'stairs[:\s]*(\d+)',  # "Stairs: 3"
        r'(\d+)\s*(?:stairs?|floors?|flights?)',  # "3 stairs"
        r'(?:stairs?|floors?|flights?)[:\s]*(\d+)',  # "stairs: 3"
        r'(\d+)\s*fl(?:oor|ight)?s?',  # "3 floors"
        r'(\d+)(?=\s*stairs|\s*climbed)',  # Number before stairs/climbed
        r'(\d+)(?=\s*$)',  # Single digit at end of line (might be stairs)
    ]
    
    for pattern in stairs_patterns:
        stairs_match = re.search(pattern, full_text)
        if stairs_match:
            stairs_value = int(stairs_match.group(1))
            # Validate reasonable stairs count (1-500) - increased maximum
            if 1 <= stairs_value <= 500:
                fitness_data['stairs'] = stairs_value
                print(f"DEBUG: Found stairs: {stairs_value}")
                break
    
    # Extract recent activity calories if mentioned
    activity_cal_patterns = [
        r'recent activity calories[:\s]*(\d+)\s*kcal',
        r'activity calories[:\s]*(\d+)',
        r'recent[:\s]*(\d+)\s*kcal'
    ]
    
    for pattern in activity_cal_patterns:
        activity_match = re.search(pattern, full_text)
        if activity_match:
            activity_value = int(activity_match.group(1))
            if 1 <= activity_value <= 1000:
                fitness_data['recent_activity_calories'] = activity_value
                print(f"DEBUG: Found recent activity calories: {activity_value}")
                break
    
    print(f"DEBUG: Final extracted data: {fitness_data}")
    return fitness_data

def generate_ai_food_plan(fitness_data):
    """Generate AI food recommendations using Google Gemini"""
    if not GEMINI_AVAILABLE:
        return "Google Gemini not available for AI recommendations"
    
    if not fitness_data:
        return "No fitness data available for recommendations"
    
    try:
        steps = fitness_data.get('steps', 0)
        calories = fitness_data.get('total_calories', 0)
        distance = fitness_data.get('distance', 0)
        
        prompt = f"""You are a professional nutritionist. Based on this fitness data, create a personalized meal plan:
        - Steps: {steps}
        - Calories burned: {calories}
        - Distance: {distance} km
        
        Provide specific meal suggestions for breakfast, lunch, dinner, and snacks with portion sizes. 
        Keep it practical and healthy. Format nicely with emojis and clear sections."""
        
        response = gemini_model.generate_content(prompt)
        return response.text if response.text else "No response generated"
        
    except Exception as e:
        return f"Error generating AI food plan: {e}"

def generate_ai_exercise_plan(fitness_data):
    """Generate AI exercise recommendations using Google Gemini"""
    if not GEMINI_AVAILABLE:
        return "Google Gemini not available for AI recommendations"
    
    if not fitness_data:
        return "No fitness data available for recommendations"
    
    try:
        steps = fitness_data.get('steps', 0)
        calories = fitness_data.get('total_calories', 0)
        
        prompt = f"""You are a certified fitness trainer. Based on this fitness data, create a personalized exercise plan for tomorrow:
        - Today's steps: {steps}
        - Calories burned: {calories}
        
        Suggest specific cardio, strength, and flexibility exercises with duration and intensity. 
        Make it achievable and progressive. Use emojis and clear formatting."""
        
        response = gemini_model.generate_content(prompt)
        return response.text if response.text else "No response generated"
        
    except Exception as e:
        return f"Error generating AI exercise plan: {e}"

def generate_ai_health_insights(fitness_data):
    """Generate AI health insights using Google Gemini"""
    if not GEMINI_AVAILABLE:
        return "Google Gemini not available for AI recommendations"
    
    if not fitness_data:
        return "No fitness data available for analysis"
    
    try:
        steps = fitness_data.get('steps', 0)
        calories = fitness_data.get('total_calories', 0)
        
        prompt = f"""You are a health expert. Analyze this fitness data and provide health insights:
        - Steps: {steps}
        - Calories burned: {calories}
        
        Provide: 1) Fitness level assessment 2) Health benefits achieved 3) Areas for improvement 4) Meditation recommendations
        Be encouraging and specific. Use emojis and clear formatting."""
        
        response = gemini_model.generate_content(prompt)
        return response.text if response.text else "No response generated"
        
    except Exception as e:
        return f"Error generating AI health insights: {e}"

if IMPORTS_SUCCESSFUL:
    def main():
        st.set_page_config(page_title="AI Fitness Health Analyzer", page_icon="📊", layout="wide")
        
        # Custom CSS for classic styling
        st.markdown("""
        <style>
        .main-header {
            background: linear-gradient(90deg, #2E86AB, #A23B72, #F18F01);
            padding: 2rem;
            border-radius: 10px;
            margin-bottom: 2rem;
            text-align: center;
            color: white;
        }
        .metric-card {
            background: #f8f9fa;
            padding: 1rem;
            border-radius: 8px;
            border: 1px solid #dee2e6;
            margin: 0.5rem 0;
        }
        .sidebar .sidebar-content {
            background: #f8f9fa;
        }
        .stButton > button {
            background: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 0.5rem 1rem;
        }
        .classic-container {
            background: white;
            padding: 1.5rem;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin: 1rem 0;
        }
        .deployment-info {
            background: #e8f5e8;
            padding: 1rem;
            border-radius: 5px;
            border-left: 4px solid #28a745;
            margin: 1rem 0;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Main header with deployment info
        st.markdown("""
        <div class="main-header">
            <h1>📊 AI Fitness Health Analyzer</h1>
            <p>Advanced Fitness Data Analysis & Health Recommendations</p>
            <div class="deployment-info">
                <small>🚀 Python Web Application</small>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Show API credentials status in sidebar
        st.sidebar.header("⚙️ System Configuration")
        if GEMINI_AVAILABLE and GEMINI_API_KEY != "NOT_AVAILABLE":
            st.sidebar.success(f"✅ AI Service: Connected")
            st.sidebar.info("🤖 Model: Advanced Vision AI")
            st.sidebar.info("💡 Status: Ready for Analysis")
        else:
            st.sidebar.error("❌ AI Service: Not Connected")
            st.sidebar.warning("⚠️ Advanced features unavailable")
        
        # Check if AI is available and install if needed
        if not GEMINI_AVAILABLE:
            st.error("⚠️ AI Vision Service not available. Installation required.")
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("🔄 Install AI Service", type="primary"):
                    with st.spinner("Installing AI components..."):
                        try:
                            subprocess.check_call([sys.executable, "-m", "pip", "install", "google-generativeai", "--upgrade"])
                            st.success("✅ AI service installed! Please restart the application.")
                            st.info("Command: streamlit run main.py")
                            st.rerun()
                        except Exception as e:
                            st.error(f"❌ Installation failed: {e}")
            with col2:
                if st.button("📋 Check System"):
                    with st.spinner("Checking system requirements..."):
                        missing_found = check_and_install_requirements()
                        if not missing_found:
                            st.success("All components ready!")
                        else:
                            st.info("Some components were installed. Please restart.")
            with col3:
                st.info("💡 Manual installation:\n```bash\npip install google-generativeai\n```")
            return
        
        try:
            # Initialize processors
            image_processor = ImageProcessor()
            health_analyzer = HealthAnalyzer()
            
            # Check AI API status
            if GEMINI_AVAILABLE:
                with st.spinner("Connecting to AI Vision Service..."):
                    api_working, message = test_gemini_api()
                    if api_working:
                        st.success(f"🤖 AI Vision Service Connected! Ready for analysis.")
                    else:
                        st.error(f"❌ AI service connection failed: {message}")
                        api_working = False
            else:
                st.error("💡 AI Vision Service not available - check installation")
                api_working = False
            
            # File upload section
            st.markdown('<div class="classic-container">', unsafe_allow_html=True)
            st.header("📁 Upload Fitness Summary")
            st.markdown("Upload an image of your fitness summary for automated analysis")
            
            uploaded_file = st.file_uploader(
                "Select your fitness summary image", 
                type=['png', 'jpg', 'jpeg'],
                help="Supported formats: PNG, JPG, JPEG"
            )
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Action buttons
            col1, col2 = st.columns(2)
            with col1:
                if st.button("📊 Load Sample Data", help="Test the application with sample fitness data"):
                    demo_data = {
                        'steps': 4889,
                        'move_goal': 120,
                        'move_progress': 92,
                        'total_calories': 1621,
                        'distance': 3.41,
                        'stairs': 3,
                        'date': 'Sunday, 1 Jun 2025'
                    }
                    st.session_state.fitness_data = demo_data
                    st.session_state.extracted_text = "Sample data loaded: 4,889 steps, 1,621 total calories, 3.41km distance, 3 stairs climbed, Move: 92/120 kcal"
                    st.success("✅ Sample data loaded successfully!")
            
            with col2:
                if GEMINI_AVAILABLE and st.button("🔧 Test AI Service", help="Verify AI service connectivity"):
                    with st.spinner("Testing AI service..."):
                        success, response_text = test_gemini_api()
                        if success:
                            st.success(f"✅ AI Service Response: Connected and Ready")
                        else:
                            st.error(f"❌ Test Failed: {response_text}")
            
            # Image analysis section
            if uploaded_file is not None:
                st.markdown('<div class="classic-container">', unsafe_allow_html=True)
                col1, col2 = st.columns([1, 1])
                
                with col1:
                    st.subheader("📷 Uploaded Image")
                    st.image(uploaded_file, caption="Fitness Summary Image", use_column_width=True)
                
                with col2:
                    st.subheader("🔍 Analysis Controls")
                    if st.button("🚀 Analyze Fitness Data", type="primary"):
                        with st.spinner("Processing image with AI Vision..."):
                            # Save uploaded file temporarily
                            with open("temp_image.jpg", "wb") as f:
                                f.write(uploaded_file.getbuffer())
                            
                            # Use AI Vision to analyze the image
                            if GEMINI_AVAILABLE:
                                st.info("🔍 Processing with Advanced AI Vision...")
                                analysis_result = analyze_image_with_gemini("temp_image.jpg")
                                
                                if isinstance(analysis_result, dict):
                                    # Display AI analysis results
                                    if analysis_result.get('text'):
                                        st.write("📝 **Extracted Information:**")
                                        text_preview = " ".join(analysis_result['text'][:3])
                                        st.text_area("AI Vision Results:", text_preview[:500], height=100)
                                    
                                    # Use AI extracted fitness data if available
                                    if analysis_result.get('fitness_data'):
                                        fitness_data = analysis_result['fitness_data']
                                        st.success("✅ Fitness data extracted successfully!")
                                    else:
                                        # Fallback to local OCR
                                        extracted_text = image_processor.extract_text("temp_image.jpg")
                                        fitness_data = image_processor.parse_fitness_data(extracted_text)
                                        st.info("🔄 Using backup text recognition")
                                else:
                                    st.error(f"AI Analysis Error: {analysis_result}")
                                    # Fallback to local OCR
                                    extracted_text = image_processor.extract_text("temp_image.jpg")
                                    fitness_data = image_processor.parse_fitness_data(extracted_text)
                            else:
                                # Fallback to local OCR only
                                extracted_text = image_processor.extract_text("temp_image.jpg")
                                fitness_data = image_processor.parse_fitness_data(extracted_text)
                            
                            # Store in session state
                            st.session_state.fitness_data = fitness_data
                            st.session_state.extracted_text = str(analysis_result if GEMINI_AVAILABLE else extracted_text)
                
                st.markdown('</div>', unsafe_allow_html=True)
            
            # Display results if data is available
            if hasattr(st.session_state, 'fitness_data'):
                display_results(st.session_state.fitness_data, health_analyzer, api_working)
        
        except Exception as e:
            st.error(f"Application Error: {e}")
            st.info("Please ensure all required components are installed and try again.")

    def display_results(fitness_data, health_analyzer, ai_available=False):
        """Display analysis results with classic styling"""
        
        # Fitness Metrics Dashboard
        st.markdown('<div class="classic-container">', unsafe_allow_html=True)
        st.header("📊 Fitness Analysis Dashboard")
        
        # Show date if available
        if fitness_data.get('date'):
            st.info(f"📅 **Analysis Date:** {fitness_data['date']}")
        
        # Main metrics in a grid layout
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            move_goal = fitness_data.get('move_goal')
            if move_goal:
                st.metric("Move Goal", f"{move_goal} kcal")
            else:
                st.metric("Move Goal", "N/A")
        
        with col2:
            move_progress = fitness_data.get('move_progress')
            move_goal = fitness_data.get('move_goal')
            if move_progress and move_goal:
                st.metric("Move Progress", f"{move_progress}/{move_goal} kcal", 
                         delta=f"{move_progress/move_goal*100:.0f}% complete")
            else:
                st.metric("Move Progress", "N/A")
        
        with col3:
            calories = fitness_data.get('total_calories')
            if calories:
                st.metric("Total Calories", f"{calories:,} kcal")
            else:
                st.metric("Total Calories", "N/A")
        
        with col4:
            steps = fitness_data.get('steps')
            if steps:
                st.metric("Steps Taken", f"{steps:,}")
                step_progress = min(steps / 10000 * 100, 100)
                st.caption(f"Daily goal: {step_progress:.1f}%")
            else:
                st.metric("Steps Taken", "N/A")
        
        with col5:
            distance = fitness_data.get('distance')
            if distance:
                st.metric("Distance", f"{distance:.2f} km")
                if fitness_data.get('steps'):
                    avg_step_length = (distance * 1000) / fitness_data['steps']
                    st.caption(f"Avg step: {avg_step_length:.2f}m")
            else:
                st.metric("Distance", "N/A")
        
        # Additional metrics
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            stairs = fitness_data.get('stairs')
            if stairs:
                st.metric("Stairs Climbed", f"{stairs}")
                floors = stairs / 15
                st.caption(f"≈ {floors:.1f} floors")
            else:
                st.metric("Stairs Climbed", "N/A")

        # Progress visualization
        if fitness_data.get('move_goal') and fitness_data.get('move_progress'):
            progress_percentage = fitness_data['move_progress'] / fitness_data['move_goal']
            st.progress(progress_percentage)
            st.caption(f"Move Goal Progress: {fitness_data['move_progress']}/{fitness_data['move_goal']} kcal ({progress_percentage*100:.1f}%)")
        
        # Activity summary
        if any([fitness_data.get('steps'), fitness_data.get('total_calories'), fitness_data.get('distance')]):
            st.info(f"📈 Activity Summary: {fitness_data.get('steps', 0):,} steps • {fitness_data.get('total_calories', 0)} kcal • {fitness_data.get('distance', 0):.2f} km")
        
        st.markdown('</div>', unsafe_allow_html=True)

        # Health Analysis Section
        st.markdown('<div class="classic-container">', unsafe_allow_html=True)
        st.header("🏥 Health Analysis")
        
        fitness_level = health_analyzer.determine_fitness_level(
            fitness_data.get('steps'), 
            fitness_data.get('total_calories')
        )
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            insights = health_analyzer.generate_health_insights(fitness_data)
            st.subheader("Health Insights")
            for insight in insights:
                st.write(insight)
        
        with col2:
            st.subheader("Fitness Assessment")
            st.info(f"**{fitness_level.replace('_', ' ').title()}**")
            
            meditation_time = health_analyzer.calculate_meditation_time(
                fitness_data.get('steps'),
                fitness_data.get('total_calories'),
                fitness_data.get('stairs')
            )
            st.success(f"🧘‍♂️ Recommended meditation: **{meditation_time} minutes**")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Recommendations Section
        st.markdown('<div class="classic-container">', unsafe_allow_html=True)
        st.header("💡 Health Recommendations")
        
        tab1, tab2, tab3 = st.tabs(["🍎 Nutrition", "💪 Exercise", "📊 Progress"])
        
        with tab1:
            food_recs = health_analyzer.generate_food_recommendations(fitness_data)
            
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("🌅 Breakfast")
                for item in food_recs['breakfast']:
                    st.write(f"• {item}")
                
                st.subheader("🥪 Lunch")
                for item in food_recs['lunch']:
                    st.write(f"• {item}")
            
            with col2:
                st.subheader("🌙 Dinner")
                for item in food_recs['dinner']:
                    st.write(f"• {item}")
                
                st.subheader("🍎 Snacks")
                for item in food_recs['snacks']:
                    st.write(f"• {item}")
        
        with tab2:
            exercise_recs = health_analyzer.generate_exercise_recommendations(fitness_data)
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.subheader("❤️ Cardio")
                for exercise in exercise_recs['cardio']:
                    st.write(f"• {exercise}")
            
            with col2:
                st.subheader("💪 Strength")
                for exercise in exercise_recs['strength']:
                    st.write(f"• {exercise}")
            
            with col3:
                st.subheader("🤸‍♀️ Flexibility")
                for exercise in exercise_recs['flexibility']:
                    st.write(f"• {exercise}")
        
        with tab3:
            st.subheader("📊 Progress Visualization")
            
            # Create sample progress chart
            if fitness_data.get('steps'):
                fig, ax = plt.subplots(1, 1, figsize=(10, 6))
                
                categories = ['Steps', 'Calories', 'Distance']
                values = [
                    min(fitness_data.get('steps', 0) / 10000 * 100, 100),
                    min(fitness_data.get('total_calories', 0) / 500 * 100, 100),
                    min(fitness_data.get('distance', 0) / 5 * 100, 100)
                ]
                
                bars = ax.bar(categories, values, color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
                ax.set_ylabel('Progress (%)')
                ax.set_title('Daily Fitness Goals Progress')
                ax.set_ylim(0, 100)
                
                # Add value labels on bars
                for bar, value in zip(bars, values):
                    height = bar.get_height()
                    ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                           f'{value:.1f}%', ha='center', va='bottom')
                
                st.pyplot(fig)
        
        # AI-Powered Recommendations (if available)
        if ai_available and GEMINI_AVAILABLE:
            st.markdown('<div class="classic-container">', unsafe_allow_html=True)
            st.header("🤖 AI-Powered Personal Recommendations")
            
            ai_tab1, ai_tab2, ai_tab3 = st.tabs(["🥗 Meal Planning", "🏋️‍♂️ Workout Plan", "🩺 Health Analysis"])
            
            with ai_tab1:
                with st.spinner("Generating personalized meal recommendations..."):
                    ai_food_plan = generate_ai_food_plan(fitness_data)
                    if ai_food_plan and "Error" not in ai_food_plan:
                        st.markdown("### 🍽️ AI-Generated Personalized Meal Plan")
                        st.write(ai_food_plan)
                    else:
                        st.warning("Unable to generate meal recommendations.")
                        st.error(ai_food_plan if ai_food_plan else "Service unavailable")
            
            with ai_tab2:
                with st.spinner("Creating personalized workout plan..."):
                    ai_exercise_plan = generate_ai_exercise_plan(fitness_data)
                    if ai_exercise_plan and "Error" not in ai_exercise_plan:
                        st.markdown("### 💪 AI-Generated Custom Workout Plan")
                        st.write(ai_exercise_plan)
                    else:
                        st.warning("Unable to generate workout plan.")
                        st.error(ai_exercise_plan if ai_exercise_plan else "Service unavailable")
            
            with ai_tab3:
                with st.spinner("Analyzing health data with AI..."):
                    ai_health_insights = generate_ai_health_insights(fitness_data)
                    if ai_health_insights and "Error" not in ai_health_insights:
                        st.markdown("### 🩺 AI Health Analysis Report")
                        st.write(ai_health_insights)
                    else:
                        st.warning("Unable to generate health analysis.")
                        st.error(ai_health_insights if ai_health_insights else "Service unavailable")
            
            st.markdown('</div>', unsafe_allow_html=True)
    
    if __name__ == "__main__":
        main()
else:
    # Show error page if imports failed - define fallback values
    GEMINI_AVAILABLE = False
    GEMINI_API_KEY = "NOT_AVAILABLE"
    st.error("Application failed to start due to missing modules.")
    st.info("Please ensure all required files are present and try again.")
    
    # Add manual installation instructions
    st.markdown("""
    ### Manual Setup Instructions:
    
    1. **Install required packages:**
    ```bash
    pip install streamlit google-generativeai opencv-python pytesseract Pillow numpy pandas scikit-learn matplotlib seaborn
    ```
    
    2. **Create missing files:**
    - Create `image_processor.py` and `health_analyzer.py` in the same directory
    
    3. **Run the application:**
    ```bash
    streamlit run main.py
    ```
    """)
