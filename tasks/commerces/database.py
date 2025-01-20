from pymongo import MongoClient
from models import Commerce

class MongoDatabase:
    def __init__(self):
        self._client = MongoClient("mongodb://admin:securepassword@localhost:27017/")
        self._db = self._client["opendatalens"]
        self._collection = self._db["commerce"]

    def insert_shops(self, commerces: list[Commerce]):
        self._collection.insert_many([commerce.to_dict() for commerce in commerces])

    def close(self):
        self._client.close()