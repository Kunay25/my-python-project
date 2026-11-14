
from app.db.db import SessionLocal
from app.db.crud import get_categories, get_books


def main():
    with SessionLocal() as db:
        categories = get_categories(db)
        books = get_books(db)

        for category in categories:
            print(f"\nКатегория: {category.title}")

            for book in books:
                if book.category_id == category.id:
                    print(f"  Книга: {book.title}")
                    print(f"  Описание: {book.description}")
                    print(f"  Цена: {book.price} руб.")
                    print(f"  Ссылка: {book.url or 'нет'}")
                    print()


if __name__ == "__main__":
    main()
