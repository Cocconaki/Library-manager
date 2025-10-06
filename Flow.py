from ManageDatabase import *


class ControlFlow:

    def __init__(self, db_connector):
        self.db_connector = db_connector
    
    def add_book(self):
        
        name = str(input("Enter books name: "))
        number_of_pages = int(input("Enter the number of pages: "))
        author = str(input("Enter authors full name: "))
        category = str(input("Enter books category: "))
        title = str(input("Enter books Title: "))
        is_avalable = str(input("Enter if the book is on stock (y/n?): ")).strip().lower() == "y"
        count = int(input("Enter how many is on stock at the moment: "))
        
        self.db_connector.cursor.execute("INSERT INTO books (name, number_of_pages, author, category, title, is_available, count) VALUES (?, ?, ?, ?, ?, ?, ?)", (name, number_of_pages, author, category, title, is_avalable, count ))
        self.db_connector.connection.commit()
    
    def delete_book(self):
        id_to_del = int(input("Enter books ID to delete: "))
        self.db_connector.cursor.execute("DELETE FROM books WHERE id = ?", (id_to_del,))
        self.db_connector.connection.commit()

    def show_all_books(self):
        
        self.db_connector.cursor.execute("SELECT * FROM books")
        rows = self.db_connector.cursor.fetchall()

        for row in rows:
            print(row)
    
    def delete_all(self):
        self.db_connector.cursor.execute("DELETE FROM books")
        self.db_connector.connection.commit()
