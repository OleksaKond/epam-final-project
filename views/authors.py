from flask import Blueprint, render_template, request, redirect
from models import Authors, Books, db

authors = Blueprint('authors', __name__, template_folder='templates')


@authors.route('/')
def all_authors():
    if request.method == "POST":
        if request.form['action'] == 'edit':
            if request.form['item'] == 'book':
                author = Authors.query.filter_by(id=request.form['id'])
                author.fname = request.form['fname']
                author.lname = request.form['lname']
                author.bdate = request.form['bdate']
                db.session.commit()
        elif request.form['action'] == 'delete':
            Authors.query.filter_by(id=request.form['id']).delete()
            db.session.commit()
            return redirect('')
    elif request.method == "GET":
        return render_template('authors/authors.html', authors=Authors.query.all())


@authors.route('/view/<author_id>/')
def view_author(author_id):
    return render_template('authors/author_view.html', author=Authors.query.filter_by(id=author_id).first(),
                           books=Books.query.filter_by(authors_id=author_id))
