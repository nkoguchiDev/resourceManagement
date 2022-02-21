# from typing import TYPE_CHECKING
from pydantic import BaseModel

# from app.db.base_class import Base

# if TYPE_CHECKING:
#     from .item import Item  # noqa: F401


class User(BaseModel):
    id: str
    email: str
    hashed_password: str
    is_active: bool = True
    is_superuser: bool = False
