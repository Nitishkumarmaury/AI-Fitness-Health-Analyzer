"""
WSGI configuration for AI Fitness Health Analyzer.
This file is used for production deployment with WSGI servers like Gunicorn.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from run import app

if __name__ == "__main__":
    app.run()
