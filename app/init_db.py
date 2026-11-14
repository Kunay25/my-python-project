
from decimal import Decimal

from app.db.db import Base, engine, SessionLocal
from app.db import models
from app.db.crud import (
    create_category,
    create_book,
    get_categories
)


def main():
    Base.metadata.create_all(bind=engine)

    with SessionLocal() as db:

        if get_categories(db):
            print("База уже заполнена")
            return

        cat1 = create_category(
            db, "Программирование"
        )

        cat2 = create_category(
            db, "Художественная литература"
        )

        create_book(
            db, "Изучаем Python",
            "Основы программирования на Python",
            Decimal("1200.00"), cat1.id
        )

        create_book(
            db, "Чистый код",
            "Правила написания качественного кода",
            Decimal("1500.00"), cat1.id
        )

        create_book(
            db, "Алгоритмы",
            "Изучение алгоритмов и структур данных",
            Decimal("1100.00"), cat1.id
        )

        create_book(
            db, "Мастер и Маргарита",
            "Роман Михаила Булгакова",
            Decimal("800.00"), cat2.id
        )

        create_book(
            db, "Преступление и наказание",
            "Роман Фёдора Достоевского",
            Decimal("900.00"), cat2.id
        )

        create_book(
            db, "Евгений Онегин",
            "Роман Александра Пушкина",
            Decimal("700.00"), cat2.id
        )

        print("Категории и книги успешно добавлены!")


if __name__ == "__main__":
    main()
