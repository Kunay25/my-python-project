
from sqlalchemy import select
from .models import Category, Book



def create_category(db, title):
    category = Category(title=title)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def get_categories(db):
    return db.scalars(select(Category)).all()


def update_category(db, category_id, new_title):
    category = db.get(Category, category_id)

    if category is not None:
        category.title = new_title
        db.commit()
        db.refresh(category)

    return category


def delete_category(db, category_id):
    category = db.get(Category, category_id)

    if category is not None:
        db.delete(category)
        db.commit()
        return True

    return False



def create_book(db, title, description, price, category_id):
    book = Book(
        title=title,
        description=description,
        price=price,
        url="",
        category_id=category_id
    )

    db.add(book)
    db.commit()
    db.refresh(book)
    return book


def get_books(db):
    return db.scalars(select(Book)).all()


def update_book(db, book_id, new_price):
    book = db.get(Book, book_id)

    if book is not None:
        book.price = new_price
        db.commit()
        db.refresh(book)

    return book


def delete_book(db, book_id):
    book = db.get(Book, book_id)

    if book is not None:
        db.delete(book)
        db.commit()
        return True

    return False
