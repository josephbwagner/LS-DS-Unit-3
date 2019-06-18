"""
Main application and routing logic for Twitter-Comparator
"""
from flask import Flask
from .models import DB
from decouple import config

def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = config("DATABASE_URL")
    DB.init_app(app)

    @app.route("/")
    def root():
        return "Thank you and welcome to the Twitter Comparator."

    return app
