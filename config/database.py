from pymongo import MongoClient
from pymongo.collection import Collection



class DatabaseSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseSingleton, cls).__new__(cls)
            cls._instance.client = MongoClient("mongodb://localhost:27017/")
            cls._instance.db = cls._instance.client["auth"]
            cls._instance.collection: Collection = cls._instance.db["users"]
        return cls._instance


