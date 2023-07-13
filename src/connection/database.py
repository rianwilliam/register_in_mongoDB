from pymongo.database import Database
from pymongo import MongoClient
from .mongo_info import MONGO_INFO
from typing import Type

url = "mongodb://{}:{}".format(
    MONGO_INFO["HOST"],
    MONGO_INFO["PORT"]
)
client = MongoClient(url)
db = client.get_database("users_project")

def get_db() -> Type[Database]:
    return db
