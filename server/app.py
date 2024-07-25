from api import register_resources
from flask import Flask
from logger import logger
from config import config
from flask_seeder import FlaskSeeder
from flask_migrate import Migrate
from models import db
from flask_cors import CORS
from flask_jwt_extended import JWTManager


app = Flask(__name__)

logger.info(f"init db uri: {config['DB_URI']}")
app.config["SQLALCHEMY_DATABASE_URI"] = config["DB_URI"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['JWT_SECRET_KEY'] = config["JWT_TOKEN"]

jwt = JWTManager(app)


db.init_app(app)
migrate = Migrate(app, db)
seeder = FlaskSeeder()
seeder.init_app(app, db)
CORS(app)

register_resources(app)

if __name__ == '__main__':
    app.run(debug=True)
