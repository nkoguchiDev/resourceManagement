# from typing import TYPE_CHECKING
from pydantic import BaseModel

# from app.db.base_class import Base

# if TYPE_CHECKING:
#     from .item import Item  # noqa: F401


class User(BaseModel):
    id: str
    full_name: str
    email: str
    hashed_password: str
    is_active: bool
    is_superuser: bool
    items: str
