from ManageDatabase import *




class ControlFlow:
    
    def add_book():
        
        name = str(input("Enter books name: "))
        number_of_pages = int(input("Enter the number of pages: "))
        author = str(input("Enter authors full name: "))
        category = str(input("Enter books category: "))
        title = str(input("Enter books Title: "))
        is_avalable = str(input("Enter if the book is on stock (y/n?): ")).strip().lower() == "y"
        count = int(input("Enter how many is on stock at the moment: "))
        
        cursor.execute("INSERT INTO books (name, number_of_pages, author, category, title, is_available, count) VALUES (?, ?, ?, ?, ?, ?, ?)", (name, number_of_pages, author, category, title, is_avalable, count ))


    def delete_book():
        id_to_del = int(input("Enter books ID to delete: "))
        cursor.execute("DELETE FROM books WHERE id = ?", (id_to_del,))

    def show_all_books():
        
        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    
    def delete_all():
        cursor.execute("DELETE FROM books")