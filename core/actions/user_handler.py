import random

from core.actions.base_handler import BaseHandler
from core.database import db


class UserHandler(BaseHandler):

    def __init__(self, object_id=None):
        super(UserHandler, self).__init__(object_id)
        self.collection = db.user

    def create(self, **kwargs):
        result = self.collection.update(kwargs, kwargs, upsert=True)
        object_id = result.upserted_id
        return UserHandler(object_id)

    def list_all(self):
        result = self.collection.find()
        return result

    def lottery(self):
        users = self.list_all()
        count = len(users)
        idx = random.randint(count)
        return users[idx], users
