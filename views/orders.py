from flask import Blueprint, render_template, request, redirect
from models import Orders, db
from flask_wtf import FlaskForm
from wtforms.fields import DateField, StringField, SelectMultipleField, SubmitField

orders = Blueprint('orders', __name__, template_folder='templates')


class OrderFrom(FlaskForm):
    fname = StringField("First Name: ")
    lname = StringField("Last Name: ")
    birth_date = DateField("Birth Date: ", format="%Y-%m-%d")
    submit = SubmitField("Submit")


@orders.route('/')
def all_orders():
    if request.method == "POST":
        if request.form['action'] == 'edit':
            pass
        elif request.form['action'] == 'delete':
            Orders.query.filter_by(id=request.form['id']).delete()
            db.session.commit()
            return redirect('')
    elif request.method == "GET":
        return render_template('orders/orders.html', orders=Orders.query.all())


@orders.route('/view/<order_id>/')
def view_order(order_id):
    return render_template('orders/order_view.html', order=Orders.query.filter_by(id=order_id).first())
