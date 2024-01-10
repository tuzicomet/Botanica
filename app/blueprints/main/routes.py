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

# NOTE: enpoint parameter specifies a unique name that can be used when generating URLs
# eg url_for('main.home')

# Define a route for the home page
@main_bp.route('/', endpoint='home')
def home():
    return render_home_page()

# Define a route for the login page
@main_bp.route('/login')
def login():
    return render_login_page()

# Define a route for the forum page
@main_bp.route('/forum')
def forum():
    return render_forum_page()

# Define a route for the marketplace page
@main_bp.route('/marketplace')
def marketplace():
    return render_marketplace_page()

# Add more routes as needed