from flask import Flask
import os

from app.main.routes import *

def create_app():
    app = Flask(__name__)

    # apply app static path
    app.static_folder = 'main/static'

    # load app config
    app.config.from_object(os.environ.get('FLASK_ENV', 'config.Config'))

    # register app blueprints
    app.register_blueprint(main_blueprint)

    return app