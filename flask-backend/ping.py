
from mongo_manager import MongoDBmanager
metadata_DB = MongoDBmanager("Products")

class Ping:
    @staticmethod
    def ping():
        return "Hello World, I am flask app!!!"