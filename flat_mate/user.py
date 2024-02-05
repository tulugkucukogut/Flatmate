from flat_mate import database
class User:
    username = ""
    email = "" # it is used for id
    password_hash = ""
    salt = ""
    first_name = ""
    last_name= ""
    date_registered = ""
    last_login = ""
    account_status = ""
    role = ""
    photo = ""

    def __init__(self,email):
        self.email = email
    def insert_user(self,users_collection):
        user = {"username" : 1,
                "email": 2,
                "password_hash" : 3
        }
        result = users_collection.insert_one()