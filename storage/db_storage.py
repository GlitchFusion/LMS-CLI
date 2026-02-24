from database.db_connections import get_connection

# Database storage class
class DBStorage:
    # getting data from db----------

    # Get all authors from database
    def get_all_authors(self):
        conn =  get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors")
        authors = cursor.fetchall()
        conn.close()
        return authors

    # get users from database
    def get_all_users(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        conn.close()
        return users

    # getting books from database
    def get_all_books(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        conn.close()
        return books
    
    # Adding to database ----------
    
    # Add author to database
    def add_authors(self, name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))
        conn.commit()
        conn.close()
    
    # adding books to database
    def add_books(self, title, author_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author_id) VALUES (?, ?)", (title, author_id))
        conn.commit()
        conn.close()
    
    # adding users to database