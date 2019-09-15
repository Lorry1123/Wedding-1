from flask_restful import Resource
from core.actions.user_handler import UserHandler
from core.serializer import UserSchema


class Users(Resource):

    def post(self):
        winner, users = UserHandler().lottery()
        winner = UserSchema().dump(winner)
        users = UserSchema().dump(users, many=True)
        return {"winner": winner, "users": users}, 200
