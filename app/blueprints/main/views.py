"""
    blueprints/main/views.py

    This file contains the route definitions for the main blueprint.
    
    Author: Leonard Lau
    Last Updated: 9/01/2023
"""

# Define view functions for the 'main' blueprint

def render_home_page():
    # Render the home page
    return render_template('pages/index.html')

def render_login_page():
    # Render the login page
    return render_template('pages/login.html')

def render_forum_page():
    # Render the forum page
    return render_template('pages/forum.html')

def render_marketplace_page():
    # Render the marketplace page
    return render_template('pages/marketplace.html')

# Add more view functions as needed