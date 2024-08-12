import os
from flask import Flask, request
from flask_seeder import FlaskSeeder
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from server.models import db
from server.logger import logger
from server.api import register_resources
from server.logger import logger


def create_app(db_uri, testing = False):
    app = Flask(__name__)

    logger.info(f"init db uri: {db_uri}")
    app.config['TESTING'] = testing
    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config['JWT_SECRET_KEY'] = os.environ["JWT_TOKEN"]
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 604800  # 1 week
    JWTManager(app)
    

    db.init_app(app)
    Migrate(app, db)
    seeder = FlaskSeeder()
    seeder.init_app(app, db)

    CORS(app)    
    register_resources(app)
    return app