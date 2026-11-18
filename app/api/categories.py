
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.db import crud
from app import schemas


router = APIRouter(prefix="/categories", tags=["Категории"])


@router.get("/", response_model=list[schemas.CategoryOut])
def get_all_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)


@router.get("/{category_id}", response_model=schemas.CategoryOut)
def get_one_category(category_id: int, db: Session = Depends(get_db)):
    category = crud.get_category(db, category_id)

    if category is None:
        raise HTTPException(404, "Категория не найдена")

    return category


@router.post("/", response_model=schemas.CategoryOut, status_code=201)
def add_category(data: schemas.CategoryCreate, db: Session = Depends(get_db)):
    if crud.get_category_by_title(db, data.title):
        raise HTTPException(409, "Такая категория уже существует")

    return crud.create_category(db, data.title)


@router.put("/{category_id}", response_model=schemas.CategoryOut)
def change_category(
    category_id: int,
    data: schemas.CategoryUpdate,
    db: Session = Depends(get_db)
):
    category = crud.get_category(db, category_id)

    if category is None:
        raise HTTPException(404, "Категория не найдена")

    same_title = crud.get_category_by_title(db, data.title)

    if same_title and same_title.id != category_id:
        raise HTTPException(409, "Такая категория уже существует")

    return crud.update_category(db, category_id, data.title)


@router.delete("/{category_id}")
def remove_category(category_id: int, db: Session = Depends(get_db)):
    category = crud.get_category(db, category_id)

    if category is None:
        raise HTTPException(404, "Категория не найдена")

    if crud.get_books_by_category(db, category_id):
        raise HTTPException(409, "Сначала удалите книги этой категории")

    crud.delete_category(db, category_id)

    return {"message": "Категория удалена"}
