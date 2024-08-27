import os
from flask import Flask
from flask_jwt_extended import JWTManager
from models import db
from api import register_resources
from logger import get_logger

def create_app(db_uri, testing=False):
    if testing:
        os.environ["FLASK_ENV"] = "testing"

    app = Flask(__name__)
    
    # Integrate your logger with Flask
    logger = get_logger()
    app.logger.handlers = logger.handlers
    app.logger.setLevel(logger.level)

    app.logger.info(f"Connect to postgres db...")
    app.config["TESTING"] = testing
    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["JWT_SECRET_KEY"] = os.environ["JWT_TOKEN"]
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 604800  # 1 week
    JWTManager(app)
    
    db.init_app(app)

    register_resources(app)
    return app



