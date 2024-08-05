import json
from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from server.models import User, db, Ticket, Flight
from server.schemas import CreateTicketSchema, ticket_to_dict


class TicketsResource(Resource):
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

        newTicket = Ticket(data["flight_id"], data["user_id"])
        flight.remaining_seats -= 1
        db.session.add(newTicket)
        db.session.commit()
        return {"newTicketId": newTicket.id}
