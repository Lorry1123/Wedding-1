import time

from core.actions.base_handler import BaseHandler
from core.actions.user_handler import UserHandler
from core.database import db
from core.utils import beaker_cache


class MsgHandler(BaseHandler):

    def __init__(self, object_id=None):
        super(MsgHandler, self).__init__(object_id)
        self.collection = db.message

    def create(self, **kwargs):
        nick = kwargs.get("nick")
        avatar = kwargs.get("avatar")
        if nick:
            user_id = UserHandler().create(nick=nick, avatar=avatar)
        else:
            user_id = None
        kwargs.update({"create_t": time.time(), "user_id": user_id})
        result = self.collection.insert_one(kwargs)
        return MsgHandler(result.inserted_id)

    @beaker_cache
    def list_all(self):
        result = self.collection.find()
        return result
