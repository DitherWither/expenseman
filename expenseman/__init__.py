from flask import Flask
from expenseman.config import Config
import expenseman.routes


def create_app(config_class=Config) -> Flask:
    """Creates a new application, and returns the flask app object

    Args:
        config_class: Config class, or something that inherits it, optional

    Returns:
        Flask: the application object
    """

    app = Flask(__name__)
    app.config.from_object(config_class)
    app.secret_key = Config.SECRET_KEY
    
    # Add blueprints
    app.register_blueprint(expenseman.routes.blueprint)

    return app


def main():
    """The application factory to be used to run the app"""
    return create_app(Config)
