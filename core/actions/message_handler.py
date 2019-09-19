import time

import pymongo

from core.actions.base_handler import BaseHandler
from core.actions.user_handler import UserHandler
from core.database import db
from core.utils import check_msg_sec


class MsgHandler(BaseHandler):

    def __init__(self, object_id=None):
        super(MsgHandler, self).__init__(object_id)
        self.collection = db.message

    def create(self, **kwargs):
        msg = kwargs.get("msg")
        status, errmsg = check_msg_sec(msg)
        if status != 0:
            return status, errmsg

        nick = kwargs.get("nick")
        avatar = kwargs.get("avatar")
        if not nick:
            return 5000, "无法获取用户信息"
        user_id = UserHandler().create(nick=nick, avatar=avatar).object_id
        kwargs.update({"create_t": time.time(), "user_id": user_id})
        result = self.collection.insert_one(kwargs)
        return status, errmsg

    def list_all(self):
        result = self.collection.find(limit=100, sort=[("_id", pymongo.DESCENDING)])
        return result
