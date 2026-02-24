# File Structure

├── main.py
├── config.py
│
├── core/
│ ├── pwd_manager.py
│ ├── auth_manager.py
│ ├── book_manager.py
│ ├── user_manager.py
│ ├── transaction_manager.py
│ └── reminder.py
│
├── storage/
│ ├── storage_interface.py
│ ├── file_handler.py
│ ├── csv_storage.py
│ ├── json_storage.py
│ └── db_storage.py
│
├── database/
│ ├── db_connection.py
│ ├── schema.sql
│ └── library.db
│
├── utils/
  ├── password_utils.py
│ ├── validators.py
│ ├── date_utils.py
│ └── menu.py
│
├── reports/
│ └── report_generator.py
│
├── README.md
└── requirements.txt

## Database Components Explained

### `database/db_connection.py`

Handles database connectivity:

- Opens and closes SQLite connections
- Provides reusable database access functions
- Centralizes connection management

---

### `database/schema.sql`

Defines the database structure:

- `books` table
- `users` table
- `transactions` table

The database can be recreated at any time using this schema.

### `database/library.db`

SQLite database file that stores:

- Book records
- User information
- Issue and return transactions
- Fine data

Automatically created on first run if not present.

## Storage Abstraction Layer

### `storage/storage_interface.py`

Defines a **common interface** for all storage types.

All storage implementations must support:

- Add, update, delete books
- Retrieve book and user data
- Record transactions

This ensures that CSV, JSON, and Database storage are interchangeable.

### `storage/db_storage.py`

Implements the storage interface using SQLite:

- Executes SQL queries
- Converts query results to Python dictionaries
- Handles CRUD operations for books, users, and transactions

---

### `storage/file_handler.py`

Acts as a storage router:

- Reads storage type from `config.py`
- Dynamically selects CSV, JSON, or Database backend
- Exposes a unified API to the core logic

---

## Configuration

Database usage is controlled via `config.py`:

```python
STORAGE_TYPE = "db"  # csv | json | db
DATABASE_PATH = "database/library.db"

FINE_PER_DAY = 10
MAX_BOOKS_PER_USER = 3
```
