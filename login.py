from flask import Flask, render_template, request
from flask.views import MethodView
from flat_mate import user
class LoginPage(MethodView):
    def get(self):
        return render_template('login_page.html')
    
    def post(self):
        username = request.form.get("user_name")
        print(username)
        password = request.form.get("password")
        user_instance = user.User("dnm")
        inserted_id = user_instance.insert_user()

    


class Login():
    def __init__(self):
        pass
