from marshmallow import fields, validate, Schema
from server.models import Country, User, Flight
from server.logger import logger
import re


class CreateUserSchema(Schema):
    full_name = fields.String(required=True, validate=validate.Length(min=1, max=100))
    password = fields.String(
        required=True,
        validate=validate.And(
            validate.Length(min=8),
            validate.Regexp(
                regex=re.compile("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"),
                error="Password must contain at least one letter and one number",
            ),
        ),
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
    logger.debug(f"ticket {ticket.user_id} {ticket.flight_id}")
    user_id = ticket.user_id
    flight_id = ticket.flight_id
    user = User.query.filter_by(id=user_id).first()
    logger.debug(user)
    flight = Flight.query.filter_by(id=flight_id).first()
    return {
        "id": ticket.id,
        "user": user_to_dict(user),
        "flight": flight_to_dict(flight),
    }
