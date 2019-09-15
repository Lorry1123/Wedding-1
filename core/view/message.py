from flask_restful import Resource
from flask import request
from core.actions.message_handler import MsgHandler
from core.serializer import MsgSchema


class Messages(Resource):

    def post(self):
        res = MsgHandler().list_all()
        res = MsgSchema().dump(res, many=True)
        return {"total": len(res), "data": res}, 200


class NewMessages(Resource):

    def post(self):
        body = request.get_json()
        MsgHandler().create(**body)
        return {"status": "ok"}, 200
