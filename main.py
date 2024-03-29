from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from flat_mate import database
from flat_mate import user
from flat_mate import flat
from login import Login
from flask_wtf.csrf import CSRFProtect
import os
from flask_wtf.csrf import CSRFProtect
from flask_login import UserMixin, LoginManager, login_required


CONNECTION = 'mongodb://localhost:27017/'
app = Flask(__name__)
CSRFProtect(app)
#bcrypt = Bcrypt(app)
app.secret_key = os.urandom(32)  # Add a secret key for session management
csrf = CSRFProtect(app)
csrf.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'login'

db = database.Database(CONNECTION)
db.create_database('flatmate_db')
users = db.get_users_collection()
print(users)


class LoginPage(MethodView):
    def get(self):
        return render_template('login_page.html')
    
    def post(self):
        email = request.form.get("email")
        password = request.form.get("password")
        # Validate login here
        login_instance = Login(email,password)
        # Redirect to home or appropriate page after login
        if login_instance.validate_on_submit():
            return render_template('index.html')
        return render_template('login_page.html')

class SignUpPage(MethodView):
    def get(self):
        return render_template('signup.html')
    
    def post(self):
        pass
    
@login_manager.user_loader
def load_user(email):
    return user.User.get(email)


class Home(MethodView):
    @login_required
    def get(self):
        return render_template('home.html')


class BillFormPage(MethodView):
    @login_required
    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html', billform=bill_form)
    
    @login_required
    def post(self):
        # Handle form submission
        pass


class ResultsPage(MethodView):
    @login_required
    def post(self):
        # Handle form submission
        pass


class BillForm(Form):
    amount = StringField("Bill Amount: ", default="100")
    period = StringField("Bill Period: ", default="December 2020")
    name1 = StringField("Name: ", default="Andrea")
    days_in_house1 = StringField("Days in the house:", default="10")
    name2 = StringField("Name: ", default="Reea")
    days_in_house2 = StringField("Days in the house:", default="20")
    submit = SubmitField("Calculate")


app.add_url_rule("/login", view_func=LoginPage.as_view('login_page'))
app.add_url_rule("/home", view_func=Home.as_view('home'))
app.add_url_rule("/bill_form_page", view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule("/register", view_func=SignUpPage.as_view('signup'))

app.run(debug=True)