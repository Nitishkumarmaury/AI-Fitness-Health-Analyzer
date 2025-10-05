#!/usr/bin/env python3
import os
import sys
import traceback
import logging
from flask import Flask, request, jsonify, send_from_directory, abort
from flask_cors import CORS
from dotenv import load_dotenv
from PIL import Image
import io
import json
from datetime import datetime
import sqlite3
from werkzeug.utils import secure_filename

# Import core functionality
from image_processor import extract_fitness_data_from_image
from health_analyzer import analyze_health_metrics
from recommendations import generate_recommendations

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Check if API key is available
if not os.environ.get("GEMINI_API_KEY"):
    logger.error("GEMINI_API_KEY is not set.")
    print("Error: GEMINI_API_KEY is not set.")
    print("Please add it to your .env file or set it as an environment variable.")
    sys.exit(1)

# Initialize Flask app
app = Flask(__name__, static_folder='frontend/build')
CORS(app)  # Enable CORS for all routes

# Configure upload folder for temporary image storage
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'temp_uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit uploads to 16MB

# Initialize database
def init_db():
    conn = sqlite3.connect('/tmp/fitness_analyzer.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        fitness_data TEXT NOT NULL,
        analysis_results TEXT NOT NULL,
        recommendations TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()
    logger.info("Database initialized")


@app.route('/api/analyze', methods=['POST'])
def analyze_image():
    """API endpoint to analyze fitness image"""
    logger.info("Received image analysis request")
    if 'image' not in request.files:
        logger.warning("No image provided in request")
        return jsonify({'error': 'No image provided'}), 400
    
    file = request.files['image']
    if file.filename == '':
        logger.warning("Empty filename in request")
        return jsonify({'error': 'No image selected'}), 400
    
    try:
        # Check file extension
        filename = secure_filename(file.filename.lower())
        if not any(filename.endswith(ext) for ext in ['.png', '.jpg', '.jpeg']):
            logger.warning(f"Unsupported file format: {filename}")
            return jsonify({'error': 'Unsupported file format. Please use JPG or PNG images'}), 400
            
        # Save file temporarily
        temp_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(temp_path)
        logger.info(f"Image saved temporarily as {temp_path}")
        
        # Open and process the image
        try:
            image = Image.open(temp_path)
            
            # Check image dimensions
            if max(image.size) < 200:
                logger.warning(f"Image too small: {image.size}")
                return jsonify({'error': 'Image is too small. Please upload a larger image with clear text.'}), 400
            
            logger.info(f"Processing image of size {image.size}")
        except Exception as e:
            logger.error(f"Error opening image: {str(e)}")
            return jsonify({'error': f'Invalid image file: {str(e)}'}), 400
        
        # Extract fitness data
        logger.info("Extracting fitness data...")
        fitness_data = extract_fitness_data_from_image(image)
        
        # Clean up temporary file
        try:
            os.remove(temp_path)
            logger.info(f"Removed temporary file {temp_path}")
        except Exception as e:
            logger.warning(f"Failed to remove temporary file: {str(e)}")
        
        if not fitness_data:
            logger.warning("No fitness data extracted from image")
            return jsonify({
                'error': 'Could not extract fitness data from the image. Please try a clearer image showing fitness metrics.'
            }), 400
        
        # Analyze the data
        logger.info("Analyzing fitness data...")
        analysis_results = analyze_health_metrics(fitness_data)
        
        # Generate recommendations
        logger.info("Generating recommendations...")
        recommendations = generate_recommendations(analysis_results)
        
        # Create entry
        entry = {
            "date": datetime.now().isoformat(),
            "fitness_data": fitness_data,
            "analysis_results": analysis_results,
            "recommendations": recommendations
        }
        
        
        # Return the results
        logger.info("Analysis completed successfully")
        return jsonify({
            'fitness_data': fitness_data,
            'analysis_results': analysis_results,
            'recommendations': recommendations
        }), 200
        
    except Exception as e:
        logger.error(f"Error in image analysis: {str(e)}")
        logger.error(traceback.format_exc())
        return jsonify({'error': f'Error analyzing image: {str(e)}'}), 500



# Serve static files from React build
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    logger.debug(f"Serving path: {path}")
    # Check if path is an API route - don't try to serve static files for API routes
    if path.startswith('api/'):
        return jsonify({'error': 'Not Found'}), 404
        
    # If the path exists as a file in the static folder, serve it
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    
    # Otherwise, serve index.html to let React Router handle the route
    return send_from_directory(app.static_folder, 'index.html')

# Error handlers
@app.errorhandler(404)
def not_found(e):
    logger.warning(f"404 error: {request.path}")
    if request.path.startswith('/api/'):
        return jsonify({"error": "API endpoint not found"}), 404
    return send_from_directory(app.static_folder, 'index.html')

@app.errorhandler(500)
def server_error(e):
    logger.error(f"500 error: {str(e)}")
    return jsonify({"error": "Internal server error occurred"}), 500

def main():
    """Run the Flask API server"""
    # Initialize the database
    init_db()

if __name__ == "__main__":
    sys.exit(main())
