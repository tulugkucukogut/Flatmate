from pymongo import MongoClient
class Database:
    def __init__(self,connection,db_name):
        self.connection = MongoClient(connection)
        self.db = self.connection[db_name]
        self.users = self.db.users
    
    def get_users(self):
        return self.users.find()
    