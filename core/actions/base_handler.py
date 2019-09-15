class BaseHandler:

    def __init__(self, object_id=None):
        self.object_id = object_id
        self.collection = None

    def get(self):
        result = self.collection.find_one({"_id": self.object_id})
        return result
