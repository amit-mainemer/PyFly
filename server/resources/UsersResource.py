import json
from flask_restful import Resource
from flask import request
from models import User, db
from schemas import CreateUserSchema, user_to_dict
from marshmallow import ValidationError
from logger import get_logger

class UsersResource(Resource):
    def __init__(self):
        self.logger = get_logger("users_resource")
        
    def get(self):
        users = User.query.all()
        result = [user_to_dict(user) for user in users]
        return result

    def post(self):
        create_user_schema = CreateUserSchema()

        try:
            data = create_user_schema.load(json.loads(request.data))
        except ValidationError as err:
            self.logger.warn(f"User signup attempt failed 422")
            return {"messages": err.messages}, 422
        
        newUser = User(data["full_name"], data["password"], data["real_id"])
        db.session.add(newUser)
        db.session.commit()
        self.logger.info(f"New user signup newUserId: {newUser.id}" )
        return {"newUserId": newUser.id}
