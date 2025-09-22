import os
import sys
import json
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from datetime import datetime
from PIL import Image, ImageTk
from dotenv import load_dotenv
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading

# Load environment variables
load_dotenv()

# Import core functionality
from image_processor import extract_fitness_data_from_image
from health_analyzer import analyze_health_metrics
from recommendations import generate_recommendations

class FitnessAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Fitness Health Analyzer")
        self.root.geometry("1000x800")
        self.root.minsize(800, 600)
        
        # Check for API key
        if not os.environ.get("GEMINI_API_KEY"):
            messagebox.showerror("API Key Missing", 
                                "GEMINI_API_KEY environment variable not set.\n"
                                "Please set it in a .env file or as an environment variable.")
            root.destroy()
            return
        
        # State variables
        self.current_image = None
        self.fitness_data = None
        self.analysis_results = None
        self.recommendations = None
        self.history = []
        
        # Create the main UI
        self.create_ui()
    
    def create_ui(self):
        # Create a notebook (tabbed interface)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create tabs
        self.upload_tab = ttk.Frame(self.notebook)
        self.dashboard_tab = ttk.Frame(self.notebook)
        self.history_tab = ttk.Frame(self.notebook)
        self.about_tab = ttk.Frame(self.notebook)
        
        self.notebook.add(self.upload_tab, text="Upload Image")
        self.notebook.add(self.dashboard_tab, text="Dashboard")
        self.notebook.add(self.history_tab, text="History")
        self.notebook.add(self.about_tab, text="About")
        
        # Setup each tab
        self.setup_upload_tab()
        self.setup_dashboard_tab()
        self.setup_history_tab()
        self.setup_about_tab()
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        self.status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def setup_upload_tab(self):
        # Create a frame for the upload section
        upload_frame = ttk.LabelFrame(self.upload_tab, text="Upload Fitness Data Image")
        upload_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Button to browse for an image
        self.browse_button = ttk.Button(upload_frame, text="Browse for Image", command=self.browse_image)
        self.browse_button.pack(pady=20)
        
        # Label to show selected file
        self.file_label = ttk.Label(upload_frame, text="No file selected")
        self.file_label.pack(pady=5)
        
        # Frame for the image preview
        self.preview_frame = ttk.LabelFrame(upload_frame, text="Image Preview")
        self.preview_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Label to show the image
        self.image_label = ttk.Label(self.preview_frame)
        self.image_label.pack(fill=tk.BOTH, expand=True)
        
        # Analyze button
        self.analyze_button = ttk.Button(upload_frame, text="Analyze Image", 
                                         command=self.analyze_image, state=tk.DISABLED)
        self.analyze_button.pack(pady=20)
        
        # Processing indicator
        self.progress_var = tk.IntVar()
        self.progress = ttk.Progressbar(upload_frame, variable=self.progress_var, 
                                        maximum=100, mode='indeterminate')
    
    def setup_dashboard_tab(self):
        # Main frame
        dashboard_frame = ttk.Frame(self.dashboard_tab)
        dashboard_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Split into two columns
        left_frame = ttk.Frame(dashboard_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        right_frame = ttk.Frame(dashboard_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Fitness metrics section
        self.metrics_frame = ttk.LabelFrame(left_frame, text="Your Fitness Metrics")
        self.metrics_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Health analysis section
        self.analysis_frame = ttk.LabelFrame(right_frame, text="Health Analysis")
        self.analysis_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Visualization section
        self.viz_frame = ttk.LabelFrame(left_frame, text="Data Visualization")
        self.viz_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Recommendations section with tabs
        self.rec_frame = ttk.LabelFrame(dashboard_frame, text="Personalized Recommendations")
        self.rec_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create recommendation tabs
        self.rec_notebook = ttk.Notebook(self.rec_frame)
        self.rec_notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.activity_tab = ttk.Frame(self.rec_notebook)
        self.nutrition_tab = ttk.Frame(self.rec_notebook)
        self.wellness_tab = ttk.Frame(self.rec_notebook)
        
        self.rec_notebook.add(self.activity_tab, text="Activity")
        self.rec_notebook.add(self.nutrition_tab, text="Nutrition")
        self.rec_notebook.add(self.wellness_tab, text="Wellness")
        
        # Text widgets for recommendations
        self.activity_text = scrolledtext.ScrolledText(self.activity_tab, wrap=tk.WORD)
        self.activity_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.nutrition_text = scrolledtext.ScrolledText(self.nutrition_tab, wrap=tk.WORD)
        self.nutrition_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.wellness_text = scrolledtext.ScrolledText(self.wellness_tab, wrap=tk.WORD)
        self.wellness_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Initial message
        initial_message = "No data to display. Please upload and analyze an image first."
        ttk.Label(self.metrics_frame, text=initial_message).pack(pady=20)
        ttk.Label(self.analysis_frame, text=initial_message).pack(pady=20)
        ttk.Label(self.viz_frame, text=initial_message).pack(pady=20)
    
    def setup_history_tab(self):
        # Main frame
        history_frame = ttk.Frame(self.history_tab)
        history_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Label
        ttk.Label(history_frame, text="Your Analysis History").pack(pady=10)
        
        # Create a canvas with scrollbar for the history items
        self.history_canvas = tk.Canvas(history_frame)
        scrollbar = ttk.Scrollbar(history_frame, orient="vertical", command=self.history_canvas.yview)
        self.scrollable_history_frame = ttk.Frame(self.history_canvas)
        
        self.scrollable_history_frame.bind(
            "<Configure>",
            lambda e: self.history_canvas.configure(
                scrollregion=self.history_canvas.bbox("all")
            )
        )
        
        self.history_canvas.create_window((0, 0), window=self.scrollable_history_frame, anchor="nw")
        self.history_canvas.configure(yscrollcommand=scrollbar.set)
        
        self.history_canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Initial message
        self.history_message = ttk.Label(self.scrollable_history_frame, 
                                         text="No history available. Start by analyzing a fitness image.")
        self.history_message.pack(pady=20)
    
    def setup_about_tab(self):
        # Main frame
        about_frame = ttk.Frame(self.about_tab)
        about_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # About text
        about_text = scrolledtext.ScrolledText(about_frame, wrap=tk.WORD)
        about_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Insert about information
        about_text.insert(tk.END, "AI Fitness Health Analyzer\n\n", "title")
        about_text.insert(tk.END, "How It Works\n\n", "heading")
        about_text.insert(tk.END, "The AI Fitness Health Analyzer uses Google's Gemini 1.5-flash AI model to:\n\n")
        about_text.insert(tk.END, "1. Extract Data: Convert fitness tracker screenshots into structured data\n")
        about_text.insert(tk.END, "2. Analyze Metrics: Interpret your activity levels based on scientific guidelines\n")
        about_text.insert(tk.END, "3. Generate Insights: Provide personalized recommendations for your health journey\n\n")
        about_text.insert(tk.END, "Privacy Notice\n\n", "heading")
        about_text.insert(tk.END, "Your uploaded images are processed securely and not stored permanently. We value your privacy and data security.\n\n")
        about_text.insert(tk.END, "Contact\n\n", "heading")
        about_text.insert(tk.END, "For questions or feedback, please contact support@aifitnesshealthanalyzer.com\n\n")
        about_text.insert(tk.END, "© 2023 AI Fitness Health Analyzer | Powered by Google Gemini AI", "footer")
        
        # Configure text tags
        about_text.tag_configure("title", font=("Arial", 16, "bold"))
        about_text.tag_configure("heading", font=("Arial", 12, "bold"))
        about_text.tag_configure("footer", font=("Arial", 8))
        
        # Make it read-only
        about_text.configure(state="disabled")
    
    def browse_image(self):
        """Open file dialog to select an image"""
        filetypes = [
            ("Image files", "*.jpg *.jpeg *.png"),
            ("JPEG files", "*.jpg *.jpeg"),
            ("PNG files", "*.png"),
            ("All files", "*.*")
        ]
        
        filename = filedialog.askopenfilename(title="Select Image File", filetypes=filetypes)
        
        if filename:
            try:
                # Open and display the image
                self.current_image = Image.open(filename)
                self.display_image(self.current_image)
                
                # Update UI
                self.file_label.config(text=os.path.basename(filename))
                self.analyze_button.config(state=tk.NORMAL)
                self.status_var.set(f"Image loaded: {os.path.basename(filename)}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not open image file: {str(e)}")
                self.status_var.set("Error loading image")
    
    def display_image(self, image):
        """Display the image in the preview area"""
        # Resize image for display if needed
        max_width = self.preview_frame.winfo_width() or 400
        max_height = self.preview_frame.winfo_height() or 300
        
        # Make a copy to avoid modifying the original
        display_image = image.copy()
        display_image.thumbnail((max_width, max_height))
        
        # Convert to PhotoImage for Tkinter
        photo = ImageTk.PhotoImage(display_image)
        
        # Update the image label
        self.image_label.config(image=photo)
        self.image_label.image = photo  # Keep a reference to prevent garbage collection
    
    def analyze_image(self):
        """Process the image in a separate thread to keep UI responsive"""
        if not self.current_image:
            messagebox.showwarning("Warning", "Please select an image first.")
            return
        
        # Start progress bar
        self.progress.pack(fill=tk.X, pady=5)
        self.progress.start(10)
        self.analyze_button.config(state=tk.DISABLED)
        self.status_var.set("Analyzing image...")
        
        # Start analysis in a new thread
        thread = threading.Thread(target=self.run_analysis)
        thread.daemon = True
        thread.start()
    
    def run_analysis(self):
        """Run the analysis in a background thread"""
        try:
            # Extract data
            self.fitness_data = extract_fitness_data_from_image(self.current_image)
            
            if not self.fitness_data:
                # Show error on the main thread
                self.root.after(0, lambda: messagebox.showerror("Error", 
                                "Could not extract fitness data from the image. Please try another image."))
                self.root.after(0, self.cleanup_progress)
                return
            
            # Analyze the data
            self.analysis_results = analyze_health_metrics(self.fitness_data)
            
            # Generate recommendations
            self.recommendations = generate_recommendations(self.analysis_results)
            
            # Add to history
            self.add_to_history()
            
            # Update the UI on the main thread
            self.root.after(0, self.update_dashboard)
            self.root.after(0, self.cleanup_progress)
            self.root.after(0, lambda: self.notebook.select(self.dashboard_tab))
            
        except Exception as e:
            # Show error on the main thread
            self.root.after(0, lambda: messagebox.showerror("Error", f"An error occurred: {str(e)}"))
            self.root.after(0, self.cleanup_progress)
    
    def cleanup_progress(self):
        """Stop and hide the progress bar"""
        self.progress.stop()
        self.progress.pack_forget()
        self.analyze_button.config(state=tk.NORMAL)
        self.status_var.set("Analysis complete")
    
    def update_dashboard(self):
        """Update the dashboard with the analysis results"""
        if not self.fitness_data or not self.analysis_results or not self.recommendations:
            return
        
        # Clear previous content
        for widget in self.metrics_frame.winfo_children():
            widget.destroy()
        
        for widget in self.analysis_frame.winfo_children():
            widget.destroy()
        
        for widget in self.viz_frame.winfo_children():
            widget.destroy()
        
        # Update metrics
        for i, (key, value) in enumerate(self.fitness_data.items()):
            ttk.Label(self.metrics_frame, text=f"{key.replace('_', ' ').title()}:").grid(
                row=i, column=0, sticky="w", padx=10, pady=5)
            ttk.Label(self.metrics_frame, text=str(value)).grid(
                row=i, column=1, sticky="w", padx=10, pady=5)
        
        # Update analysis
        for i, (key, value) in enumerate(self.analysis_results.items()):
            if key != "raw_data" and key not in ["food_recommendations", "exercise_recommendations"]:
                if key == "insights":
                    # Handle insights specially
                    ttk.Label(self.analysis_frame, text="Health Insights:").grid(
                        row=i, column=0, sticky="nw", padx=10, pady=5)
                    
                    insights_frame = ttk.Frame(self.analysis_frame)
                    insights_frame.grid(row=i, column=1, sticky="w", padx=10, pady=5)
                    
                    for j, insight in enumerate(value):
                        ttk.Label(insights_frame, text=f"• {insight}").grid(
                            row=j, column=0, sticky="w", pady=2)
                else:
                    ttk.Label(self.analysis_frame, text=f"{key.replace('_', ' ').title()}:").grid(
                        row=i, column=0, sticky="w", padx=10, pady=5)
                    ttk.Label(self.analysis_frame, text=str(value)).grid(
                        row=i, column=1, sticky="w", padx=10, pady=5)
        
        # Update recommendations
        self.activity_text.delete(1.0, tk.END)
        self.activity_text.insert(tk.END, self.recommendations.get("activity", "No recommendations available"))
        
        self.nutrition_text.delete(1.0, tk.END)
        self.nutrition_text.insert(tk.END, self.recommendations.get("nutrition", "No recommendations available"))
        
        self.wellness_text.delete(1.0, tk.END)
        self.wellness_text.insert(tk.END, self.recommendations.get("wellness", "No recommendations available"))
        
        # Create visualization
        self.create_visualization()
    
    def create_visualization(self):
        """Create a bar chart of the fitness metrics"""
        try:
            # Get numeric metrics
            metrics_to_plot = {k: v for k, v in self.fitness_data.items() 
                               if isinstance(v, (int, float))}
            
            if not metrics_to_plot:
                ttk.Label(self.viz_frame, text="No numeric data to visualize").pack(pady=20)
                return
            
            # Create the figure
            fig, ax = plt.subplots(figsize=(5, 4))
            ax.bar(metrics_to_plot.keys(), metrics_to_plot.values())
            ax.set_title("Your Fitness Metrics")
            ax.set_ylabel("Value")
            ax.set_xlabel("Metric")
            
            # Rotate x-axis labels for readability
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            
            # Add the plot to the GUI
            canvas = FigureCanvasTkAgg(fig, master=self.viz_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            
        except Exception as e:
            ttk.Label(self.viz_frame, text=f"Error creating visualization: {str(e)}").pack(pady=20)
    
    def add_to_history(self):
        """Add the current analysis to history"""
        if not self.fitness_data or not self.analysis_results or not self.recommendations:
            return
        
        # Create history entry
        entry = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "fitness_data": self.fitness_data,
            "analysis_results": self.analysis_results,
            "recommendations": self.recommendations
        }
        
        # Add to history list
        self.history.append(entry)
        
        # Update history tab
        self.update_history_tab()
    
    def update_history_tab(self):
        """Update the history tab with the latest entries"""
        # Clear previous content
        for widget in self.scrollable_history_frame.winfo_children():
            widget.destroy()
        
        if not self.history:
            self.history_message = ttk.Label(self.scrollable_history_frame, 
                                            text="No history available. Start by analyzing a fitness image.")
            self.history_message.pack(pady=20)
            return
        
        # Add each history entry
        for i, entry in enumerate(reversed(self.history)):
            frame = ttk.LabelFrame(self.scrollable_history_frame, text=f"Analysis from {entry['date']}")
            frame.pack(fill=tk.X, expand=True, padx=10, pady=5)
            
            # Fitness data section
            ttk.Label(frame, text="Fitness Data", font=("Arial", 10, "bold")).grid(
                row=0, column=0, sticky="w", padx=10, pady=5)
            
            data_text = ""
            for key, value in entry["fitness_data"].items():
                data_text += f"{key.title()}: {value}\n"
            
            data_label = ttk.Label(frame, text=data_text)
            data_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
            
            # Analysis section
            ttk.Label(frame, text="Analysis Results", font=("Arial", 10, "bold")).grid(
                row=0, column=1, sticky="w", padx=10, pady=5)
            
            analysis_text = ""
            for key, value in entry["analysis_results"].items():
                if key != "raw_data" and key not in ["food_recommendations", "exercise_recommendations", "insights"]:
                    analysis_text += f"{key.replace('_', ' ').title()}: {value}\n"
            
            analysis_label = ttk.Label(frame, text=analysis_text)
            analysis_label.grid(row=1, column=1, sticky="w", padx=10, pady=5)
            
            # Button to view full details
            view_button = ttk.Button(frame, text="View Full Details", 
                                     command=lambda e=entry: self.view_history_entry(e))
            view_button.grid(row=2, column=0, columnspan=2, pady=10)
    
    def view_history_entry(self, entry):
        """Show a popup with full details of a history entry"""
        dialog = tk.Toplevel(self.root)
        dialog.title(f"Analysis from {entry['date']}")
        dialog.geometry("800x600")
        dialog.minsize(600, 400)
        
        # Create a notebook for the details
        notebook = ttk.Notebook(dialog)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Data tab
        data_frame = ttk.Frame(notebook)
        notebook.add(data_frame, text="Fitness Data")
        
        data_text = scrolledtext.ScrolledText(data_frame, wrap=tk.WORD)
        data_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        for key, value in entry["fitness_data"].items():
            data_text.insert(tk.END, f"{key.replace('_', ' ').title()}: {value}\n")
        
        # Analysis tab
        analysis_frame = ttk.Frame(notebook)
        notebook.add(analysis_frame, text="Analysis")
        
        analysis_text = scrolledtext.ScrolledText(analysis_frame, wrap=tk.WORD)
        analysis_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        for key, value in entry["analysis_results"].items():
            if key != "raw_data" and key not in ["food_recommendations", "exercise_recommendations"]:
                if key == "insights":
                    analysis_text.insert(tk.END, "Health Insights:\n")
                    for insight in value:
                        analysis_text.insert(tk.END, f"• {insight}\n")
                    analysis_text.insert(tk.END, "\n")
                else:
                    analysis_text.insert(tk.END, f"{key.replace('_', ' ').title()}: {value}\n")
        
        # Recommendations tab
        rec_frame = ttk.Frame(notebook)
        notebook.add(rec_frame, text="Recommendations")
        
        rec_text = scrolledtext.ScrolledText(rec_frame, wrap=tk.WORD)
        rec_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        for category, text in entry["recommendations"].items():
            rec_text.insert(tk.END, f"--- {category.title()} ---\n\n")
            rec_text.insert(tk.END, f"{text}\n\n")
        
        # Close button
        ttk.Button(dialog, text="Close", command=dialog.destroy).pack(pady=10)

def main():
    # Check if Gemini API key is set
    if not os.environ.get("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY environment variable not set.")
        print("Please set it in a .env file or export it in your terminal.")
        sys.exit(1)
    
    # Create and run the app
    root = tk.Tk()
    app = FitnessAnalyzerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
