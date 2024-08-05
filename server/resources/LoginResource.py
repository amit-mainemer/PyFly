from flask_restful import Resource, request
from flask_jwt_extended import create_access_token
from server.models import User
from server.logger import logger


class LoginResource(Resource):
    def post(self):
        json_data = request.get_json()
        real_id = json_data.get("real_id")
        password = json_data.get("password")

        logger.info(f"Login attempt id: {real_id}")

        user = User.query.filter_by(real_id=real_id, password=password).first()
        if not user:
            return {"message": "Invalid credentials"}, 400

        access_token = create_access_token(
            identity={
                "full_name": user.full_name,
                "id": user.id,
                "real_id": user.real_id,
            }
        )
        return {"access_token": access_token}, 200
