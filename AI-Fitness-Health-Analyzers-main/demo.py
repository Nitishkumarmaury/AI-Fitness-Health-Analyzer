import os
import argparse
from dotenv import load_dotenv
from PIL import Image
import logging
from image_processor import extract_fitness_data_from_image, extract_from_image_path
from health_analyzer import analyze_health_metrics
from recommendations import generate_recommendations

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    # Load environment variables
    load_dotenv()
    
    # Check for API key
    if not os.environ.get("GEMINI_API_KEY"):
        logger.error("GEMINI_API_KEY not found in environment variables")
        print("Error: Please set the GEMINI_API_KEY environment variable")
        return
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Test fitness data extraction from an image')
    parser.add_argument('image_path', help='Path to the fitness tracker image')
    args = parser.parse_args()
    
    # Check if file exists
    if not os.path.exists(args.image_path):
        logger.error(f"Image file not found: {args.image_path}")
        print(f"Error: Image file not found: {args.image_path}")
        return
    
    # Process the image
    print(f"Processing image: {args.image_path}")
    try:
        # Extract fitness data
        fitness_data = extract_from_image_path(args.image_path)
        
        if fitness_data:
            print("\n--- Extracted Fitness Data ---")
            for key, value in fitness_data.items():
                print(f"{key}: {value}")
            
            # Analyze data
            analysis = analyze_health_metrics(fitness_data)
            print("\n--- Health Analysis ---")
            for key, value in analysis.items():
                if key != "raw_data":
                    print(f"{key.replace('_', ' ').title()}: {value}")
            
            # Generate recommendations
            recs = generate_recommendations(analysis)
            print("\n--- Recommendations Summary ---")
            for category, text in recs.items():
                summary = text.split('\n')[0] if text else "No recommendations"
                print(f"{category.title()}: {summary}")
                
            return True
        else:
            print("No fitness data could be extracted from the image.")
            print("Try using an image with clearly visible fitness metrics.")
            return False
            
    except Exception as e:
        logger.error(f"Error processing image: {e}")
        print(f"Error: {str(e)}")
        return False

if __name__ == "__main__":
    main()
