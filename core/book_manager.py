from storage.db_storage import DBStorage

class BookManager:
    def __init__(self):
        self.storage = DBStorage()
