"""
    blueprints/main/routes.py

    This file defines the routes specific to the 'main' blueprint,
    handling the main pages and functionalities of the Botanica web application.

    Author: Leonard Lau
    Last Updated: 10/01/2024
"""

from . import main_bp
from .views import *

# Define routes for the 'main' blueprint
# (define routes for pages using this blueprint)

@main_bp.route('/', endpoint='home')
def home():
    """
    Define a route for the home page.

    NOTE: endpoint='home' parameter specifies a unique name that can be used when 
    generating URLs. eg url_for('main.home')

    Returns:
        rendered_template: Rendered HTML template for the home page.
    """
    return render_home_page()

@main_bp.route('/login')
def login():
    """
    Define a route for the login page.

    Returns:
        rendered_template: Rendered HTML template for the login page.
    """
    return render_login_page()

@main_bp.route('/forum')
def forum():
    """
    Define a route for the forum page.

    Returns:
        rendered_template: Rendered HTML template for the forum page.
    """
    return render_forum_page()

@main_bp.route('/marketplace')
def marketplace():
    """
    Define a route for the marketplace page.

    Returns:
        rendered_template: Rendered HTML template for the marketplace page.
    """
    return render_marketplace_page()

# Add more routes as needed