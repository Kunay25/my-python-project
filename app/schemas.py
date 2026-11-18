
from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field



class CategoryBase(BaseModel):
    title: str


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass


class CategoryOut(CategoryBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class BookBase(BaseModel):
    title: str
    description: str
    price: Decimal = Field(ge=0)
    url: str | None = None
    category_id: int


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass


class BookOut(BookBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
