from database.db_connections import get_connection

# Database storage class
class DBStorage:
    # Add author to database
    def add_authors(self, name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))
        conn.commit()
        conn.close()

    # Get all authors from database
    def get_authors(self):
        conn =  get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors")
        authors = cursor.fetchall()
        conn.close()
        return authors

    # get users from database
    def get_users(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        conn.close()
        return users

    def get_books(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        conn.close()
        return books