from storage.db_storage import DBStorage

class BookManager:
    def __init__(self):
        self.storage = DBStorage()

    def add_author(self, name):
        self.storage.add_authors(name)

    def list_authors(self):
        return self.storage.get_authors()
    
    
    