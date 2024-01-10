"""
    blueprints/main/__init__.py

    This file initializes the Flask blueprint for the main content-related routes
    in the Botanica web application.

    Author: Leonard Lau
    Last Updated: 10/01/2024
"""

# NOTE: whatever is imported here, does not need to be imported again in routes.py or views.py

from flask import Blueprint

# Create a Blueprint instance for the 'main' module
main_bp = Blueprint('main', __name__, template_folder='templates', static_folder='static')

# Import routes to include them in the blueprint
from . import routes

# Import all view functions to include them in the blueprint
from .views import *