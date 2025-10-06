
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


        