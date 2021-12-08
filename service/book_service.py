from models import db, Books


def get_book(**kwargs):
    book = Books.query.filter_by(**kwargs).first()
    return book


def get_books(**kwargs):
    books = Books.query.filter_by(**kwargs)
    return books


def get_books_all():
    return Books.query.all()


def add_book(**kwargs):
    try:
        book = Books(**kwargs)
        db.session.add(book)
        return True
    except:
        print("Error adding")


def update_book(id1=None, **kwargs):
    book = get_book(id=id1)
    keys = kwargs.keys()  # new_data in your case is filenames
    # you want to update
    for key in keys:
        print(f"book.{key} = kwargs['{key}']")
        exec(f"book.{key} = kwargs['{key}']")
    db.session.commit()
    return True


def delete_book(id1=None):
    db.session.delete(get_book(id=id1))
    db.session.commit()