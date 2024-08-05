from flask_restful import Api
from server.resources.Home import Home
from server.resources.UsersResource import UsersResource
from server.resources.UserResource import UserResource
from server.resources.FlightsResource import FlightsResource
from server.resources.LoginResource import LoginResource
from server.resources.CountriesResource import CountriesResource
from server.resources.TicketsResource import TicketsResource
from server.resources.TicketResource import TicketResource
from server.resources.UserTicketResource import UserTicketResource
from server.logger import logger


def register_resources(app):
    logger.info("register_resources")
    api = Api(app)
    api.add_resource(Home, "/")
    api.add_resource(UsersResource, "/users")
    api.add_resource(UserResource, "/user/<int:id>")
    api.add_resource(LoginResource, "/login")
    api.add_resource(FlightsResource, "/flights")
    api.add_resource(CountriesResource, "/countries")
    api.add_resource(TicketsResource, "/tickets")
    api.add_resource(TicketResource, "/ticket/<int:id>")
    api.add_resource(UserTicketResource, "/user/tickets/<int:id>")
