from flask_restful import Resource
from server.models import Ticket
from server.schemas import ticket_to_dict


class UserTicketResource(Resource):
    def get(self, id):
        userTickets = Ticket.query.filter_by(user_id=int(id)).all()
        if userTickets is None:
            return []
        return [ticket_to_dict(ticket) for ticket in userTickets], 200
