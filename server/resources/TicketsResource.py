import json
from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from models import User, Ticket, Flight, db
from schemas import CreateTicketSchema, ticket_to_dict
from logger import get_logger
from rabbit import RabbitProducer
from constants import TICKETS_ORDER_QUEUE
from cache import redis_client

class TicketsResource(Resource):
    def __init__(self):
        self.logger = get_logger("tickets_resource")
        self.producer = RabbitProducer(TICKETS_ORDER_QUEUE)

    def get(self):
        tickets = Ticket.query.all()
        if tickets is None:
            return []
        result = [ticket_to_dict(ticket) for ticket in tickets]
        return result

    def post(self):
        create_ticket_schema = CreateTicketSchema()
        try:
            data = create_ticket_schema.load(json.loads(request.data))
        except ValidationError as err:
            return {"errors": err.messages}, 422

        flight = Flight.query.filter_by(id=data["flight_id"]).first()
        if flight is None:
            return {"error": "No such flight"}, 400
        if flight.remaining_seats == 0:
            return {"error": "flight has no remaining seats"}, 400

        user = User.query.filter_by(id=data["user_id"]).first()
        if user is None:
            return {"error": "No such user"}, 400

        flight.remaining_seats -= 1

        newTicket = Ticket(data["flight_id"], data["user_id"])
        db.session.add(newTicket)
        db.session.commit()
        self.logger.info(
            f"New ticket was bought successfully. ticketId: {newTicket.id}"
        )

        try:
            self.producer.push_message(
                {
                    "ticketId": newTicket.id,
                    "userId": data["user_id"],
                    "flightId": data["flight_id"],
                }
            )
        except Exception as e:
            self.logger.debug("Message wasn't sent. probably testing")
        
        self.invalidate_flights_cache()        

        return {"message": "order was sent!", "newTicketId": newTicket.id}
    
    def invalidate_flights_cache(self):
        try:
            self.logger.info("Clearing flights cached results")
            pattern = "flights_*"
            cursor = 0

            while True:
                cursor, keys = redis_client.scan(cursor=cursor, match=pattern)
                if keys:
                    for key in keys:
                        redis_client.delete(key)
                if cursor == 0:
                    break
        except Exception as e:
            self.logger.debug("Cache wasn't cleared. probably testing")

