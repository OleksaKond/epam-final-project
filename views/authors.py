from flask import Blueprint, render_template, request, redirect, url_for
from models import Authors, Books, db
from flask_wtf import FlaskForm
from wtforms.fields import DateField, StringField, SelectMultipleField, SubmitField

authors = Blueprint('authors', __name__, template_folder='templates')


class AuthorFrom(FlaskForm):
    fname = StringField("First Name: ")
    lname = StringField("Last Name: ")
    birth_date = DateField("Birth Date: ", format="%Y-%m-%d")
    submit = SubmitField("Submit")


@authors.route('/')
def all_authors():
    if request.method == "POST":
        Authors.query.filter_by(id=request.form['id']).delete()
        db.session.commit()
        return redirect('')
    elif request.method == "GET":
        return render_template('authors/authors.html', authors=db.session.query(Authors).order_by(Authors.id))


@authors.route('/view/<author_id>/', methods=['POST', "GET"])
def view_author(author_id):
    if request.method == 'GET':
        return render_template('authors/author_view.html', form=AuthorFrom(), author=Authors.query.filter_by(id=author_id).first())
    elif request.method == 'POST':
        author = Authors.query.filter_by(id=author_id).first()
        author.fname = request.form['fname']
        author.lname = request.form['lname']
        author.bdate = request.form['birth_date']
        db.session.commit()
        return redirect(url_for('authors.all_authors'))
