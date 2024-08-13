
import os
from application import create_app
from models import db

os.environ['FLASK_ENV'] = 'testing'
os.environ['JWT_TOKEN'] = 'JWT123'
os.environ['REDIS_HOST'] = 'localhost'
os.environ['REDIS_POST'] = '6379'

app = create_app("sqlite:///:memory:", True)

with app.app_context():
    db.create_all()
    print("All tables created successfully.")