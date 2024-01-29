from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, jsonify
from flask import Flask, render_template, request
from flat_mate import database
from flat_mate import flat
from login import LoginPage


CONNECTION = 'mongodb://localhost:27017/'
app = Flask(__name__)
db = database.Database(CONNECTION,'flatmate_db')



@app.route('/users', methods=['GET'])
def get_users():
    users = db.get_users()
    user_list = []
    for user in users:
        print("xx")
        user_list.append({
            'username': user['username'],
            'email': user['email']
            # Add other fields as needed
        })
    return jsonify({'users': user_list})

class HomePage(MethodView):
    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):
    def get(self):
        bill_form = BillForm()
        
        return render_template('bill_form_page.html',billform=bill_form)
    
    def post(self):
        billform = BillForm(request.form)
        the_bill = flat.Bill(float(billform.amount.data),billform.period.data)
        flatmate1 = flat.Flatmate(billform.name1.data,float(billform.days_in_house1.data))
        flatmate2 = flat.Flatmate(billform.name2.data,float(billform.days_in_house2.data))
        return render_template("bill_form_page.html", result = True,
                                            billform=billform, name1 = flatmate1.name, amount1 = flatmate1.pays(the_bill,flatmate2),
                                            name2 = flatmate2.name, amount2 = flatmate2.pays(the_bill,flatmate1))


class ResultsPage(MethodView):
    def post(self):
        billform = BillForm(request.form)
        the_bill = flat.Bill(float(billform.amount.data),billform.period.data)
        flatmate1 = flat.Flatmate(billform.name1.data,float(billform.days_in_house1.data))
        flatmate2 = flat.Flatmate(billform.name2.data,float(billform.days_in_house2.data))
        return render_template("results.html", name1 = flatmate1.name, amount1 = flatmate1.pays(the_bill,flatmate2),
                                            name2 = flatmate2.name, amount2 = flatmate2.pays(the_bill,flatmate1))
 
class BillForm(Form):
    amount = StringField("Bill Amount: ", default="100")
    period = StringField("Bill Period: ", default="December 2020")

    name1 = StringField("Name: ", default="Andrea")
    days_in_house1 = StringField("Days in the house:", default="10")

    name2 = StringField("Name: ", default="Reea")
    days_in_house2 = StringField("Days in the house:", default="20")

    submit = SubmitField("Calculate")

app.add_url_rule("/", view_func= LoginPage.as_view('login_page'))
app.add_url_rule("/home", view_func= HomePage.as_view('home_page'))
app.add_url_rule("/bill_form_page", view_func= BillFormPage.as_view('bill_form_page'))
#app.add_url_rule("/results", view_func= ResultsPage.as_view('results_page'))

app.run(debug=True)
