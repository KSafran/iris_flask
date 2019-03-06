from flask import Flask
from .routes import ROUTES
from .pyconfig import config
from .iris_model import load_model

def create_app():
    chip=Flask(__name__)
    chip.config.update(config)
    chip.register_blueprint(ROUTES)
    chip.iris_model = load_model(config['MODEL'])
    return chip
