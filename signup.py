from flat_mate import user
from email_validator import validate_email, EmailNotValidError
import bcrypt

class Signup():
    email =""
    password =""
    confirm_password = ""
    def __init__(self, email, password, confirm_password):
        print("XXXX")
        self.email = email
        self.password = password
        print(self.password)
        self.confirm_password = confirm_password
    
    def check_password_mismatch(self):
        if self.password != self.confirm_password:
            return True
        return False
    
    def is_valid_email(self):
        try:
            print("valid email")
            v = validate_email(self.email)
            return True
        except EmailNotValidError as e:
            return False

    def existance_email(self,collection):
        print("existance emial")
        print(collection.find_one({"email": self.email}))
        return collection.find_one({"email": self.email})

    def create_user(self,collection):
        new_user = user.User(self.email)
        new_user.password_hash = self.hash_password_bcrypt()
        new_user.insert_user(collection)
        

    
    def validate_user(self,collection):
        if not self.is_valid_email:
            print("there is not correct email")
            return False
        
        if self.existance_email(collection):
            print("There is already email")
            return False
        
        if self.check_password_mismatch():
            print("Passwords are mismatch")
            return False
        return True
        #buraya inputların düzgün girilip girilmiceğini belli etmemiz gerek

    def hash_password_bcrypt(self):
        # Password'u UTF-8'e encode et
        print("password")
        print(self.password)
        password_bytes = self.password.encode('utf-8')
        # Salt oluşturarak hash'i oluştur
        hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        # Hash'i döndür
        return hashed
        



