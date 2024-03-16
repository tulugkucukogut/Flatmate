from flat_mate.database import Database
from flask_login import UserMixin
class User(UserMixin):
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
        self.email = email
        CONNECTION = 'mongodb://localhost:27017/'
        self.db_instance = Database(CONNECTION)
        self.db_instance.create_database('flatmate_db')
        self.collection = self.db_instance.get_users_collection()
    

    def insert_user(self,users_collection):
        user_collection = self.db_instance.get_collection_by_name(users_collection)
        user_data = {"username" : 1,
                "email": 2,
                "password_hash" : 3
        }
        inserted_id = user_collection.insert_one(user_data).inserted_id
        return inserted_id
    
    def user_existance(self):
        user = self.collection.find_one({'email' : self.email})
        return user is not None

    def get_by_email(self,value):
        user = self.collection.find_one({'email' : self.email})
        return user if user else None
    @staticmethod
    def get(email):
        return User(email)

    

    