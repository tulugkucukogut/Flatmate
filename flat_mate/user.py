from flat_mate.database import Database
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
    db_instance = ""

    def __init__(self,email):
        CONNECTION = 'mongodb://localhost:27017/'
        self.db_instance = Database(CONNECTION)
        self.db_instance.create_database('flatmate_db')
        self.email = email
    

    def insert_user(self,users_collection):
        user_collection = self.db_instance.get_collection_by_name(users_collection)
        user_data = {"username" : 1,
                "email": 2,
                "password_hash" : 3
        }
        inserted_id = user_collection.insert_one(user_data).inserted_id
        return inserted_id