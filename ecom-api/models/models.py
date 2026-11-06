from typing import Optional, List
from sqlmodel import Field, Relationship, SQLModel


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True),
    username: str = Field(index=True, unique=True)


class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, Primary_key=True)
    name: Optional[str] = Field(index=True, unique=True)
