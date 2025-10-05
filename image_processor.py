import os
import io
import base64
from PIL import Image
import google.generativeai as genai
import re
import json
import logging
import traceback

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Configure the Gemini API
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# Try to import OpenCV and pytesseract for OCR fallback
try:
    import cv2
    import pytesseract
    import numpy as np
    OCR_AVAILABLE = True
    # Try to find tesseract automatically (for Windows)
    if os.name == 'nt':
        if os.path.exists(r'C:\Program Files\Tesseract-OCR\tesseract.exe'):
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        elif os.path.exists(r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'):
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
except ImportError:
    OCR_AVAILABLE = False
    logger.warning("OpenCV or pytesseract not available. OCR fallback will not be used.")


class ImageProcessor:
    def __init__(self):
        """Initialize the image processor"""
        self.ocr_available = OCR_AVAILABLE
    
    def extract_text(self, image):
        """Extract text from image using OCR"""
        if not self.ocr_available:
            return "OCR not available. Please install opencv-python and pytesseract."
        
        try:
            # Convert PIL Image to OpenCV format
            if isinstance(image, str):
                # If image is a file path
                cv_image = cv2.imread(image)
            else:
                # If image is a PIL Image
                cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            
            # Preprocess image for better OCR
            gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
            
            # Apply thresholding to get better text extraction
            _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            
            # Use pytesseract to extract text
            text = pytesseract.image_to_string(thresh, config='--psm 6')
            
            return text
            
        except Exception as e:
            logger.error(f"OCR Error: {e}")
            return f"Error extracting text: {e}"
    
    def parse_fitness_data(self, text):
        """Parse fitness data from extracted text"""
        fitness_data = {}
        
        if not text:
            return fitness_data
        
        text_lower = text.lower()
        
        # Extract steps with comma support
        steps_patterns = [
            r'\*?\*?steps\*?\*?[:\s]*(\d{1,3}),(\d{3})',  # "**Steps:** 4,889"
            r'\*?\*?steps\*?\*?[:\s]*(\d{1,5})',  # "**Steps:** 4889"
            r'(\d{1,5})\s*steps?',
            r'steps[:\s]*(\d{1,5})',
        ]
        
        for pattern in steps_patterns:
            match = re.search(pattern, text_lower)
            if match:
                if len(match.groups()) == 2 and match.group(2):
                    steps = int(match.group(1) + match.group(2))
                else:
                    steps = int(match.group(1))
                
                if 100 <= steps <= 50000:
                    fitness_data['steps'] = steps
                    break
        
        # Extract total calories with comma support
        total_cal_patterns = [
            r'total calories burned[:\s]*(\d{1,3}),(\d{3})\s*kcal',
            r'total calories burned[:\s]*(\d{1,5})',
            r'(\d{1,4})\s*kcal',
            r'calories[:\s]*(\d{1,4})',
        ]
        
        for pattern in total_cal_patterns:
            match = re.search(pattern, text_lower)
            if match:
                if len(match.groups()) == 2 and match.group(2):
                    calories = int(match.group(1) + match.group(2))
                else:
                    calories = int(match.group(1))
                
                if 50 <= calories <= 5000:
                    fitness_data['total_calories'] = calories
                    break
        
        # Extract distance
        dist_patterns = [
            r'(\d+\.?\d*)\s*km',
            r'distance[:\s]*(\d+\.?\d*)',
        ]
        
        for pattern in dist_patterns:
            match = re.search(pattern, text_lower)
            if match:
                distance = float(match.group(1))
                if 0.1 <= distance <= 100:
                    fitness_data['distance'] = distance
                    break
        
        # Extract stairs
        stairs_patterns = [
            r'\*?\*?stairs climbed\*?\*?[:\s]*(\d+)',  # "**Stairs Climbed:** 10"
            r'(\d+)\s*(?:stairs?|floors?|flights?)',
            r'(?:stairs?|floors?)[:\s]*(\d+)',
        ]
        
        for pattern in stairs_patterns:
            match = re.search(pattern, text_lower)
            if match:
                stairs = int(match.group(1))
                if 1 <= stairs <= 500:
                    fitness_data['stairs'] = stairs
                    break
        
        # Extract move goal and progress
        move_patterns = [
            r'move[:\s]*(\d+)[/\\](\d+)\s*kcal',
            r'(\d+)[/\\](\d+)\s*kcal',
        ]
        
        for pattern in move_patterns:
            match = re.search(pattern, text_lower)
            if match:
                fitness_data['move_progress'] = int(match.group(1))
                fitness_data['move_goal'] = int(match.group(2))
                break
        
        return fitness_data
    
    def extract_fitness_data_from_image_ocr(self, image):
        """
        Extract fitness data from image using OCR as a fallback method
        
        Args:
            image (PIL.Image or str): Image object or path
            
        Returns:
            dict: Extracted fitness data
        """
        if not self.ocr_available:
            logger.warning("OCR not available for fallback extraction")
            return None
            
        try:
            # Extract text from image
            text = self.extract_text(image)
            logger.info(f"OCR extracted text: {text[:100]}...")
            
            # Parse fitness data from text
            fitness_data = self.parse_fitness_data(text)
            
            if fitness_data:
                logger.info(f"OCR extracted fitness data: {fitness_data}")
                return fitness_data
            else:
                logger.warning("OCR could not extract any fitness data")
                return None
                
        except Exception as e:
            logger.error(f"OCR extraction error: {e}")
            logger.error(traceback.format_exc())
            return None


def extract_fitness_data_from_image(image):
    """
    Extract fitness data from an image using Google's Gemini AI with OCR fallback.
    
    Args:
        image (PIL.Image): The image containing fitness data
    
    Returns:
        dict: A dictionary of extracted fitness metrics
    """
    try:
        # Convert PIL image to bytes for Gemini API
        img_byte_arr = io.BytesIO()
        
        # Ensure image has a format, default to JPEG if not specified
        img_format = image.format if image.format else 'JPEG'
        
        # Save with appropriate format and quality
        image.save(img_byte_arr, format=img_format, quality=95)
        img_byte_arr = img_byte_arr.getvalue()
        
        logger.info(f"Image converted to bytes, size: {len(img_byte_arr)} bytes, format: {img_format}")
        
        # Debug: Check if image data is valid
        if len(img_byte_arr) < 100:
            logger.error(f"Image data too small, possibly corrupted: {len(img_byte_arr)} bytes")
            return None
        
        # Set up the Gemini model
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Create the prompt for Gemini
        prompt = """
        Extract fitness data from this image. Look for numerical values of metrics such as:
        - Steps
        - Calories burned
        - Distance (miles/km)
        - Active minutes
        - Heart rate
        - Sleep duration
        - Exercise duration
        
        Format the response as a JSON object with the metrics as keys and values as numbers.
        Only include metrics that are clearly visible in the image.
        Example: {"steps": 8500, "calories": 2100, "distance": 5.2}
        
        If you cannot extract any fitness metrics from the image, respond with {"error": "No fitness data found in image"}
        """
        
        # Generate content with the image
        logger.info("Sending request to Gemini API...")
        response = model.generate_content([prompt, img_byte_arr], timeout=30)
        
        # Extract the JSON from the response
        response_text = response.text
        logger.info(f"Received response from Gemini API: {response_text[:100]}...")
        
        # Find JSON in the response (it might be embedded in markdown code blocks)
        json_match = re.search(r'```json\s*(.*?)\s*```', response_text, re.DOTALL)
        if json_match:
            json_str = json_match.group(1)
            logger.info("Found JSON in code block")
        else:
            # Try to find a regular JSON object
            json_match = re.search(r'({.*})', response_text, re.DOTALL)
            if json_match:
                json_str = json_match.group(1)
                logger.info("Found JSON in plain text")
            else:
                logger.warning("Could not find JSON in response, using full response")
                json_str = response_text
        
        # Clean up the string and parse the JSON
        json_str = json_str.strip()
        logger.info(f"Parsed JSON string: {json_str}")
        
        try:
            data = json.loads(json_str)
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON: {e}")
            logger.error(f"Raw JSON string: {json_str}")
            
            # Try OCR fallback
            logger.info("Attempting OCR fallback extraction...")
            ocr_processor = ImageProcessor()
            return ocr_processor.extract_fitness_data_from_image_ocr(image)
        
        # Check if the response indicates no fitness data was found
        if "error" in data:
            logger.warning(f"Gemini API reported: {data['error']}")
            
            # Try OCR fallback
            logger.info("Attempting OCR fallback extraction...")
            ocr_processor = ImageProcessor()
            ocr_data = ocr_processor.extract_fitness_data_from_image_ocr(image)
            if ocr_data:
                return ocr_data
            return None
            
        # Convert string numbers to integers or floats where appropriate
        for key, value in data.items():
            if isinstance(value, str):
                try:
                    # Try to convert to int first, then float if that fails
                    try:
                        data[key] = int(value)
                    except ValueError:
                        # Try to handle values with commas like "1,234"
                        cleaned_value = value.replace(',', '')
                        data[key] = int(cleaned_value) if cleaned_value.isdigit() else float(cleaned_value)
                except ValueError:
                    # Keep as string if conversion fails
                    pass
        
        # Validate that we have at least some fitness metrics
        if not validate_fitness_data(data):
            logger.warning("Extracted data doesn't contain essential fitness metrics")
            
            # Try OCR fallback
            logger.info("Attempting OCR fallback extraction...")
            ocr_processor = ImageProcessor()
            ocr_data = ocr_processor.extract_fitness_data_from_image_ocr(image)
            if ocr_data:
                return ocr_data
            return None
            
        logger.info(f"Successfully extracted fitness data: {data}")
        return data
    
    except Exception as e:
        logger.error(f"Error extracting fitness data: {str(e)}")
        logger.error(traceback.format_exc())
        
        # Try OCR fallback
        try:
            logger.info("Attempting OCR fallback extraction after error...")
            ocr_processor = ImageProcessor()
            return ocr_processor.extract_fitness_data_from_image_ocr(image)
        except Exception as ocr_e:
            logger.error(f"OCR fallback also failed: {str(ocr_e)}")
            return None

def validate_fitness_data(data):
    """
    Validate the extracted fitness data to ensure it contains the required metrics.
    
    Args:
        data (dict): The extracted fitness data
    
    Returns:
        bool: True if valid, False otherwise
    """
    # Check if we have at least some basic metrics
    common_metrics = ['steps', 'calories', 'total_calories', 'distance', 'active_minutes', 
                      'heart_rate', 'sleep', 'exercise', 'activity']
    
    # Consider valid if at least one common fitness metric is present
    has_metrics = any(metric in data.keys() for metric in common_metrics)
    
    # Or if data contains any keys with numeric values
    has_numeric = any(isinstance(value, (int, float)) for value in data.values())
    
    return has_metrics and has_numeric

def extract_from_image_path(image_path):
    """
    Helper function to extract data from an image file path
    
    Args:
        image_path (str): Path to the image file
        
    Returns:
        dict: Extracted fitness data or None if extraction fails
    """
    try:
        with Image.open(image_path) as img:
            return extract_fitness_data_from_image(img)
    except Exception as e:
        logger.error(f"Error opening image file {image_path}: {e}")
        return None
