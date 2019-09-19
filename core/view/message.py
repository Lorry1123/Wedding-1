from flask_restful import Resource
from flask import request
from core.actions.message_handler import MsgHandler
from core.serializer import MsgSchema
from core.utils import beaker_cache


class Messages(Resource):

    @beaker_cache.cache("list_msgs", expire=1)
    def post(self):
        res = MsgHandler().list_all()
        res = MsgSchema().dump(res, many=True)
        return {"total": len(res), "data": res}, 200


class NewMessages(Resource):

    def post(self):
        body = request.get_json()
        body = MsgSchema().load(body)
        status, errmsg = MsgHandler().create(**body)
        return {"status": status, "errmsg": errmsg}, 200
