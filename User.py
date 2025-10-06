
class User:
    def __init__(self, id, name, age, gender, phone, email, items_borrowed=None):
        if items_borrowed is None:
            self.items_borrowed = []
        else:
            self.items_borrowed = items_borrowed
        
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.email = email

    def borrow_book(self, book_id, cursor):
        cursor.execute("INSERT INTO borrowed_books (user_id, book_id) VALUES (?, ?)", (self.id, book_id))

    def return_book(self, book_id, cursor):
        cursor.execute("DELETE FROM borrowed_books WHERE user_id = ? AND book_id = ?", (self.id, book_id))
    
    def show_books(self, cursor):
        cursor.execute("""
        SELECT books.id, books.title
        FROM books
        JOIN borrowed_books 
        ON books.id = borrowed_books.book_id 
        WHERE borrowed_books.user_id = ?""", (self.id,))
        return cursor.fetchall()


        