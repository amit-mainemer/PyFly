from marshmallow import fields, validate, Schema
from models import Country

class CreateUserSchema(Schema):
    full_name = fields.String(required=True, validate=validate.Length(min=1, max=100))
    password = fields.String(required=True, validate=validate.Length(min=2))
    real_id = fields.Integer(required=True)
    
def user_to_dict(user):
    return {
        'id': user.id,
        'full_name': user.full_name,
        'real_id': user.real_id
    }
    
def country_to_dict(country):
    return {
        "id": country.id,
        "name": country.name,
    }
    
def flight_to_dict(flight):
    origin_country = Country.query.get(flight.origin_country_id)
    dest_country = Country.query.get(flight.dest_country_id)
    return {
        "id": flight.id,
        "remaining_seats": flight.remaining_seats,
        'origin_country': country_to_dict(origin_country),
        'dest_country': country_to_dict(dest_country),
        "timestamp": flight.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    }
    