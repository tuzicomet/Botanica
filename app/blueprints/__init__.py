"""
    blueprints/__init__.py

    This file initializes the Flask blueprints for the Botanica web application.
    It creates and configures the main and auth blueprints.

    NOTE: __init__.py files in a directory are a special type of file in Python,
    which have 2 important purposes:
    1 - when present, Python will treat the directory as a package, meaning that
        like other packages, its modules can be imported in the same way.
    2 - The code contained within these files will be executed when the package
        or its modules are imported, such as any setup or initialisation needed.

    Author: Leonard Lau
    Last Updated: 09/01/2024
"""

from flask import Blueprint

"""TODO"""