from flask import Blueprint, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms.fields import DateField, StringField, SelectMultipleField, SubmitField, SelectField
from service import service

books = Blueprint('books', __name__, template_folder='templates')


class BookForm(FlaskForm):
    name = StringField("Name: ")
    author = SelectMultipleField("Author: ", choices=service.get_all('Authors'))
    genre = DateField("Birth Date: ", format="%Y-%m-%d")
    submit = SubmitField("Submit")


@books.route('/', methods=['GET', "POST"])
def all_books():
    if request.method == "POST":
        service.delete("Books", request.form['id'])
        return redirect('')
    elif request.method == "GET":
        return render_template('books/books.html', books=service.get_all("Books"))


@books.route('/view/<book_id>/', methods=['GET', 'POST'])
def view_book(book_id):
    if request.method == "GET":
        return render_template('books/book_view.html', book=service.get('Books', id=book_id), authors=service.get_all("Authors"))
    elif request.method == 'POST':
        service.update("Books", book_id, id=book_id, name=request.form['name'], authors_id=int(request.form['author']), genre=request.form['genre'])
        return redirect(url_for('books.all_books', books=service.get_all()))


@books.route('/create/', methods=['GET', 'POST'])
def create_book():
    if request.method == "GET":
        return render_template("books/book_view.html")