"""
    blueprints/main/__init__.py

    This file initializes the Flask blueprint for the main content-related routes
    in the Botanica web application.

    Author: Leonard Lau
    Last Updated: 09/01/2024
"""

from flask import Blueprint

# Create a Blueprint instance for the 'main' module
main_bp = Blueprint('main', __name__, template_folder='templates', static_folder='static')

# Import routes to include them in the blueprint
from . import routes