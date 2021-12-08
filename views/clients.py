from flask import Blueprint, render_template, request, redirect
from models import Clients, db
from flask_wtf import FlaskForm
from wtforms.fields import DateField, StringField, SelectMultipleField, SubmitField

clients = Blueprint('clients', __name__, template_folder='templates')


class ClientFrom(FlaskForm):
    fname = StringField("First Name: ")
    lname = StringField("Last Name: ")
    birth_date = DateField("Birth Date: ", format="%Y-%m-%d")
    submit = SubmitField("Submit")


@clients.route('/')
def all_clients():
    if request.method == "POST":
        if request.form['action'] == 'edit':
            pass
        elif request.form['action'] == 'delete':
            Clients.query.filter_by(id=request.form['id']).delete()
            db.session.commit()
            return redirect('')
    elif request.method == "GET":
        return render_template('clients/clients.html', clients=Clients.query.all())


@clients.route('/view/<client_id>/')
def view_client(client_id):
    return render_template('clients/client_view.html', client=Clients.query.filter_by(id=client_id).first())
