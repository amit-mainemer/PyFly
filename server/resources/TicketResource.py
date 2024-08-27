from flask_jwt_extended import jwt_required
from flask_restful import Resource, request
from models import Ticket, db
from schemas import CreateTicketSchema, ticket_to_dict
from logger import get_logger

class TicketResource(Resource):
    def __init__(self):
        self.logger = get_logger("ticket_resource")
        
    def get(self, id):
        ticket = Ticket.query.get_or_404(id)
        return ticket_to_dict(ticket), 200

    @jwt_required()
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

    @jwt_required()
    def delete(self, id):
        self.logger.info(f"Deleting ticket {id}")
        ticket = Ticket.query.get(int(id))
        if ticket is None:
            return {"message": "ticket not found"}, 400

        db.session.delete(ticket)
        db.session.commit()
        return {"message": "ticket deleted successfully"}, 200
