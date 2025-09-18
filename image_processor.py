import cv2
import pytesseract
from PIL import Image
import numpy as np
import re

class ImageProcessor:
    def __init__(self):
        """Initialize the image processor"""
        # Set tesseract path if needed (Windows)
        try:
            # Try to find tesseract automatically
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        except:
            # If not found, try default
            pass
    
    def extract_text(self, image_path):
        """Extract text from image using OCR"""
        try:
            # Load image
            image = cv2.imread(image_path)
            
            # Preprocess image for better OCR
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            # Apply thresholding to get better text extraction
            _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            
            # Use pytesseract to extract text
            text = pytesseract.image_to_string(thresh, config='--psm 6')
            
            return text
            
        except Exception as e:
            print(f"OCR Error: {e}")
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
            r'\*?\*?stairs climbed\*?\*?[:\s]*(\d+)',
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
