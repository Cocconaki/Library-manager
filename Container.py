import sqlite3
connection = sqlite3.connect("BooksInLibrary.db")
cursor = connection.cursor()

cursor.execute("""
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

cursor.execute("INSERT INTO books (name, number_of_pages, author, category, title, is_available, count) VALUES (?, ?, ?, ?, ?, ?, ?)", ("Bible", 1000, "Jesus", "Religion", "The holy book", True, 0))
cursor.execute("INSERT INTO books (name, number_of_pages, author, category, title, is_available, count) VALUES (?, ?, ?, ?, ?, ?, ?)", ("Bible", 1001, "Jesus", "Religion", "The holy book", True, 0))
cursor.execute("INSERT INTO books (name, number_of_pages, author, category, title, is_available, count) VALUES (?, ?, ?, ?, ?, ?, ?)", ("Bible", 1000, "Jesus", "Religion", "The holy book", True, 0))
cursor.execute("INSERT INTO books (name, number_of_pages, author, category, title, is_available, count) VALUES (?, ?, ?, ?, ?, ?, ?)", ("Bible", 1000, "Jesus", "Religion", "The holy book", True, 0))
cursor.execute("INSERT INTO books (name, number_of_pages, author, category, title, is_available, count) VALUES (?, ?, ?, ?, ?, ?, ?)", ("Bible", 1100, "Jesus", "Religion", "The holy book", True, 0))
cursor.execute("INSERT INTO books (name, number_of_pages, author, category, title, is_available, count) VALUES (?, ?, ?, ?, ?, ?, ?)", ("Bible", 1099, "Jesus", "Religion", "The holy book", True, 0))
cursor.execute("INSERT INTO books (name, number_of_pages, author, category, title, is_available, count) VALUES (?, ?, ?, ?, ?, ?, ?)", ("Bible", 1000, "Jesus", "Religion", "The holy book", True, 0))



connection.commit()


  