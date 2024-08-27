from flask_restful import Resource
from logger import get_logger


class Home(Resource):
    def __init__(self):
        self.logger = get_logger('home_resource')
        
    def get(self):
        return {"message": "hello PyFly"}
