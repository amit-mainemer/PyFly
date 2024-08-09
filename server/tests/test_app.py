from server.app import create_app
from server.models import db

app = create_app("sqlite:///:memory:", True)


with app.app_context():
    db.create_all()
    print("All tables created successfully.")