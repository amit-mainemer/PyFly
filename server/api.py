from flask_restful import Api
from resources.Home import Home
from resources.UsersResource import UsersResource
from resources.UserResource import UserResource
from resources.FlightsResource import FlightsResource
from resources.LoginResource import LoginResource
from resources.CountriesResource import CountriesResource
from resources.TicketsResource import TicketsResource
from resources.TicketResource import TicketResource
from resources.UserTicketResource import UserTicketResource
from logger import logger


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
