import time
from Flow import *
from ManageDatabase import *
from Flow import ControlFlow
from User import User

with DatabaseConnection() as db:
    db.init_database()
    db.connection.commit()
    manager = ControlFlow(db)


    print("Your going to add a book: ")
    time.sleep(2)
    manager.add_book()
    manager.show_all_books()