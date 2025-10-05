class HealthAnalyzer:
    def __init__(self):
        """Initialize the health analyzer"""
        pass
    
    def determine_fitness_level(self, steps, calories):
        """Determine fitness level based on steps and calories"""
        if not steps:
            return "unknown"
        
        if steps >= 12000:
            return "very_active"
        elif steps >= 8000:
            return "active"
        elif steps >= 5000:
            return "moderately_active"
        elif steps >= 2500:
            return "lightly_active"
        else:
            return "sedentary"
    
    def generate_health_insights(self, fitness_data):
        """Generate health insights based on fitness data"""
        insights = []
        
        steps = fitness_data.get('steps', 0)
        calories = fitness_data.get('total_calories', 0) or fitness_data.get('calories', 0)
        distance = fitness_data.get('distance', 0)
        
        # Steps insights
        if steps >= 10000:
            insights.append("✅ Excellent! You've reached the recommended 10,000 daily steps.")
        elif steps >= 7500:
            insights.append("👍 Good job! You're close to the 10,000 step goal.")
        elif steps >= 5000:
            insights.append("🚶 Moderate activity level. Try to increase your daily steps.")
        elif steps > 0:
            insights.append("⚠️ Low activity level. Consider adding more walking to your routine.")
        
        # Calories insights
        if calories >= 400:
            insights.append("🔥 Great calorie burn! You're maintaining an active lifestyle.")
        elif calories >= 200:
            insights.append("💪 Good calorie burn. Keep up the activity!")
        elif calories > 0:
            insights.append("📈 Consider increasing your activity level to burn more calories.")
        
        # Distance insights
        if distance >= 5:
            insights.append(f"🏃 Impressive distance of {distance:.1f}km covered!")
        elif distance >= 2:
            insights.append(f"🚶 Good distance of {distance:.1f}km walked.")
        elif distance > 0:
            insights.append(f"🚶 You've covered {distance:.1f}km today.")
            
        return insights
    
    def calculate_meditation_time(self, fitness_data):
        """Calculate recommended meditation time based on activity"""
        base_time = 10
        
        steps = fitness_data.get('steps', 0)
        calories = fitness_data.get('total_calories', 0) or fitness_data.get('calories', 0)
        stairs = fitness_data.get('stairs', 0)
        
        if steps:
            if steps >= 10000:
                base_time += 5
            elif steps >= 5000:
                base_time += 3
        
        if calories:
            if calories >= 400:
                base_time += 5
            elif calories >= 200:
                base_time += 3
        
        return min(base_time, 20)  # Cap at 20 minutes
    
    def generate_food_recommendations(self, fitness_data):
        """Generate food recommendations based on fitness data"""
        steps = fitness_data.get('steps', 0)
        calories = fitness_data.get('total_calories', 0) or fitness_data.get('calories', 0)
        
        if steps >= 8000 or calories >= 300:
            # High activity recommendations
            return {
                'breakfast': [
                    "Protein smoothie with banana and berries",
                    "Whole grain toast with avocado and eggs",
                    "Greek yogurt with granola and nuts"
                ],
                'lunch': [
                    "Grilled chicken with quinoa and vegetables",
                    "Salmon salad with mixed greens",
                    "Turkey and hummus wrap"
                ],
                'dinner': [
                    "Lean beef with sweet potato and broccoli",
                    "Grilled fish with brown rice and asparagus",
                    "Chicken stir-fry with vegetables"
                ],
                'snacks': [
                    "Mixed nuts and dried fruit",
                    "Greek yogurt with berries",
                    "Apple with almond butter"
                ]
            }
        else:
            # Moderate activity recommendations
            return {
                'breakfast': [
                    "Oatmeal with fresh berries",
                    "Whole grain cereal with milk",
                    "Scrambled eggs with vegetables"
                ],
                'lunch': [
                    "Grilled chicken salad",
                    "Vegetable soup with whole grain bread",
                    "Tuna sandwich on whole wheat"
                ],
                'dinner': [
                    "Baked chicken with roasted vegetables",
                    "Fish with steamed broccoli and rice",
                    "Vegetable pasta with lean protein"
                ],
                'snacks': [
                    "Fresh fruit",
                    "Vegetable sticks with hummus",
                    "Low-fat yogurt"
                ]
            }
    
    def generate_exercise_recommendations(self, fitness_data):
        """Generate exercise recommendations based on fitness data"""
        steps = fitness_data.get('steps', 0)
        
        if steps >= 8000:
            # High activity - maintain and enhance
            return {
                'cardio': [
                    "30-minute moderate run",
                    "45-minute cycling session",
                    "HIIT workout (20 minutes)"
                ],
                'strength': [
                    "Full body weight training",
                    "Resistance band exercises",
                    "Bodyweight circuit training"
                ],
                'flexibility': [
                    "30-minute yoga session",
                    "Dynamic stretching routine",
                    "Pilates core workout"
                ]
            }
        else:
            # Low to moderate activity - build up gradually
            return {
                'cardio': [
                    "20-minute brisk walk",
                    "15-minute light cycling",
                    "Swimming for 20 minutes"
                ],
                'strength': [
                    "Basic bodyweight exercises",
                    "Light dumbbell workout",
                    "Wall push-ups and squats"
                ],
                'flexibility': [
                    "Gentle stretching routine",
                    "Beginner yoga poses",
                    "Simple mobility exercises"
                ]
            }

# Legacy function to maintain compatibility with existing code
def analyze_health_metrics(fitness_data):
    """
    Analyze fitness metrics and categorize them into different health levels.
    
    Args:
        fitness_data (dict): Dictionary containing fitness metrics
    
    Returns:
        dict: Dictionary with analysis results
    """
    analyzer = HealthAnalyzer()
    
    analysis_results = {
        "activity_level": "Unknown",
        "calorie_burn": "Unknown",
        "fitness_score": 0,
        "raw_data": fitness_data
    }
    
    # Get steps and calories, accounting for different possible key names
    steps = fitness_data.get("steps", 0)
    calories = fitness_data.get("calories", 0) or fitness_data.get("total_calories", 0)
    
    # Generate insights
    insights = analyzer.generate_health_insights(fitness_data)
    analysis_results["insights"] = insights
    
    # Add meditation recommendation
    meditation_time = analyzer.calculate_meditation_time(fitness_data)
    analysis_results["meditation_time"] = meditation_time
    
    # Analyze step count
    if steps > 0:
        if steps < 5000:
            analysis_results["activity_level"] = "Sedentary"
        elif 5000 <= steps < 7500:
            analysis_results["activity_level"] = "Low Active"
        elif 7500 <= steps < 10000:
            analysis_results["activity_level"] = "Somewhat Active"
        elif 10000 <= steps < 12500:
            analysis_results["activity_level"] = "Active"
        else:
            analysis_results["activity_level"] = "Very Active"
    
    # Analyze calorie burn
    if calories > 0:
        if calories < 200:
            analysis_results["calorie_burn"] = "Low"
        elif 200 <= calories < 400:
            analysis_results["calorie_burn"] = "Moderate"
        elif 400 <= calories < 600:
            analysis_results["calorie_burn"] = "High"
        else:
            analysis_results["calorie_burn"] = "Very High"
    
    # Calculate fitness score (a simple metric between 0-100)
    fitness_score = 0
    
    # Score based on steps
    if steps > 0:
        step_score = min(steps / 15000 * 40, 40)  # 40% weight, max at 15000 steps
        fitness_score += step_score
    
    # Score based on calories
    if calories > 0:
        calorie_score = min(calories / 600 * 30, 30)  # 30% weight, max at 600 calories
        fitness_score += calorie_score
    
    # Score based on active minutes
    if "active_minutes" in fitness_data:
        active_minutes = fitness_data["active_minutes"]
        active_score = min(active_minutes / 60 * 20, 20)  # 20% weight, max at 60 minutes
        fitness_score += active_score
    
    # Score based on distance
    if "distance" in fitness_data:
        distance = fitness_data["distance"]
        distance_score = min(distance / 10 * 10, 10)  # 10% weight, max at 10 miles/km
        fitness_score += distance_score
    
    analysis_results["fitness_score"] = round(fitness_score)
    
    # Determine overall fitness level
    if fitness_score < 20:
        analysis_results["overall_fitness"] = "Needs Improvement"
    elif 20 <= fitness_score < 40:
        analysis_results["overall_fitness"] = "Fair"
    elif 40 <= fitness_score < 60:
        analysis_results["overall_fitness"] = "Good"
    elif 60 <= fitness_score < 80:
        analysis_results["overall_fitness"] = "Very Good"
    else:
        analysis_results["overall_fitness"] = "Excellent"
    
    # Add food recommendations
    food_recommendations = analyzer.generate_food_recommendations(fitness_data)
    analysis_results["food_recommendations"] = food_recommendations
    
    # Add exercise recommendations
    exercise_recommendations = analyzer.generate_exercise_recommendations(fitness_data)
    analysis_results["exercise_recommendations"] = exercise_recommendations
    
    return analysis_results

def get_health_trends(historical_data):
    """
    Analyze trends in fitness data over time.
    
    Args:
        historical_data (list): List of fitness data dictionaries
    
    Returns:
        dict: Dictionary with trend analysis
    """
    if not historical_data or len(historical_data) < 2:
        return {"message": "Not enough data to analyze trends"}
    
    # Extract metrics for trend analysis
    trends = {}
    
    # Common metrics to track
    metrics = ["steps", "calories", "total_calories", "distance", "active_minutes"]
    
    for metric in metrics:
        values = [entry.get(metric) for entry in historical_data if metric in entry and entry[metric] is not None]
        if len(values) >= 2:
            current = values[-1]
            previous = values[-2]
            change = current - previous
            percent_change = (change / previous) * 100 if previous != 0 else 0
            
            trends[metric] = {
                "current": current,
                "previous": previous,
                "change": change,
                "percent_change": round(percent_change, 2),
                "direction": "up" if change > 0 else "down" if change < 0 else "stable"
            }
    
    return trends
