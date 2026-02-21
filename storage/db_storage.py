from database.db_connections import get_connection

# Database storage class
class DBStorage:
    def add_authors(self, name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))
        conn.commit()
        conn.close()