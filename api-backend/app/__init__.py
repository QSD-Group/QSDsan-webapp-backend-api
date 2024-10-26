# Python Version: 3.10.1
from flask import Flask # flask Version 3.0.3, we use this run our API
from flask_cors import CORS # flask-cors Version 5.0.0, we use this to allow cross-origin requests
from flasgger import Swagger # flasgger Version 0.9.7.1, we use this to generate swagger documentation for our API

# We use blueprints from Flask to organize our API into different modules
from app.blueprints.fermentation import fermentation_bp
from app.blueprints.htl import htl_bp
from app.blueprints.combustion import combustion_bp

def create_app():
    app = Flask(__name__)
    CORS(app)
    Swagger(app)
    
    app.register_blueprint(fermentation_bp, url_prefix='/api/v1')
    app.register_blueprint(htl_bp, url_prefix='/api/v1')
    app.register_blueprint(combustion_bp, url_prefix='/api/v1')
    
    return app
