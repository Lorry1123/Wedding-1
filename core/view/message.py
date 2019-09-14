from flask_restful import Resource
from flask import request
from core.actions.message_handler import MsgHandler


class Messages(Resource):

    def get(self):
        res = MsgHandler().list_all()
        return {"total": len(res), "data": res}, 200

    def post(self):
        body = request.get_json()
        MsgHandler().create(**body)
        return {"status": "ok"}, 200
