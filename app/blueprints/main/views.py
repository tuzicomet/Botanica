"""
    blueprints/main/views.py

    This file contains the route definitions for the main blueprint.
    
    Author: Leonard Lau
    Last Updated: 9/01/2023
"""

from flask import render_template
from . import main_bp

# Define view functions for the 'main' blueprint

def render_home_page():
    # Render the home page
    return render_template('pages/index.html')

# Add more view functions as needed