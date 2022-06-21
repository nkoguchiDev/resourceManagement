from pydantic import BaseModel


class User(BaseModel):
    id: str
    email: str
    hashed_password: str
    is_active: bool = True
    is_superuser: bool = False
