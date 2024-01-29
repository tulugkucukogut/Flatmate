from flask import Flask, render_template, request
from flask.views import MethodView
class LoginPage(MethodView):
    def get(self):
        login = Login()
        
        return render_template('login_page.html')
    


class Login():
    def __init__(self):
        pass
