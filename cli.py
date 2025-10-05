#!/usr/bin/env python3
import os
import sys
import argparse
import json
from datetime import datetime
from dotenv import load_dotenv
from PIL import Image

# Load environment variables
load_dotenv()

# Import core functionality
from image_processor import extract_fitness_data_from_image, extract_from_image_path
from health_analyzer import analyze_health_metrics
from recommendations import generate_recommendations

def display_fitness_data(data):
    """Display extracted fitness data in a formatted way"""
    print("\n=== EXTRACTED FITNESS DATA ===")
    if not data:
        print("No fitness data could be extracted from the image.")
        return
    
    for key, value in data.items():
        print(f"{key.replace('_', ' ').title()}: {value}")

def display_analysis(analysis):
    """Display health analysis in a formatted way"""
    print("\n=== HEALTH ANALYSIS ===")
    
    for category, value in analysis.items():
        if category == "raw_data" or category in ["food_recommendations", "exercise_recommendations"]:
            continue
        elif category == "insights":
            print("\n--- Health Insights ---")
            for insight in value:
                print(f"• {insight}")
        else:
            print(f"{category.replace('_', ' ').title()}: {value}")

def display_recommendations(recommendations):
    """Display recommendations in a formatted way"""
    print("\n=== PERSONALIZED RECOMMENDATIONS ===")
    
    # Activity recommendations
    print("\n--- Activity Recommendations ---")
    activity_text = recommendations.get("activity", "No activity recommendations available.")
    # Extract the main recommendations (skip the header and sample plan)
    main_activity = activity_text.split("####")[0].strip()
    # Remove markdown formatting
    main_activity = main_activity.replace("###", "").replace("- ", "• ")
    print(main_activity)
    
    # Nutrition recommendations
    print("\n--- Nutrition Recommendations ---")
    nutrition_text = recommendations.get("nutrition", "No nutrition recommendations available.")
    main_nutrition = nutrition_text.split("####")[0].strip()
    main_nutrition = main_nutrition.replace("###", "").replace("- ", "• ")
    print(main_nutrition)
    
    # Wellness recommendations
    print("\n--- Wellness Recommendations ---")
    wellness_text = recommendations.get("wellness", "No wellness recommendations available.")
    main_wellness = wellness_text.split("####")[0].strip()
    main_wellness = main_wellness.replace("###", "").replace("- ", "• ")
    print(main_wellness)

def save_results(filename, fitness_data, analysis, recommendations):
    """Save results to a JSON file"""
    results = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "fitness_data": fitness_data,
        "analysis": analysis,
        "recommendations": recommendations
    }
    
    with open(filename, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\nResults saved to {filename}")

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='AI Fitness Health Analyzer CLI')
    parser.add_argument('image_path', help='Path to the fitness tracker image')
    parser.add_argument('--save', help='Save results to specified JSON file')
    args = parser.parse_args()
    
    # Check if Gemini API key is set
    if not os.environ.get("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY environment variable not set.")
        print("Please set it in a .env file or export it in your terminal.")
        sys.exit(1)
    
    # Check if the image file exists
    if not os.path.exists(args.image_path):
        print(f"Error: Image file not found: {args.image_path}")
        sys.exit(1)
    
    print(f"Processing image: {args.image_path}")
    print("This may take a moment...")
    
    # Extract fitness data from the image
    fitness_data = extract_from_image_path(args.image_path)
    
    # Display extracted data
    display_fitness_data(fitness_data)
    
    if not fitness_data:
        print("\nNo fitness data could be extracted. Please try another image.")
        sys.exit(1)
    
    # Analyze the data
    analysis = analyze_health_metrics(fitness_data)
    
    # Display analysis
    display_analysis(analysis)
    
    # Generate recommendations
    recommendations = generate_recommendations(analysis)
    
    # Display recommendations
    display_recommendations(recommendations)
    
    # Save results if requested
    if args.save:
        save_results(args.save, fitness_data, analysis, recommendations)

if __name__ == "__main__":
    main()
