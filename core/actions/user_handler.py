import random

from core.actions.base_handler import BaseHandler
from core.database import db
from core.exceptions import EmptyLotteryPool


class UserHandler(BaseHandler):

    def __init__(self, object_id=None):
        super(UserHandler, self).__init__(object_id)
        self.collection = db.user

    def create(self, **kwargs):
        exist_user = self.collection.find_one(kwargs)
        if exist_user:
            return UserHandler(exist_user["_id"])
        result = self.collection.insert_one(kwargs)
        object_id = result.inserted_id
        return UserHandler(object_id)

    def list_all(self):
        result = list(self.collection.find())
        return result

    def lottery(self):
        users = self.list_all()
        count = len(users)
        if not count:
            raise EmptyLotteryPool("当前没有用户可参与抽奖")
        idx = random.randint(0, count - 1)
        return users[idx], users
