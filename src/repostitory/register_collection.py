from typing import Type
from pymongo.collection import Collection
from src.connection.database import get_db

db = get_db()
collection = db.get_collection("registered_users")

def get_collection() -> Type[Collection]:
    return collection
