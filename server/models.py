from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))
    password = db.Column(db.String(200))
    real_id = db.Column(db.Integer, unique=True)

    def __init__(self, full_name: str, password: str, real_id: int):
        self.full_name = full_name
        self.password = password
        self.real_id = real_id


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    code = db.Column(db.String(10), unique=True)

    def __init__(self, name: str, code: str):
        self.name = name
        self.code = code


class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    remaining_seats = db.Column(db.Integer)
    origin_country_id = db.Column(db.Integer, db.ForeignKey("country.id"))
    dest_country_id = db.Column(db.Integer, db.ForeignKey("country.id"))
    timestamp = db.Column(db.Date)

    def __init__(
        self,
        remaining_seats: int,
        origin_country_id: int,
        dest_country_id: int,
        timestamp,
    ):
        self.remaining_seats = remaining_seats
        self.origin_country_id = origin_country_id
        self.dest_country_id = dest_country_id
        self.timestamp = timestamp


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flight_id = db.Column(db.Integer, db.ForeignKey("flight.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __init__(self, flight_id, user_id):
        self.flight_id = flight_id
        self.user_id = user_id
