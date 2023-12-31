"""
    app.py

    This file serves as the main entry point for the Botanica web application.
    It defines the Flask application instance, routes, and configuration.

    Author: Leonard Lau
    Last Updated: 29/12/2023
"""

import os
from flask import send_from_directory  

from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__, template_folder='templates')

# Add a custom view to handle /favicon requests, as by default, flask only serves files on the /static endpoint
@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

# Define a route for the home page
@app.route('/')
def home():
    # Render the 'index.html' template
    return render_template('pages/index.html')

# Define a route for the login page
@app.route('/login')
def marketplace():
    # Render the 'login.html' template
    return render_template('pages/login.html')

# Define a route for the forum front page
@app.route('/forum')
def forum():
    # Render the 'forum.html' template
    return render_template('pages/forum.html')

# Define a route for the marketplace front page
@app.route('/marketplace')
def marketplace():
    # Render the 'marketplace.html' template
    return render_template('pages/marketplace.html')

# This block ensures that the app is run only when this script is executed directly
if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)