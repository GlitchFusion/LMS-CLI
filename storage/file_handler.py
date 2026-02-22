from config import STORAGE_TYPE
from storage.db_storage import DBStorage

def get_storage():
    if STORAGE_TYPE == "db":
        return DBStorage()