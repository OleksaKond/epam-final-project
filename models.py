from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import Flask, config
from config import sql_uri

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = sql_uri

db = SQLAlchemy(app)


class Authors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(30))
    lname = db.Column(db.String(30))
    bdate = db.Column(db.DateTime, nullable=False)
    books = db.relationship("Books", backref='author')

    def __init__(self, fname, lname, bdate):
        self.fname = fname
        self.lname = lname
        self.bdate = bdate

    def __repr__(self):
        return f"{self.fname} {self.lname}"


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    authors_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
    genre = db.Column(db.String(30))
    order = db.relationship("Orders", backref='book')

    def __init__(self, name, author, genre):
        self.name = name
        self.author = author
        self.genre = genre

    def __repr__(self):
        return f'{self.name} - {self.author}'


class Clients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(40))
    lname = db.Column(db.String(40))
    bdate = db.Column(db.DateTime)
    reg_date = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    order = db.relationship("Orders", backref='client')

    def __init__(self, fname, lname, bdate, reg_date):
        self.fname = fname
        self.lname = lname
        self.bdate = bdate
        self.reg_date = reg_date

    def __repr__(self):
        return f"{self.fname} {self.lname}"


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    cr_date = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    till_date = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, client, book, cr_date, till_date):
        self.client = client
        self.book = book
        self.cr_date = cr_date
        self.till_date = till_date
