from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()


def create_app(config_name):

    # Initializing application
    app = Flask(__name__)

    #creating app configuration
    app.config.from_object(config_options[config_name])

    #Initializing Flask Extensions
    bootsrap.init_app(app)

    #Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app