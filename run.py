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
    conn = sqlite3.connect('fitness_analyzer.db')
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

# Get history from database
def get_history_from_db():
    try:
        conn = sqlite3.connect('fitness_analyzer.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, date, fitness_data, analysis_results, recommendations FROM history ORDER BY id DESC')
        rows = cursor.fetchall()
        history_items = []
        for row in rows:
            history_items.append({
                "id": row[0],
                "date": row[1],
                "fitness_data": json.loads(row[2]),
                "analysis_results": json.loads(row[3]),
                "recommendations": json.loads(row[4])
            })
        conn.close()
        return history_items
    except Exception as e:
        logger.error(f"Error retrieving history: {str(e)}")
        return []

# Add entry to database
def add_entry_to_db(entry):
    try:
        conn = sqlite3.connect('fitness_analyzer.db')
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO history (date, fitness_data, analysis_results, recommendations) VALUES (?, ?, ?, ?)',
            (
                entry["date"],
                json.dumps(entry["fitness_data"]),
                json.dumps(entry["analysis_results"]),
                json.dumps(entry["recommendations"])
            )
        )
        entry_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return entry_id
    except Exception as e:
        logger.error(f"Error adding entry to database: {str(e)}")
        return None

# Get entry from database
def get_entry_from_db(entry_id):
    try:
        conn = sqlite3.connect('fitness_analyzer.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, date, fitness_data, analysis_results, recommendations FROM history WHERE id = ?', (entry_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return {
                "id": row[0],
                "date": row[1],
                "fitness_data": json.loads(row[2]),
                "analysis_results": json.loads(row[3]),
                "recommendations": json.loads(row[4])
            }
        return None
    except Exception as e:
        logger.error(f"Error retrieving entry from database: {str(e)}")
        return None

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
        
        # Add to database
        logger.info("Adding entry to database...")
        entry_id = add_entry_to_db(entry)
        if entry_id:
            entry["id"] = entry_id
        else:
            logger.error("Failed to add entry to database")
            return jsonify({'error': 'Failed to save analysis results'}), 500
        
        # Return the results
        logger.info(f"Analysis completed successfully for entry {entry_id}")
        return jsonify({
            'fitness_data': fitness_data,
            'analysis_results': analysis_results,
            'recommendations': recommendations,
            'id': entry_id
        }), 200
        
    except Exception as e:
        logger.error(f"Error in image analysis: {str(e)}")
        logger.error(traceback.format_exc())
        return jsonify({'error': f'Error analyzing image: {str(e)}'}), 500

@app.route('/api/history', methods=['GET'])
def get_history():
    """API endpoint to retrieve analysis history"""
    logger.info("Retrieving analysis history")
    history = get_history_from_db()
    return jsonify(history), 200

@app.route('/api/history/<int:entry_id>', methods=['GET'])
def get_history_entry(entry_id):
    """API endpoint to retrieve a specific history entry"""
    logger.info(f"Retrieving history entry {entry_id}")
    entry = get_entry_from_db(entry_id)
    if entry:
        return jsonify(entry), 200
    logger.warning(f"Entry not found: {entry_id}")
    return jsonify({'error': 'Entry not found'}), 404

@app.route('/api/metrics/summary', methods=['GET'])
def get_metrics_summary():
    """API endpoint to get summary statistics of user metrics"""
    logger.info("Retrieving metrics summary")
    try:
        history = get_history_from_db()
        if not history:
            return jsonify({"message": "No data available yet"}), 200
        
        # Extract metrics for analysis
        steps_data = []
        calories_data = []
        distance_data = []
        
        for entry in history:
            fitness_data = entry["fitness_data"]
            if "steps" in fitness_data:
                steps_data.append({"date": entry["date"], "value": fitness_data["steps"]})
            
            calories = fitness_data.get("calories") or fitness_data.get("total_calories")
            if calories:
                calories_data.append({"date": entry["date"], "value": calories})
            
            if "distance" in fitness_data:
                distance_data.append({"date": entry["date"], "value": fitness_data["distance"]})
        
        return jsonify({
            "steps": steps_data,
            "calories": calories_data,
            "distance": distance_data
        }), 200
    except Exception as e:
        logger.error(f"Error generating metrics summary: {str(e)}")
        return jsonify({'error': 'Failed to generate metrics summary'}), 500

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
    
    # Make sure the React build folder exists
    if not os.path.exists(app.static_folder):
        logger.error(f"React build folder not found at {app.static_folder}")
        print(f"Error: React build folder not found at {app.static_folder}")
        print("Please run 'npm run build' in the frontend directory first.")
        return 1
        
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() in ('true', '1', 't')
    
    logger.info(f"Starting server on http://localhost:{port} (debug={debug})")
    print(f"Starting server on http://localhost:{port}")
    
    app.run(host='0.0.0.0', port=port, debug=debug)
    return 0

if __name__ == "__main__":
    sys.exit(main())
