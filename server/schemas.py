from marshmallow import fields, validate, Schema, ValidationError
from models import Country, User, Flight
from logger import logger
import re

def validate_password(password):
    if len(password) < 6:
        raise ValidationError("Password must be at least 6 characters long")
    if not any(char.isdigit() for char in password):
        raise ValidationError("Password must contain at least one number")
    if not any(char.isalpha() for char in password):
        raise ValidationError("Password must contain at least one letter")

class CreateUserSchema(Schema):
    full_name = fields.String(required=True, validate=validate.Length(min=1, max=100))
    password = fields.String(
        required=True,
        validate=validate_password,
    )
    real_id = fields.Integer(required=True)


class CreateCountrySchema(Schema):
    full_name = fields.String(required=True, validate=validate.Length(min=1, max=225))


class CreateFlightSchema(Schema):
    origin_country_id = fields.Integer(required=True)
    dest_country_id = fields.Integer(required=True)
    timestamp = fields.Date(required=True)
    remaining_seats = fields.Integer(required=True)


class CreateTicketSchema(Schema):
    user_id = fields.Integer(required=True)
    flight_id = fields.Integer(required=True)


def user_to_dict(user):
    return {"id": user.id, "full_name": user.full_name, "real_id": user.real_id}


def country_to_dict(country):
    return {"id": country.id, "name": country.name, "code": country.code}


def flight_to_dict(flight):
    origin_country = Country.query.filter_by(
        id=flight.origin_country_id
    ).first()
    dest_country = Country.query.filter_by(
        id=flight.dest_country_id
    ).first()
    return {
        "id": flight.id,
        "remaining_seats": flight.remaining_seats,
        "origin_country": country_to_dict(origin_country),
        "dest_country": country_to_dict(dest_country),
        "timestamp": flight.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
    }


def ticket_to_dict(ticket):
    user_id = ticket.user_id
    flight_id = ticket.flight_id
    user = User.query.filter_by(id=user_id).first()
    flight = Flight.query.filter_by(id=flight_id).first()
    return {
        "id": ticket.id,
        "user": user_to_dict(user),
        "flight": flight_to_dict(flight),
    }
