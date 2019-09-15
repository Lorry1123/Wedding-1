import time

import pymongo

from core.actions.base_handler import BaseHandler
from core.actions.user_handler import UserHandler
from core.database import db


class MsgHandler(BaseHandler):

    def __init__(self, object_id=None):
        super(MsgHandler, self).__init__(object_id)
        self.collection = db.message

    def create(self, **kwargs):
        nick = kwargs.get("nick")
        avatar = kwargs.get("avatar")
        if not nick:
            return
        user_id = UserHandler().create(nick=nick, avatar=avatar).object_id
        kwargs.update({"create_t": time.time(), "user_id": user_id})
        result = self.collection.insert_one(kwargs)
        return MsgHandler(result.inserted_id)

    def list_all(self):
        result = self.collection.find(limit=100, sort=[("_id", pymongo.DESCENDING)])
        return result
