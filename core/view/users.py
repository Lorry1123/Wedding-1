from flask_restful import Resource
from core.actions.user_handler import UserHandler


class Users(Resource):

    def get(self):
        res = UserHandler().lottery()
        return res, 200
