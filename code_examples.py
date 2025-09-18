"""
Key Code Examples from the AI Fitness Health Analyzer

This file contains important code snippets that demonstrate the core functionality
of the AI Fitness Health Analyzer project for inclusion in the research paper.
"""

# 1. AI Vision Integration with Google Gemini
def analyze_image_with_gemini(image_path):
    """Analyze image using Google Gemini Vision with enhanced fitness data extraction"""
    try:
        # Load and process image
        image = PILImage.open(image_path)
        
        # Extract text from image using Gemini Vision with specific fitness focus
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
        
        # Send image to Gemini for analysis
        response = gemini_model.generate_content([prompt, image])
        extracted_text = response.text if response.text else ""
        
        # Extract fitness metrics from the detected text
        fitness_metrics = extract_fitness_from_text([extracted_text])
        
        return {'text': [extracted_text], 'fitness_data': fitness_metrics}
    except Exception as e:
        return f"Gemini Analysis Error: {e}"

# 2. Pattern-Based Fitness Metric Extraction
def extract_fitness_from_text(text_lines):
    """Extract fitness metrics from detected text with improved patterns"""
    import re
    
    fitness_data = {}
    full_text = " ".join(text_lines).lower() if text_lines else ""
    
    # Steps extraction patterns
    steps_patterns = [
        r'\*?\*?steps\*?\*?[:\s]*(\d{1,3}),(\d{3})',  # "**Steps:** 4,889" with comma
        r'\*?\*?steps\*?\*?[:\s]*(\d{1,5})',  # "**Steps:** 4889" without comma
        r'steps[:\s]*(\d{1,3}),(\d{3})',  # "steps: 4,889"
        r'steps[:\s]*(\d{1,5})',  # "steps: 4889"
        r'(\d{1,5})\s*steps?',  # "4889 steps"
    ]
    
    for pattern in steps_patterns:
        steps_match = re.search(pattern, full_text)
        if steps_match:
            if len(steps_match.groups()) == 2 and steps_match.group(2):  # Format with comma like "4,889"
                steps_value = int(steps_match.group(1) + steps_match.group(2))
            else:
                steps_value = int(steps_match.group(1))
            
            # Validate reasonable step count
            if 500 <= steps_value <= 50000:
                fitness_data['steps'] = steps_value
                break
    
    # Similar pattern matching for other metrics
    # ...existing code...
    
    return fitness_data

# 3. AI-Generated Personalized Recommendations
def generate_ai_food_plan(fitness_data):
    """Generate AI food recommendations using Google Gemini"""
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

# 4. Fitness Assessment Algorithm
def determine_fitness_level(steps, calories):
    """Determine fitness level based on steps and calories burned"""
    fitness_level = "moderate"
    
    if steps is not None and steps > 0:
        if steps < 3000:
            fitness_level = "sedentary"
        elif steps < 7500:
            fitness_level = "lightly_active"
        elif steps < 10000:
            fitness_level = "moderately_active"
        else:
            fitness_level = "very_active"
    
    # Adjust based on calories if available
    if calories is not None and calories > 0:
        if calories < 1000:
            # Slight downgrade if low calories
            if fitness_level == "moderately_active":
                fitness_level = "lightly_active"
            elif fitness_level == "very_active":
                fitness_level = "moderately_active"
        elif calories > 2000:
            # Slight upgrade if high calories
            if fitness_level == "lightly_active":
                fitness_level = "moderately_active"
            elif fitness_level == "moderately_active":
                fitness_level = "very_active"
    
    return fitness_level

# 5. Visualization of Fitness Metrics
def create_fitness_dashboard(fitness_data):
    """Create visualization dashboard of fitness metrics"""
    import matplotlib.pyplot as plt
    import seaborn as sns
    
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
    
    return fig

# 6. System Initialization and API Connection
def initialize_ai_service():
    """Initialize the AI service and test connection"""
    try:
        import google.generativeai as genai
        from PIL import Image as PILImage
        
        # Configure Gemini API
        genai.configure(api_key=GEMINI_API_KEY)
        gemini_model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Test the connection
        response = gemini_model.generate_content("Say 'Google Gemini API working!'")
        if response.text:
            return True, gemini_model
        else:
            return False, None
            
    except Exception as e:
        return False, f"AI service initialization failed: {e}"