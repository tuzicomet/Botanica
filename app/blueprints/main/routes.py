"""
    blueprints/main/routes.py

    This file defines the routes specific to the 'main' blueprint,
    handling the main pages and functionalities of the Botanica web application.

    Author: Leonard Lau
    Last Updated: 09/01/2024
"""

from flask import Blueprint, render_template
from . import main_bp

# Define routes for the 'main' blueprint
# (define routes for pages using this blueprint)

@main_bp.route('/', endpoint='home')
def home():
    # Render the 'index.html' template
    return render_template('pages/index.html')

# Define a route for the login page
@main_bp.route('/login')
def login():
    # Render the 'login.html' template
    return render_template('pages/login.html')

@main_bp.route('/forum')
def forum():
    # Render the 'forum.html' template
    return render_template('pages/forum.html')

@main_bp.route('/marketplace')
def marketplace():
    # Render the 'marketplace.html' template
    return render_template('pages/marketplace.html')

# Add more routes as needed