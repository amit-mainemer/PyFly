import json
from flask_restful import Resource
from flask import request
from server.models import User, db
from server.schemas import CreateUserSchema, user_to_dict
from marshmallow import ValidationError
from server.logger import logger


class UsersResource(Resource):
    def get(self):
        users = User.query.all()
        result = [user_to_dict(user) for user in users]
        return result

    def post(self):
        create_user_schema = CreateUserSchema()
        logger.info(json.loads(request.data))
        try:
            data = create_user_schema.load(json.loads(request.data))
        except ValidationError as err:
            return {"messages": err.messages}, 422

        newUser = User(data["full_name"], data["password"], data["real_id"])
        db.session.add(newUser)
        db.session.commit()
        return {"newUserId": newUser.id}
