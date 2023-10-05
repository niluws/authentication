from pymongo import MongoClient
from pymongo.collection import Collection



client = MongoClient("mongodb://localhost:27017/")
db = client["auth"]
collection: Collection = db["users"]


