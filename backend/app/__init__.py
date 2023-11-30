"""INITIALIZE APP"""
from flask import Flask
from flask_login import LoginManager
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from config.config import Config

db = SQLAlchemy()
login_manager = LoginManager()
session = Session()

def create_app():
    """ CREATE, REGISTER AND COMPILE """
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)

    # Initialize Plugins
    db.init_app(app)
    login_manager.init_app(app)
    session.init_app(app)

    # pylint: disable=C0415
    with app.app_context():
        from .home.routes import main_blueprint
        from .auth.routes import auth_blueprint
        from .assets import compile_static_assets

        app.register_blueprint(main_blueprint)
        app.register_blueprint(auth_blueprint)

        for blueprint_name, blueprint in app.blueprints.items():
            print(f"Blueprint Name: {blueprint_name}, Blueprint Object: {blueprint}")


        # Create static asset bundles
        compile_static_assets(app)
        # Create Database Models
        db.create_all()

        return app