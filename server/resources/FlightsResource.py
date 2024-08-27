import json
import time
from flask import request
from flask_restful import Resource
from models import Flight
from schemas import flight_to_dict
from cache import redis_client
from logger import get_logger

SP_EXPIRATION = 600  # 10 minutes
ROWS_PER_PAGE = 10


def cache_sp(sp_key: str, result):
    redis_client.set(
        sp_key, json.dumps({"timestamp": int(time.time()), "value": result})
    )


class FlightsResource(Resource):
    def __init__(self):
        self.logger = get_logger("flights_resource")
        
    def get(self):
        origin_country_id = request.args.get("from")
        dest_country_id = request.args.get("to")
        page = request.args.get("page", default=1, type=int)

        sp_key = f"flights_{origin_country_id}_{dest_country_id}_page_{page}"

        cached_result = redis_client.get(sp_key)
        if cached_result:
            cached_result = json.loads(cached_result)
            timestamp = cached_result["timestamp"]
            current_time = int(time.time())

            if current_time - timestamp < SP_EXPIRATION:
                return cached_result["value"]
            
        self.logger.info("Calling Stored Procedure saving flights query to cache")

        flights_query = Flight.query
        if origin_country_id:
            flights_query = flights_query.filter(
                Flight.origin_country_id == origin_country_id
            )
        if dest_country_id:
            flights_query = flights_query.filter(
                Flight.dest_country_id == dest_country_id
            )

        paginated_flights = flights_query.paginate(
            page=page, per_page=ROWS_PER_PAGE, error_out=False
        )

        flights = [flight_to_dict(flight) for flight in paginated_flights.items]

        result = {
            "total": paginated_flights.total,
            "pages": paginated_flights.pages,
            "current_page": paginated_flights.page,
            "flights": flights,
        }

        cache_sp(sp_key, result)

        return result
