from flask import Blueprint, render_template, request, redirect, url_for
from models import Books, Authors, db

books = Blueprint('books', __name__, template_folder='templates')


@books.route('/')
def all_books():
    if request.method == "POST":
        Books.query.filter_by(id=request.form['id']).delete()
        db.session.commit()
        return redirect('')
    elif request.method == "GET":
        return render_template('books/books.html', books=Books.query.all())


@books.route('/view/<book_id>/', methods=['GET', 'POST'])
def view_book(book_id):
    if request.method == "GET":
        return render_template('books/book_view.html', book=Books.query.filter_by(id=book_id).first(), authors=Authors.query.all())
    elif request.method == 'POST':
        book = Books.query.filter_by(id=book_id).first()
        book.name = request.form['name']
        book.genre = request.form['genre']
        book.authors_id = Authors.query.filter_by(id=request.form['author'].split()[0]).first().id
        db.session.commit()
        return redirect(url_for('books.all_books', books=Books.query.all()))
