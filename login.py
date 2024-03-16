from flask import Flask, render_template, request
from flask.views import MethodView
from flat_mate import user
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user



class Login():
    email = ""
    password = ""
    def __init__(self, email, password):
        self.email = email
        self.password = password
    
    def validate_on_submit(self):
        login_user = user.User(self.email).user_existance() # it should be checked with hash
        if login_user and self.password == self.check_password():
            return True
        return False
    
    def check_password(self):
        user_data = user.User(self.email).get_by_email(self.email)
        if user_data:
            return user_data.get('password_hash',None)
        else: 
            return None
        
