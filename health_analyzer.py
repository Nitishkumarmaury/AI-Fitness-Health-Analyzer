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
        calories = fitness_data.get('total_calories', 0)
        distance = fitness_data.get('distance', 0)
        
        # Steps insights
        if steps >= 10000:
            insights.append("✅ Excellent! You've reached the recommended 10,000 daily steps.")
        elif steps >= 7500:
            insights.append("👍 Good job! You're close to the 10,000 step goal.")
        elif steps >= 5000:
            insights.append("🚶 Moderate activity level. Try to increase your daily steps.")
        else:
            insights.append("⚠️ Low activity level. Consider adding more walking to your routine.")
        
        # Calories insights
        if calories >= 400:
            insights.append("🔥 Great calorie burn! You're maintaining an active lifestyle.")
        elif calories >= 200:
            insights.append("💪 Good calorie burn. Keep up the activity!")
        else:
            insights.append("📈 Consider increasing your activity level to burn more calories.")
        
        # Distance insights
        if distance >= 5:
            insights.append(f"🏃 Impressive distance of {distance:.1f}km covered!")
        elif distance >= 2:
            insights.append(f"🚶 Good distance of {distance:.1f}km walked.")
        
        return insights
    
    def calculate_meditation_time(self, steps, calories, stairs):
        """Calculate recommended meditation time based on activity"""
        base_time = 10
        
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
        calories = fitness_data.get('total_calories', 0)
        
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
