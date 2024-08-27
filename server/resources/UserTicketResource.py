from flask_restful import Resource
from models import Ticket
from schemas import ticket_to_dict
from logger import get_logger

class UserTicketResource(Resource):
    def __init__(self):
        self.logger = get_logger("user_ticket_resource")
        
    def get(self, id):
        userTickets = Ticket.query.filter_by(user_id=int(id)).all()
        if userTickets is None:
            return []
        return [ticket_to_dict(ticket) for ticket in userTickets], 200
