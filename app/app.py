"""
    app.py

    This file serves as the main entry point for the Botanica web application.
    It defines the Flask application instance, routes, and configuration.

    Author: Leonard Lau
    Last Updated: 9/01/2023
"""

import os
from flask import send_from_directory  
from flask import Flask, render_template
from blueprints.main import main_bp

# Import the Config class from config.py
# TODO: create config.py later when needed

# Create a Flask application instance
app = Flask(__name__, template_folder='templates')

# Create a function to create and configure the Flask application
def create_app():
    # Create the Flask application instance
    app = Flask(__name__, template_folder='templates')

    # Load configuration from the Config class TODO: create it
    # app.config.from_object(Config)

    # Register the main Blueprint
    from blueprints.main import main_bp
    app.register_blueprint(main_bp)

    # Add a custom view to handle /favicon requests, as by default, flask only 
    #   serves files on the /static endpoint
    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'), 
                                   'favicon.ico', mimetype='image/vnd.microsoft.icon')

    return app

# Create the Flask application instance
app = create_app()

# This block ensures that the app is run only when this script is executed directly
if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)