from flask import Flask
from flask_cors import CORS
from app.controllers import blueprints
from config import Config
from app.models import init_app  
from app.schemas import ma
from flask_jwt_extended import JWTManager

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    ma.init_app(app)
    init_app(app)    
    CORS(app)
    jwt = JWTManager(app)

    for bp in blueprints:
        app.register_blueprint(bp)

    return app