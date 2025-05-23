"""
This module initializes the Flask web application and defines routes for rendering
HTML templates. It serves as the main entry point for the web server, handling
requests and responses.

Attributes:
    app: Flask application instance configured in the app package.
"""
from flask import render_template
from app import app



@app.route('/')
def index():
    """Render the homepage template"""
    user = {"name": "Biswajit", "is_authenticated": False}
    skills = {"Python", "Flask", "Django", "Jinja2"}
    return render_template("index.html", user=user, skills=skills)


@app.route('/about')
def about():
    """Render the about page template"""
    return render_template("about.html")


@app.route('/contact')
def contact():
    """Render the contact page template"""
    contact_info = {
        'email': 'your_name@gmail.com',
        'linkedin': 'https://linkedin.com/in/your_name',
        'github': 'https://github.com/your_name'
    }
    return render_template("contact.html", contact=contact_info)
