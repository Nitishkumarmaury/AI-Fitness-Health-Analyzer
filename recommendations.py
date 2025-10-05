from health_analyzer import HealthAnalyzer

def generate_recommendations(analysis_results):
    """
    Generate personalized health recommendations based on analysis results.
    
    Args:
        analysis_results (dict): Dictionary containing analyzed health metrics
    
    Returns:
        dict: Dictionary with personalized recommendations
    """
    analyzer = HealthAnalyzer()
    recommendations = {
        "activity": "",
        "nutrition": "",
        "wellness": ""
    }
    
    # Get the activity level and fitness score
    activity_level = analysis_results.get("activity_level", "Unknown")
    calorie_burn = analysis_results.get("calorie_burn", "Unknown")
    fitness_score = analysis_results.get("fitness_score", 0)
    overall_fitness = analysis_results.get("overall_fitness", "Unknown")
    
    # Get insights
    insights = analysis_results.get("insights", [])
    meditation_time = analysis_results.get("meditation_time", 10)
    
    # Activity recommendations based on activity level
    if activity_level == "Sedentary":
        recommendations["activity"] = """
### Activity Recommendations
- Start with a goal of 5,000 steps per day
- Take short 5-10 minute walks throughout the day
- Try gentle activities like yoga or swimming
- Consider using a standing desk for part of your workday
- Set a reminder to move for 5 minutes every hour
        """
    elif activity_level == "Low Active":
        recommendations["activity"] = """
### Activity Recommendations
- Aim to increase your daily steps to 7,500
- Add a 20-minute brisk walk to your daily routine
- Try bodyweight exercises like squats and push-ups
- Consider joining a fitness class once a week
- Take the stairs instead of elevators when possible
        """
    elif activity_level == "Somewhat Active":
        recommendations["activity"] = """
### Activity Recommendations
- Push toward the 10,000 steps per day milestone
- Incorporate 30 minutes of moderate exercise 5 days a week
- Add strength training 2-3 times per week
- Try interval training to boost cardiovascular fitness
- Consider weekend hikes or longer recreational activities
        """
    elif activity_level == "Active":
        recommendations["activity"] = """
### Activity Recommendations
- Maintain your excellent activity level of 10,000+ steps
- Add variety to your routine with different exercise modalities
- Consider training for a 5K or 10K event
- Incorporate active recovery days with light activity
- Try more challenging strength training or HIIT workouts
        """
    elif activity_level == "Very Active":
        recommendations["activity"] = """
### Activity Recommendations
- Your activity level is exceptional - focus on quality and recovery
- Consider periodization in your training to prevent plateaus
- Add flexibility and mobility work to prevent injuries
- Try new challenging activities like rock climbing or martial arts
- Consider training for a half-marathon or other endurance event
        """
    else:
        recommendations["activity"] = """
### Activity Recommendations
- Aim for at least 30 minutes of moderate activity daily
- Try to accumulate 150 minutes of exercise per week
- Include both cardio and strength training in your routine
- Take regular breaks from sitting throughout the day
- Find activities you enjoy to make exercise sustainable
        """
    
    # Nutrition recommendations based on calorie burn
    if calorie_burn == "Low":
        recommendations["nutrition"] = """
### Nutrition Recommendations
- Focus on nutrient-dense, lower-calorie foods
- Ensure adequate protein intake (0.8g per kg of body weight)
- Include plenty of vegetables and fruits for essential nutrients
- Consider intermittent fasting or time-restricted eating
- Stay hydrated with at least 8 glasses of water daily
        """
    elif calorie_burn == "Moderate":
        recommendations["nutrition"] = """
### Nutrition Recommendations
- Balance your macronutrients (protein, carbs, and fats)
- Eat regular meals to maintain energy throughout the day
- Include complex carbohydrates for sustained energy
- Ensure adequate protein for muscle recovery
- Consider a pre-workout snack for energy during exercise
        """
    elif calorie_burn == "High" or calorie_burn == "Very High":
        recommendations["nutrition"] = """
### Nutrition Recommendations
- Increase caloric intake to match your high activity level
- Focus on post-workout nutrition for recovery
- Include carbohydrates to replenish glycogen stores
- Ensure higher protein intake (1.2-1.6g per kg of body weight)
- Include healthy fats for sustained energy
- Stay extra hydrated and consider electrolyte replacement
        """
    else:
        recommendations["nutrition"] = """
### Nutrition Recommendations
- Eat a balanced diet with plenty of whole foods
- Include protein with each meal for satiety and muscle health
- Choose complex carbohydrates over simple sugars
- Include healthy fats like avocados, nuts, and olive oil
- Stay hydrated and limit sugary beverages
        """
    
    # Wellness recommendations based on overall fitness
    if overall_fitness == "Needs Improvement" or overall_fitness == "Fair":
        recommendations["wellness"] = f"""
### Wellness Recommendations
- Focus on consistency rather than intensity
- Celebrate small victories and progress
- Prioritize sleep with a regular 7-8 hour schedule
- We recommend {meditation_time} minutes of meditation daily to manage stress
- Find an accountability partner or group for motivation
- Consider working with a fitness professional to create a personalized plan
        """
    elif overall_fitness == "Good":
        recommendations["wellness"] = f"""
### Wellness Recommendations
- Add variety to your routine to prevent plateaus
- Focus on quality sleep and recovery
- Practice mindfulness or meditation for {meditation_time} minutes daily
- Track your progress to stay motivated
- Set specific, measurable goals for the next month
        """
    elif overall_fitness == "Very Good" or overall_fitness == "Excellent":
        recommendations["wellness"] = f"""
### Wellness Recommendations
- Focus on recovery and preventing overtraining
- Consider advanced recovery techniques like contrast therapy
- Optimize sleep quality with a consistent schedule
- Practice mindfulness and meditation for {meditation_time} minutes daily
- Set challenging but realistic goals for continued improvement
- Consider helping others by sharing your fitness journey
        """
    else:
        recommendations["wellness"] = f"""
### Wellness Recommendations
- Prioritize 7-9 hours of quality sleep
- Practice stress management through meditation ({meditation_time} min/day) or deep breathing
- Take rest days for proper recovery
- Stay socially connected for mental well-being
- Set realistic, achievable health goals
        """
    
    # Add health insights if available
    if insights:
        recommendations["wellness"] = recommendations["wellness"] + "\n\n### Health Insights\n" + "\n".join([f"- {insight}" for insight in insights])
    
    # Add a sample meal plan based on calorie burn and food recommendations
    if "food_recommendations" in analysis_results:
        food_recs = analysis_results["food_recommendations"]
        recommendations["nutrition"] += """
        
#### Sample Meal Plan
- **Breakfast**: """ + food_recs["breakfast"][0] + """
- **Lunch**: """ + food_recs["lunch"][0] + """
- **Dinner**: """ + food_recs["dinner"][0] + """
- **Snacks**: """ + food_recs["snacks"][0]
    else:
        # Add a sample meal plan based on calorie burn
        if calorie_burn == "Low":
            recommendations["nutrition"] += """
            
#### Sample Meal Plan (Low Calorie Burn)
- **Breakfast**: Greek yogurt with berries and a sprinkle of granola
- **Lunch**: Large salad with lean protein and light dressing
- **Dinner**: Baked fish with roasted vegetables
- **Snacks**: Apple slices with a small amount of nut butter
            """
        elif calorie_burn == "Moderate":
            recommendations["nutrition"] += """
            
#### Sample Meal Plan (Moderate Calorie Burn)
- **Breakfast**: Oatmeal with fruit, nuts, and a scoop of protein powder
- **Lunch**: Whole grain wrap with lean protein, veggies, and hummus
- **Dinner**: Stir-fry with lean meat or tofu, plenty of vegetables, and brown rice
- **Snacks**: Greek yogurt with honey, handful of nuts and seeds
            """
        elif calorie_burn == "High" or calorie_burn == "Very High":
            recommendations["nutrition"] += """
            
#### Sample Meal Plan (High Calorie Burn)
- **Breakfast**: Eggs with whole grain toast, avocado, and fruit
- **Lunch**: Hearty grain bowl with quinoa, beans, vegetables, and a protein source
- **Dinner**: Lean protein with sweet potato, vegetables, and healthy fats
- **Snacks**: Protein smoothie, trail mix, banana with nut butter
- **Post-workout**: Protein shake with fruit and a source of carbohydrates
            """
    
    # Add a weekly exercise plan based on activity level and exercise recommendations
    if "exercise_recommendations" in analysis_results:
        ex_recs = analysis_results["exercise_recommendations"]
        recommendations["activity"] += """
        
#### Sample Weekly Exercise Plan
- **Monday**: """ + ex_recs["cardio"][0] + """
- **Tuesday**: """ + ex_recs["strength"][0] + """
- **Wednesday**: Active recovery or """ + ex_recs["flexibility"][0] + """
- **Thursday**: """ + ex_recs["strength"][1] + """
- **Friday**: """ + ex_recs["cardio"][1] + """
- **Weekend**: One longer workout and one recovery day
        """
    else:
        # Add a weekly exercise plan based on activity level
        if activity_level == "Sedentary" or activity_level == "Low Active":
            recommendations["activity"] += """
            
#### Sample Weekly Exercise Plan (Beginner)
- **Monday**: 15-minute walk
- **Tuesday**: 10 minutes of basic stretching
- **Wednesday**: 15-minute walk
- **Thursday**: Rest or gentle yoga
- **Friday**: 20-minute walk
- **Weekend**: One 30-minute recreational activity like swimming or cycling
            """
        elif activity_level == "Somewhat Active":
            recommendations["activity"] += """
            
#### Sample Weekly Exercise Plan (Intermediate)
- **Monday**: 30-minute brisk walk or jog
- **Tuesday**: Basic strength training (bodyweight exercises)
- **Wednesday**: 30-minute cardio of choice
- **Thursday**: Yoga or flexibility training
- **Friday**: 30-minute interval training
- **Weekend**: One longer (45-60 min) recreational activity
            """
        elif activity_level == "Active" or activity_level == "Very Active":
            recommendations["activity"] += """
            
#### Sample Weekly Exercise Plan (Advanced)
- **Monday**: 45-minute run or high-intensity cardio
- **Tuesday**: Strength training focusing on upper body
- **Wednesday**: 45-minute interval training or cross-training
- **Thursday**: Strength training focusing on lower body
- **Friday**: 30-minute recovery cardio and mobility work
- **Weekend**: One challenging workout (long run, hike, cycling) and one active recovery day
            """
    
    return recommendations
