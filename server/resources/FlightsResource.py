from flask import request
from flask_restful import Resource, reqparse
from server.models import Flight
from server.schemas import flight_to_dict
from server.logger import logger


class FlightsResource(Resource):
    def get(self):
        origin_country_id = request.args.get("from")
        dest_country_id = request.args.get("to")
        page = request.args.get("page", default=1, type=int)
        per_page = 10
        logger.info("parsed values")

        flights_query = Flight.query
        if origin_country_id:
            flights_query = flights_query.filter(
                Flight.origin_country_id == origin_country_id
            )
        if dest_country_id:
            flights_query = flights_query.filter(
                Flight.dest_country_id == dest_country_id
            )

        logger.info("pass query")
        paginated_flights = flights_query.paginate(
            page=page, per_page=per_page, error_out=False
        )

        flights = [flight_to_dict(flight) for flight in paginated_flights.items]

        logger.info("send res")

        return {
            "total": paginated_flights.total,
            "pages": paginated_flights.pages,
            "current_page": paginated_flights.page,
            "flights": flights,
        }
