from flask import render_template, request, redirect
from models import Books, Authors, Clients, Orders, db, app
from views.books import books
from views.authors import authors
from views.clients import clients
from views.orders import orders


app.register_blueprint(books, url_prefix="/books")
app.register_blueprint(authors, url_prefix="/authors")
app.register_blueprint(clients, url_prefix="/clients")
app.register_blueprint(orders, url_prefix="/orders")

app.config['SECRET_KEY']='LOL'

GENRES = ["Romance",
          "Crime",
          "Thriller",
          "Fantasy",
          "Sci-fi",
          "Children's",
          "Religious",
          "Self-help"]


@app.route('/')
@app.route('/home/')
def home_page():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
