from flat_mate import user
from email_validator import validate_email, EmailNotValidError

class Signup():
    email =""
    password =""
    confirm_password = ""
    def __init__(self, email, password, confirm_password):
        self.email = email
        self.password = password
        self.confirm_password = confirm_password
    
    def check_password_mismatch(self):
        if self.email != self.confirm_password:
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
        



