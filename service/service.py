from models import db, Books, Authors, Clients, Orders


def get(obj=None, **kwargs):
    return eval(f"{obj}.query.filter_by({kwargs}).first()")


def get_one(obj=None, **kwargs):
    return eval(f"{obj}.query.filter_by({kwargs})")


def get_all(item=None):
    return eval(f"{item}.query.all()")


def add(obj=None, **kwargs):
    try:
        eval(f"item={obj}({kwargs})")
        eval(f"db.session.add(item)")
        return True
    except:
        print("Error adding")


def update(obj=None, id1=None, **kwargs):
    keys = kwargs.keys()  # new_data in your case is filenames
    # you want to update
    for key in keys:
        eval(f"{get(obj=obj, id=id1)}.{key} = kwargs['{key}']")
    db.session.commit()
    return True


def delete(obj=None, id1=None):
    db.session.delete(get(obj=obj, id=id1))
    db.session.commit()
