from flask import jsonify
from flask_restful import Resource, request
from server.models import User, db
from server.schemas import CreateUserSchema, user_to_dict


class UserResource(Resource):
    def get(self, id):
        user = User.query.get_or_404(id)
        return user_to_dict(user), 200

    def put(self, id):
        user = User.query.get_or_404(int(id))
        data = request.get_json()
        user_schema = CreateUserSchema()
        errors = user_schema.validate(data)
        if errors:
            return errors, 400

        user.name = data["name"]
        user.password = data["password"]
        db.session.commit()
        return user_schema.dump(user)

    def delete(self, id):
        user = User.query.get(id)
        if user is None:
            return {"message": "User not found"}, 400

        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted successfully"}, 200
