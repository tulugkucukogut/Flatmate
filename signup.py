from flat_mate import user
from email_validator import validate_email, EmailNotValidError

class Signup():
    email =""
    password =""
    confirm_password = ""
    def __init__(self, email, password, confirm_password):
        print("burada")
        self.email = email
        self.password = password
        self.confirm_password = confirm_password
    
    def check_password_match(self):
        if self.email != self.confirm_password:
            return False
        return True
    
    def is_valid_email(self):
        try:
            v = validate_email(self.email)
            return True
        except EmailNotValidError as e:
            return False

    def existance_email(self):
        pass

