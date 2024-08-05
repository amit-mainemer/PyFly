from flask_restful import Resource, request
from server.models import Ticket, db
from server.schemas import CreateTicketSchema, ticket_to_dict
from server.logger import logger


class TicketResource(Resource):
    def get(self, id):
        ticket = Ticket.query.get_or_404(id)
        return ticket_to_dict(ticket), 200

    def put(self, id):
        ticket = Ticket.query.get_or_404(int(id))
        data = request.get_json()
        ticket_schema = CreateTicketSchema()
        errors = ticket_schema.validate(data)
        if errors:
            return {"errors": errors}, 400

        ticket.user_id = data["user_id"]
        ticket.flight_id = data["flight_id"]
        db.session.commit()
        return ticket_schema.dump(ticket)

    def delete(self, id):
        logger.debug(id)
        ticket = Ticket.query.get(int(id))
        if ticket is None:
            return {"message": "ticket not found"}, 400

        db.session.delete(ticket)
        db.session.commit()
        return {"message": "ticket deleted successfully"}, 200
