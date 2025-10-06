import sqlite3

class DatabaseConnection:
    

    def __init__(self, db_name="BooksInLibrary.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON")
        self.connection.commit()



    @staticmethod
    def init_database(self):

        

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            number_of_pages INTEGER,
            author TEXT NOT NULL,
            category TEXT,
            title TEXT NOT NULL,
            is_available BOOLEAN,
            count INTEGER
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            gender TEXT NOT NULL,
            email TEXT,
            phone_number TEXT NOT NULL
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS borrowed_books (
            user_id INTEGER,
            books_id INTEGER,
            borrow_date TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (books_id) REFERENCES books(id)
        )
        """)

        self.connection.commit()

    
    @staticmethod
    def reinit_database(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ")
        tables = self.cursor.fetchall()
        for table in tables:
            self.cursor.execute(f'DROP TABLE IF EXISTS "{table[0]}"')
        self.connection.commit()
        self.init_database()
    
    @staticmethod
    def close(self):
        self.connection.close()
    
