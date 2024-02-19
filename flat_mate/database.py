from pymongo import MongoClient
class Database:
    def __init__(self,connection):
        self.connection = MongoClient(connection)
        self.db = None
    
    def create_database(self,db_name):
        self.db = self.connection[db_name]

    def get_users_collection(self):
        return self.db["users"]

    def get_collection_by_name(self,collection_name):
        return self.db[collection_name]

    