import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os
from matplotlib.path import Path
import matplotlib.patheffects as PathEffects

def create_system_architecture_diagram():
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    plt.suptitle('AI Fitness Health Analyzer: System Architecture', fontsize=22, fontweight='bold', y=0.98)
    
    # Define colors
    colors = {
        'user': '#FFD8B1',
        'input': '#AADDFF',
        'processing': '#C3E6CB',
        'ai': '#D4C4FB',
        'output': '#FDCFE8',
        'storage': '#FFE082',
        'arrow': '#555555',
        'title': '#333333'
    }
    
    # Draw layers background
    layer_names = [
        'Data Acquisition Layer',
        'AI Vision Layer',
        'Data Processing Layer',
        'Analysis Layer',
        'Recommendation Layer'
    ]
    layer_colors = ['#F8F9FA', '#EFF8FF', '#F3FFF3', '#F8F0FF', '#FFF5F8']
    
    for i, (name, color) in enumerate(zip(layer_names, layer_colors)):
        y_pos = 8.5 - i * 1.6
        rect = patches.Rectangle((0.5, y_pos - 0.7), 11, 1.4, linewidth=1, 
                                 edgecolor='#CCCCCC', facecolor=color, alpha=0.5)
        ax.add_patch(rect)
        ax.text(0.7, y_pos + 0.5, name, fontsize=13, fontweight='bold', color=colors['title'])
    
    # User interaction
    user_circle = plt.Circle((2, 9.2), 0.4, color=colors['user'])
    ax.add_patch(user_circle)
    ax.text(2, 9.2, '👤', fontsize=20, ha='center', va='center')
    ax.text(2, 8.6, 'User', fontsize=12, ha='center', va='center', fontweight='bold')
    
    # Draw components
    
    # Layer 1: Data Acquisition
    upload_box = patches.FancyBboxPatch((3.5, 8.1), 1.5, 0.8, linewidth=1,
                                  edgecolor='#777777', facecolor=colors['input'], 
                                  boxstyle="round,pad=0.3", alpha=0.9)
    ax.add_patch(upload_box)
    ax.text(4.25, 8.5, 'Image Upload', fontsize=11, ha='center', va='center', fontweight='bold')
    
    storage_box = patches.FancyBboxPatch((6, 8.1), 1.5, 0.8, linewidth=1,
                                  edgecolor='#777777', facecolor=colors['storage'], 
                                  boxstyle="round,pad=0.3", alpha=0.9)
    ax.add_patch(storage_box)
    ax.text(6.75, 8.5, 'Temp Storage', fontsize=11, ha='center', va='center', fontweight='bold')
    
    preprocessing_box = patches.FancyBboxPatch((8.5, 8.1), 1.5, 0.8, linewidth=1,
                                  edgecolor='#777777', facecolor=colors['processing'], 
                                  boxstyle="round,pad=0.3", alpha=0.9)
    ax.add_patch(preprocessing_box)
    ax.text(9.25, 8.5, 'Preprocessing', fontsize=11, ha='center', va='center', fontweight='bold')
    
    # Layer 2: AI Vision Layer
    gemini_box = patches.FancyBboxPatch((3.5, 6.5), 2.0, 0.8, linewidth=1,
                                  edgecolor='#777777', facecolor=colors['ai'], 
                                  boxstyle="round,pad=0.3", alpha=0.9)
    ax.add_patch(gemini_box)
    ax.text(4.5, 6.9, 'Google Gemini AI', fontsize=11, ha='center', va='center', fontweight='bold')
    ax.text(4.5, 6.7, '(1.5-flash model)', fontsize=9, ha='center', va='center')
    
    ocr_box = patches.FancyBboxPatch((6.5, 6.5), 2.0, 0.8, linewidth=1,
                                  edgecolor='#777777', facecolor=colors['ai'], 
                                  boxstyle="round,pad=0.3", alpha=0.9)
    ax.add_patch(ocr_box)
    ax.text(7.5, 6.9, 'Text Extraction', fontsize=11, ha='center', va='center', fontweight='bold')
    ax.text(7.5, 6.7, '(OCR)', fontsize=9, ha='center', va='center')
    
    # Layer 3: Data Processing Layer
    pattern_box = patches.FancyBboxPatch((3.5, 4.9), 2.0, 0.8, linewidth=1,
                                  edgecolor='#777777', facecolor=colors['processing'], 
                                  boxstyle="round,pad=0.3", alpha=0.9)
    ax.add_patch(pattern_box)
    ax.text(4.5, 5.3, 'Pattern Recognition', fontsize=11, ha='center', va='center', fontweight='bold')
    
    metrics_box = patches.FancyBboxPatch((6.5, 4.9), 2.0, 0.8, linewidth=1,
                                  edgecolor='#777777', facecolor=colors['processing'], 
                                  boxstyle="round,pad=0.3", alpha=0.9)
    ax.add_patch(metrics_box)
    ax.text(7.5, 5.3, 'Metrics Extraction', fontsize=11, ha='center', va='center', fontweight='bold')
    
    validation_box = patches.FancyBboxPatch((9.5, 4.9), 1.5, 0.8, linewidth=1,
                                  edgecolor='#777777', facecolor=colors['processing'], 
                                  boxstyle="round,pad=0.3", alpha=0.9)
    ax.add_patch(validation_box)
    ax.text(10.25, 5.3, 'Validation', fontsize=11, ha='center', va='center', fontweight='bold')
    
    # Layer 4: Analysis Layer
    health_box = patches.FancyBboxPatch((3.5, 3.3), 2.0, 0.8, linewidth=1,
                                  edgecolor='#777777', facecolor=colors['ai'], 
                                  boxstyle="round,pad=0.3", alpha=0.9)
    ax.add_patch(health_box)
    ax.text(4.5, 3.7, 'Health Analysis', fontsize=11, ha='center', va='center', fontweight='bold')
    
    fitness_box = patches.FancyBboxPatch((6.5, 3.3), 2.0, 0.8, linewidth=1,
                                  edgecolor='#777777', facecolor=colors['ai'], 
                                  boxstyle="round,pad=0.3", alpha=0.9)
    ax.add_patch(fitness_box)
    ax.text(7.5, 3.7, 'Fitness Assessment', fontsize=11, ha='center', va='center', fontweight='bold')
    
    # Layer 5: Recommendation Layer
    meal_box = patches.FancyBboxPatch((2.5, 1.7), 1.8, 0.8, linewidth=1,
                                  edgecolor='#777777', facecolor=colors['output'], 
                                  boxstyle="round,pad=0.3", alpha=0.9)
    ax.add_patch(meal_box)
    ax.text(3.4, 2.1, 'Meal Plan', fontsize=11, ha='center', va='center', fontweight='bold')
    
    exercise_box = patches.FancyBboxPatch((5, 1.7), 1.8, 0.8, linewidth=1,
                                  edgecolor='#777777', facecolor=colors['output'], 
                                  boxstyle="round,pad=0.3", alpha=0.9)
    ax.add_patch(exercise_box)
    ax.text(5.9, 2.1, 'Exercise Plan', fontsize=11, ha='center', va='center', fontweight='bold')
    
    insight_box = patches.FancyBboxPatch((7.5, 1.7), 1.8, 0.8, linewidth=1,
                                  edgecolor='#777777', facecolor=colors['output'], 
                                  boxstyle="round,pad=0.3", alpha=0.9)
    ax.add_patch(insight_box)
    ax.text(8.4, 2.1, 'Health Insights', fontsize=11, ha='center', va='center', fontweight='bold')
    
    # User interface
    ui_box = patches.FancyBboxPatch((5, 0.5), 2, 0.8, linewidth=1,
                              edgecolor='#777777', facecolor='#D1ECFF', 
                              boxstyle="round,pad=0.3", alpha=0.9)
    ax.add_patch(ui_box)
    ax.text(6, 0.9, 'Streamlit Interface', fontsize=11, ha='center', va='center', fontweight='bold')
    
    # Draw arrows
    def draw_arrow(start, end, color='#555555', width=0.02, alpha=0.7):
        arrow = patches.FancyArrowPatch(start, end, arrowstyle='->', color=color, 
                                     connectionstyle='arc3,rad=0.1', linewidth=2, alpha=alpha)
        ax.add_patch(arrow)
    
    # Data flow arrows
    draw_arrow((2.4, 9.2), (3.5, 8.5))  # User to Upload
    draw_arrow((5, 8.5), (6, 8.5))      # Upload to Storage
    draw_arrow((7.5, 8.5), (8.5, 8.5))  # Storage to Preprocessing
    
    draw_arrow((9.25, 8.1), (7.5, 7.3))  # Preprocessing to OCR
    draw_arrow((9.25, 8.1), (4.5, 7.3))  # Preprocessing to Gemini
    
    draw_arrow((4.5, 6.5), (4.5, 5.7))  # Gemini to Pattern
    draw_arrow((7.5, 6.5), (7.5, 5.7))  # OCR to Metrics
    
    draw_arrow((4.5, 4.9), (4.5, 4.1))  # Pattern to Health
    draw_arrow((7.5, 4.9), (7.5, 4.1))  # Metrics to Fitness
    
    draw_arrow((4.5, 3.3), (3.4, 2.5))  # Health to Meal
    draw_arrow((4.5, 3.3), (5.9, 2.5))  # Health to Exercise
    draw_arrow((7.5, 3.3), (8.4, 2.5))  # Fitness to Insights
    
    draw_arrow((3.4, 1.7), (5.5, 1.3))  # Meal to UI
    draw_arrow((5.9, 1.7), (6, 1.3))    # Exercise to UI
    draw_arrow((8.4, 1.7), (6.5, 1.3))  # Insights to UI
    
    # Add code annotations
    code_box = patches.FancyBboxPatch((0.6, 0.5), 3.5, 2.5, linewidth=1,
                              edgecolor='#CCCCCC', facecolor='#F8F9FA', 
                              boxstyle="round,pad=0.3", alpha=0.9)
    ax.add_patch(code_box)
    
    code_text = """# Key components
gemini_model = genai.GenerativeModel('gemini-1.5-flash')

# Image analysis
response = gemini_model.generate_content([prompt, image])
extracted_text = response.text

# Pattern extraction
steps_match = re.search(r'steps[:\s]*(\d{1,5})', text)
if steps_match:
    steps_value = int(steps_match.group(1))"""
    
    ax.text(0.8, 1.8, code_text, fontsize=8, ha='left', va='center', family='monospace')
    ax.text(0.8, 2.8, 'Implementation Highlights:', fontsize=10, ha='left', va='center', fontweight='bold')
    
    # Add cloud deployment note
    cloud_box = patches.FancyBboxPatch((9.3, 0.5), 2, 1.2, linewidth=1,
                              edgecolor='#CCCCCC', facecolor='#F0F7FF', 
                              boxstyle="round,pad=0.3", alpha=0.9)
    ax.add_patch(cloud_box)
    
    ax.text(10.3, 1.2, 'Cloud Deployment', fontsize=10, ha='center', va='center', fontweight='bold')
    ax.text(10.3, 0.9, 'AWS ECS with Docker', fontsize=9, ha='center', va='center')
    ax.text(10.3, 0.7, 'Containerized Architecture', fontsize=9, ha='center', va='center')
    
    # Data extracted
    data_box = patches.FancyBboxPatch((2.2, 3.9), 0.8, 2.2, linewidth=1,
                              edgecolor='#CCCCCC', facecolor='#FFFDE7', 
                              boxstyle="round,pad=0.3", alpha=0.9)
    ax.add_patch(data_box)
    
    ax.text(2.6, 5.8, 'Extracted Data', fontsize=9, ha='center', va='center', fontweight='bold')
    ax.text(2.6, 5.5, '• Steps', fontsize=8, ha='center', va='center')
    ax.text(2.6, 5.3, '• Calories', fontsize=8, ha='center', va='center')
    ax.text(2.6, 5.1, '• Distance', fontsize=8, ha='center', va='center')
    ax.text(2.6, 4.9, '• Stairs', fontsize=8, ha='center', va='center')
    ax.text(2.6, 4.7, '• Move Goal', fontsize=8, ha='center', va='center')
    ax.text(2.6, 4.5, '• Progress', fontsize=8, ha='center', va='center')
    
    # Save the figure
    plt.tight_layout()
    output_path = os.path.join(os.path.dirname(__file__), 'system_architecture_diagram.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"System architecture diagram saved to: {output_path}")
    return output_path

if __name__ == "__main__":
    create_system_architecture_diagram()
