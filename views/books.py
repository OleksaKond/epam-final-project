from flask import Blueprint, render_template, request, redirect, url_for
from models import Books, Authors, db
from service import book_service

books = Blueprint('books', __name__, template_folder='templates')


@books.route('/', methods=['GET', "POST"])
def all_books():
    if request.method == "POST":
        book_service.delete_book(request.form['id'])
        return redirect('')
    elif request.method == "GET":
        return render_template('books/books.html', books=Books.query.all())


@books.route('/view/<book_id>/', methods=['GET', 'POST'])
def view_book(book_id):
    if request.method == "GET":
        return render_template('books/book_view.html', book=Books.query.filter_by(id=book_id).first(), authors=Authors.query.all())
    elif request.method == 'POST':
        print(request.form['author'])
        book_service.update_book(book_id, id=book_id, name=request.form['name'], authors_id=int(request.form['author']), genre=request.form['genre'])
        return redirect(url_for('books.all_books', books=Books.query.all()))
