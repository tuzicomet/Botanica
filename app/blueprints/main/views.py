"""
    blueprints/main/views.py

    This file contains view functions for rendering HTML templates.
    
    Author: Leonard Lau
    Last Updated: 10/01/2023
"""

from flask import render_template

# Define view functions for the 'main' blueprint

def render_home_page():
    """
    Render the home page.

    Returns:
        rendered_template: Rendered HTML template for the home page.
    """
    return render_template('pages/index.html')

def render_login_page():
    """
    Render the login page.

    Returns:
        rendered_template: Rendered HTML template for the login page.
    """
    return render_template('pages/login.html')

def render_forum_page():
    """
    Render the forum page.

    Returns:
        rendered_template: Rendered HTML template for the forum page.
    """
    return render_template('pages/forum.html')

def render_marketplace_page():
    """
    Render the marketplace page.

    Returns:
        rendered_template: Rendered HTML template for the marketplace page.
    """
    return render_template('pages/marketplace.html')

# Add more view functions as needed