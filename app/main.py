
from fastapi import FastAPI
from sqlalchemy import text

from app.api import books, categories
from app.db.db import engine


app = FastAPI(title="Магазин книг")


app.include_router(books.router)
app.include_router(categories.router)


@app.get("/health")
def health():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))

    return {"status": "ok"}
