import json
from flask_restful import Resource
from flask import request
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required
from models import Country, db
from schemas import CreateCountrySchema, country_to_dict


class CountriesResource(Resource):
    def __init__(self, **kwargs):
        self.logger = kwargs.get('logger')
        
    @jwt_required()
    def get(self):
        countries = Country.query.all()
        result = [country_to_dict(country) for country in countries]
        return result, 200

    @jwt_required()
    def post(self):
        create_country_schema = CreateCountrySchema()

        try:
            data = create_country_schema.load(json.loads(request.data))
        except ValidationError as err:
            return {"messages": err.messages}, 422

        newCountry = Country(data["name"])
        db.session.add(newCountry)
        db.session.commit()
        return {"newCountryId": newCountry.id}, 201
