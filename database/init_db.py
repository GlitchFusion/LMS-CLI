from database.db_connections import get_connection

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    with open('database/schema.sql', 'r') as f:
        schema = f.read()
        cursor.executescript(schema)
    
    conn.commit()
    conn.close()