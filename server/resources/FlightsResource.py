
from flask_restful import Resource
from models import Flight
from schemas import  flight_to_dict
    
class FlightsResource(Resource):
      def get(self):
        flights = Flight.query.all()
        result = [flight_to_dict(flight) for flight in flights]
        return result
    
            