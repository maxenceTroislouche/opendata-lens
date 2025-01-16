from pymongo import MongoClient

from models import Evenement


class MongoDatabase:
    def __init__(self):
        self._client = MongoClient("mongodb://admin:securepassword@localhost:27017/")
        self._db = self._client["opendatalens"]
        self._collection = self._db["evenement"]

    def insert_events(self, events: list[Evenement]):
        self._collection.insert_many([event.to_dict() for event in events])

    def close(self):
        self._client.close()
