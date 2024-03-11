from flask import Flask, render_template, request
from flask.views import MethodView
from flat_mate import user
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


#you should take the query with user id
@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))

class LoginPage(MethodView):
    def get(self):
        return render_template('login_page.html')
    
    def post(self):
        username = request.form.get("user_name")
        print(username)
        password = request.form.get("password")
        user_instance = user.User("dnm")
        inserted_id = user_instance.insert_user("users")

    


class Login():
    user_name = ""
    password = ""
    def __init__(self, username, password):
        self.user_name = username
        self.password = password
    
    def validate_user(self, username):
        pass
        
