"""
Main application and routing logic for Twitter-Comparator
"""
from decouple import config
from flask import Flask
from .models import DB
from .twitter import add_or_update_user


def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = config("DATABASE_URL")
    DB.init_app(app)

    @app.route("/")
    def root():
        return "Welcome to the Twitter Comparator."

    @app.route("/reset")
    def reset():
        DB.drop_all()
        DB.create_all()
        return "DB reset!"


    return app
