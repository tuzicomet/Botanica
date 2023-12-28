"""
app.py

This file serves as the main entry point for the Botanica web application.
It defines the Flask application instance, routes, and configuration.

Last edited: 28/12/2023 11:19pm NZT
"""

from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    # Render the 'index.html' template
    return render_template('index.html')

# This block ensures that the app is run only when this script is executed directly
if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)