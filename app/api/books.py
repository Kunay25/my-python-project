
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.db import crud
from app import schemas


router = APIRouter(prefix="/books", tags=["Книги"])


@router.get("/", response_model=list[schemas.BookOut])
def get_all_books(
    category_id: int | None = None,
    db: Session = Depends(get_db)
):
    if category_id is not None:
        return crud.get_books_by_category(db, category_id)

    return crud.get_books(db)


@router.get("/{book_id}", response_model=schemas.BookOut)
def get_one_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)

    if book is None:
        raise HTTPException(404, "Книга не найдена")

    return book


@router.post("/", response_model=schemas.BookOut, status_code=201)
def add_book(data: schemas.BookCreate, db: Session = Depends(get_db)):
    category = crud.get_category(db, data.category_id)

    if category is None:
        raise HTTPException(404, "Категория не найдена")

    return crud.create_book(
        db,
        data.title,
        data.description,
        data.price,
        data.category_id,
        data.url
    )


@router.put("/{book_id}", response_model=schemas.BookOut)
def change_book(
    book_id: int,
    data: schemas.BookUpdate,
    db: Session = Depends(get_db)
):
    book = crud.get_book(db, book_id)

    if book is None:
        raise HTTPException(404, "Книга не найдена")

    category = crud.get_category(db, data.category_id)

    if category is None:
        raise HTTPException(404, "Категория не найдена")

    return crud.update_book(
        db,
        book_id,
        data.title,
        data.description,
        data.price,
        data.category_id,
        data.url
    )


@router.delete("/{book_id}")
def remove_book(book_id: int, db: Session = Depends(get_db)):
    if crud.get_book(db, book_id) is None:
        raise HTTPException(404, "Книга не найдена")

    crud.delete_book(db, book_id)

    return {"message": "Книга удалена"}
